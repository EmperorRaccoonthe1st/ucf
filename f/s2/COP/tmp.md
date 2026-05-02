Now to plan a prompt architect prompt.                                                         
   Take the following prompt and improve it, ensuring discrete final, and enriched output: 

# Role
You are a master prompt architect & engineer.

Your goal is to take two source prompts @documents/CDA_GEMINI.md and @documents/CHM_GEMINI.md, and combining them to result in an improved final product that takes the best from both sources.
The document @documents/COP_GEMINI.md will provide starting point to begin development of the final GEMINI folder that will reside in the parent directory of the project.

You will improve them based on my feedback on the final projects they resulted in, in addition to your own rigorous review.

# Pre-Planning Structure

The project will consist of phases of review and design where swarms of agents write their findings into .md files that are sorted into project subdir's within the @GEMINI/ folder.

The final product will be a series of in-depth instructions located within the @GEMINI folder starting with a master_outline.md and then following phase_n.md's

Project_Plan:
GEMINI/
GEMINI/master_outline.md
GEMINI/phase_(n).md

Subdir's:
GEMINI_PLAN/
GEMINI_PLAN/prompt_review
GEMINI_PLAN/project_review
GEMINI_PLAN/learnings

Planning Documents:
GEMINI_PLAN/prompt_plan.md
GEMINI_PLAN/prompt_style.md

 
## Phases
You will conduct your document engineering in phases:
1. You will begin with a swarm review of each prompt itself, ensuring that an agent is placed on each prompt. They will write their initial review into the prompt_review dir
2. You will then spawn a large swarm of high quality agents to review each finished review document. As these .pdf files are very large it is **IMPORTANT** that you properly create a large amount of agents to perform deep reviews of every segment of the .pdf files. These agents will write their findings into the project_review dir
3. Another round of agents will investigate the intermediate findings that each project generated (found within the @CDA/ and @CHM/ dir's respectively) and report their findings also to the @project_review/ dir
4. A new round of agents will then review the initial prompts again with the findings found on the projects and update the .md files found within the prompt_review dir.
5. Now that both supporting dirs are complete, a new round will then synthesize the knowledge gathered about the prompts, the projects, and their effectiveness, into a set of complete lesson.md files in the learning directory
6. With all of the supporting investigation gathered, you will build a prompt_plan.md file.
7. The same will be done with the prompt_style.md to ensure that the resulting prompt has been architected and stylized to perfection.

8. Once all the prep has been completed, generate begin work on the master architecture file based on the documents GEMINI_PLAN/prompt_plan.md and GEMINI_PLAN/prompt_style.md. 
- You will generate a series of phase_n.md files to direct each phase of the project.
- These files be explicit, instructions that describe each step in detail.
- They will utilize many subagents to preserve context.
- They will have multiple rounds of review for each step within each phase. With at least *2* phases destined to provide review
- There will be a series of final review rounds and revisions to ensure document quality and consistency
