# Kit Builder Autosave and Crash Recovery Feature

This report documents the implementation of atomic autosaving, background draft persistence, and interactive crash recovery in the `gmcli build` workflow.

---

## 1. Problem Statement & Architecture

Previously, `gmcli build` maintained questions, answers, and metadata strictly in volatile process memory (`KitBuilderModel.kit.Questions`). Write-to-disk operations were deferred entirely until `phaseSaveDestination`. If a machine rebooted, terminal closed, or power failed prior to confirming the save destination, all entered questions were lost.

---

## 2. Solution Architecture

The autosave subsystem introduces a zero-latency, atomic persistence layer that guarantees unsaved authoring progress survives abrupt process termination, terminal disconnects, and system reboots.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Autosave Lifecycle                              │
│                                                                        │
│  [Question Added / Updated / Deleted / Renamed]                        │
│                           │                                            │
│                           ▼                                            │
│            Atomic Write: <draft_path>.tmp.<nano>                       │
│                           │                                            │
│                           ▼ (Atomic POSIX Rename)                      │
│                  `.draft_<slug>.json`                                  │
│                           │                                            │
│            ┌──────────────┴──────────────┐                             │
│            ▼                             ▼                             │
│     [Save Kit & Exit]          [Machine Reboot / Crash]                │
│            │                             │                             │
│            ▼                             ▼                             │
│  Target: `<slug>.json`            Run `gmcli build`                    │
│  Delete: `.draft_<slug>.json`            │                             │
│                                          ▼                             │
│                                [RESUME DRAFT] Option                   │
│                                (Pre-selected at top)                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Key Enhancements Implemented

### A. Atomic Disk Persistence
* **Atomic Rename**: In [`run/script/loader.go`](file:///home/owen/Projects/ai_projects/gmcli/run/script/loader.go), `SaveToFile` writes to a sibling temporary file (`<path>.tmp.<timestamp>`) and executes an atomic POSIX rename (`os.Rename`). This ensures that even power loss mid-write cannot leave a corrupted or truncated draft.
* **Continuous Synching**: In [`run/gui/builder.go`](file:///home/owen/Projects/ai_projects/gmcli/run/gui/builder.go), `autoSaveDraft()` executes automatically whenever:
  * A new question is added.
  * An existing question is modified.
  * A question is deleted.
  * Kit title or author metadata is updated.

### B. Draft Naming & Path Resolution
* **Standard Prefix**: Drafts use hidden dotfiles prefixed with `.draft_`:
  * Target `chapter_12.json` -> `.draft_chapter_12.json`
  * Subdirectory `kits/chapter_12.json` -> `kits/.draft_chapter_12.json`
  * New kit with title `Operating Systems` -> `.draft_operating_systems.json`
* **Clean Renaming**: If a kit's title is edited from the Question Hub, the existing draft is automatically cleaned up and replaced with the new title slug.

### C. Seamless Draft Discovery & Restoration
* **Startup Detection**: When `gmcli build` is launched without arguments, `DiscoverLocalKitsWithDrafts(".")` searches the current folder and subdirectories for active drafts.
* **Top-Level Priority**: Any detected drafts appear at the top of the selection list prefixed with `[RESUME DRAFT]` and are selected by default. Pressing `<Enter>` restores the entire kit into the Question Hub immediately.
* **CLI Target Resolution**: If invoked with an explicit argument (e.g. `gmcli build chapter_12.json` or `gmcli build -o chapter_12.json`), `gmcli` checks for an existing `.draft_chapter_12.json`. If the draft exists (or if the target file was never saved before crashing), it automatically loads the draft progress.

### D. Lifecycle Cleanup & Discard Controls
* **Automatic Cleanup on Save**: Once the user completes `phaseSaveDestination` and saves to the final kit JSON, the corresponding `.draft_*.json` is deleted.
* **Explicit Discard Option**: In the Question Hub, if an active draft is detected, users are provided with an explicit menu option: `Discard Draft & Exit (Delete autosaved progress)`.
* **Safe Preserves on Cancellation**: If a user cancels out of the save prompt using `<Ctrl+C>`, the draft is preserved and a message is printed directing the user to `gmcli build` to resume later.

---

## 4. Verification & Test Battery

The implementation is verified by an 8-stage automated test suite in [`run/tests/autosave_draft_test.go`](file:///home/owen/Projects/ai_projects/gmcli/run/tests/autosave_draft_test.go):

```text
=== RUN   TestPathResolutionFunctions
--- PASS: TestPathResolutionFunctions (0.00s)
=== RUN   TestAutoSaveDraftOnQuestionAdded
--- PASS: TestAutoSaveDraftOnQuestionAdded (0.00s)
=== RUN   TestAutoSaveDraftOnQuestionEditedAndDeleted
--- PASS: TestAutoSaveDraftOnQuestionEditedAndDeleted (0.00s)
=== RUN   TestAutoSaveDraftOnTitleChange
--- PASS: TestAutoSaveDraftOnTitleChange (0.00s)
=== RUN   TestDraftCleanedUpOnFinalSave
--- PASS: TestDraftCleanedUpOnFinalSave (0.00s)
=== RUN   TestDiscoverDraftsRecursive
--- PASS: TestDiscoverDraftsRecursive (0.00s)
=== RUN   TestResumeDraftFromSelectMenu
--- PASS: TestResumeDraftFromSelectMenu (0.00s)
=== RUN   TestAtomicSaveIntegrity
--- PASS: TestAtomicSaveIntegrity (0.00s)
PASS
ok      gmcli/run/tests 0.017s
```

All 34 test suites across the repository pass cleanly:

```text
ok      gmcli/run/tests 0.109s
```

---

## 5. Binary Installation

The executable at [`/home/owen/.local/bin/gmcli`](file:///home/owen/.local/bin/gmcli) (linked to [`/home/owen/Projects/ai_projects/gmcli/gmcli`](file:///home/owen/Projects/ai_projects/gmcli/gmcli)) has been compiled and updated with the new autosave capabilities.
