# Chapter 4: Sequential Logic Design

## 1. Introduction to Sequential Logic
Unlike combinational circuits where outputs depend purely on current inputs, **sequential circuits** have \"State\" (memory). Their outputs depend on both current inputs and the history of past inputs (previous outputs).
*   **Memory Elements:** Store the current state.
*   **Combinational Logic:** Computes the *next state* and *outputs* based on the input and current state.
*   **Steady-State Abstraction:** Sequential design relies on reasoning about steady-state behaviors. Outputs are only observed after sufficient time has elapsed for the system to settle. State changes are only permitted at specific times (controlled by a clock).

## 2. Latches
A latch is a fundamental memory element where the output equals the stored state, and the state changes whenever appropriate inputs change (event-driven).

### Set-Reset (S-R) Latch
Built from cross-coupled NOR or NAND gates, the S-R latch can force its output to 0 (reset) or 1 (set).
*   **States:** Hold, Set, Reset, Unstable
*   **Truth Table (NOR-based S-R Latch):**
    *   `S=0, R=0`: Hold State (Q remains unchanged)
    *   `S=0, R=1`: Reset State (Q = 0)
    *   `S=1, R=0`: Set State (Q = 1)
    *   `S=1, R=1`: Unstable/Not Allowed (forces both Q and Q' to 0 in a NOR latch). Entering and leaving this state can cause unpredictable oscillations or race conditions.
*   **Characteristic Equation:** $Q(t+\Delta) = S + R' Q(t)$

### Clocked (Gated) S-R Latch
To prevent accidental unstable states and control *when* inputs are sampled, a clock signal is added using AND gates before the S and R inputs. The inputs to the cross-coupled NOR gates can only change when the clock is asserted (high).
*   **Behavior:** When clock is 1, the latch is \"open\" and S/R inputs can change the state. When clock is 0, the latch is \"closed\" and holds its value.

## 3. Flip-Flops
A flip-flop is a memory element built from clocked latches. Unlike latches which are level-sensitive, flip-flops are **edge-triggered**, meaning their internal state changes *only* on a clock edge (rising or falling).

### D Flip-Flop (Data Flip-Flop)
*   **Inputs:** `D` (data to be stored) and `C` (clock).
*   **Outputs:** `Q` and `Q'`.
*   **Behavior:** On the active clock edge, $Q$ becomes equal to $D$.
*   **Structure:** Often constructed using cascaded latches configured in a master-slave arrangement so that the unstable state cannot propagate.

### T (Toggle) and J-K Flip-Flops
*   **T Flip-Flop:** Toggles its state on the clock edge if $T=1$. If $T=0$, it holds. Characteristic equation: $Q(t+1) = T \oplus Q(t)$.
*   **J-K Flip-Flop:** Solves the unstable state issue of the S-R latch. 
    *   `J=0, K=1`: Reset
    *   `J=1, K=0`: Set
    *   `J=1, K=1`: Toggle
    *   Characteristic equation: $Q(t+1) = J Q'(t) + K' Q(t)$.

## 4. Timing Methodologies
Systems heavily rely on synchronous timing controlled by periodic clock signals.
*   **Duty Cycle:** The ratio of time the clock is \"high\" to the total clock period.
*   **Setup Time ($T_{su}$):** Minimum time inputs must be valid/steady *before* the clock edge.
*   **Hold Time ($T_h$):** Minimum time inputs must be valid/steady *after* the clock edge.
*   **Metastability / Synchronizer Failure:** If asynchronous inputs transition during the setup/hold window, the flip-flop can enter an unresolved/metastable state. A **synchronizer** (usually two D flip-flops in series) is used to safely translate asynchronous inputs into synchronous ones.
*   **Clock Skew:** The difference in time between when two state elements see the same clock edge. Max clock period must account for skew to avoid incorrect data capture.

## 5. Counters & Registers
Collections of flip-flops sharing a clock and similar logic form basic hardware elements.
*   **Data Registers:** Hold multi-bit binary values. New values are loaded when a `Write Enable` signal is asserted.
*   **Shift Registers:** Hold a sequence of input samples. A 4-bit shift register moves its stored bits left or right per clock cycle. A **Universal Shift Register** permits parallel/serial input and output, as well as bidirectional shifting.
*   **Register Files:** Sets of registers accessible via decoders and multiplexers by supplying a register number to read or write.
*   **Counters:** Sequence through a fixed set of patterns.
    *   *Binary Counters:* Count in standard binary (or Grey Code, where only 1 bit changes per step to prevent transient errors).
    *   *Mobius (Johnson) Counter:* Sequences like `1000 -> 1100 -> 1110 -> 1111 -> 0111...`

## 6. Finite State Machines (FSMs)
Sequential circuits are mathematically described as FSMs, consisting of a set of states, a next-state function, and an output function.

### FSM Design Steps (Example: 1001 Overlapping Pattern Recognizer)
1.  **State Diagram & Table:** Define states (e.g., A=000, B=001, etc.) and map transitions based on inputs.
2.  **State Encoding:** Assign binary values to each state. If there are 5 states, 3 flip-flops are needed. Unused states become *don't cares*.
3.  **Find Boolean Expressions:** Use Karnaugh Maps to derive minimum sum-of-products (SOP) expressions for the inputs of the flip-flops (e.g., $D_2, D_1, D_0$) and the outputs (e.g., $Y$).
    *   *Example Minterms:* $D_2 = \overline{X} Q_1 \overline{Q_0}$, $Y = Q_1 Q_0$.
4.  **Draw Logic Circuit:** Combine combinational gates with the D flip-flops.

### Moore vs. Mealy Machines
*   **Moore Machine:** The outputs depend *only* on the current state. In state diagrams, the output is typically written inside the state node. The logic circuit's output gates are driven entirely by the flip-flop outputs ($Q$).
*   **Mealy Machine:** The outputs depend on *both* the current state and the current inputs. In state diagrams, the output is written on the transition arrows (Input/Output). This allows for faster responses to inputs but can lead to asynchronous glitches if inputs change mid-cycle.