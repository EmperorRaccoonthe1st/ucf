#u Prompt

## Part One
Information Inventory & Content Strategy

You probably know much more about your topic than your audience needs to know. Professional writers must therefore make decisions about what information to include, what to emphasize, and what to leave out.

Begin by brainstorming everything your audience might potentially need to know about your topic.

Then sort the information into three categories:

1. Must Know

Information the audience needs in order to understand the topic or accomplish the purpose of your document.

2. Useful to Know

Information that may help the audience but is not essential.

3. Don't Need to Know

Information you know but that does not serve this particular audience or purpose.

After categorizing your information, create a Content Strategy showing how you will organize the information your audience actually needs.

Your Content Strategy should identify:

Your document's main message
3–5 major pieces of information your audience needs
Supporting information for each major point
Information you deliberately decided to exclude
The action you want your audience to take

Conclude by explaining at least two decisions you made because of your audience analysis.

## Part Two

The "So What?" Test

Information becomes rhetorically useful when the writer can explain why the audience needs it. Therefore as you begin to map the ideas you should include on your document for the Professional Information Project, you need to determine what needs to be communicated. 
Activity

List ten facts about your topic from the activity above. 

Then create two columns:

 
Information 	Why Does My Audience Need to Know This? 
Fact 1 	So what? 
Fact 2 	So what?
Fact 3 	So what?
etc... 	

If you cannot answer the second column, you need to reconsider whether the information belongs in the document.
Submit

Compile the work completed for part one and part two into one document. I am flexible on some of the formatting, as long as it makes sense to me as I review. 

# Response

## Part One

My professional document will be about the code editor _Vim_, in particular the _VS Code_ Extension for _Vim_.
It will primly focus on conveying basic usage of the code editor and the philosophy that supports its particular manner of editing.

### Information Inventory

#### Must Know

1. _Core Navigation_
    - How to move the cursor.
2. _Modal Editing_
    - The fundamental philosophy behind the _Vim_ code editor.
3. _Essential Modes_
    - How one operates the program.
4. _File Operations_
    - Saving and editing files, behaviors that are required to work with a project.

#### Useful to Know

1. _Advanced Navigation_
    - Specific mechanisms for moving efficiently throughout a file.
2. _Editing Operators_
    - Controls for editing entire blocks of text.
3. _Operator Combination_
    - High level logic that allows for chains of commands.
4. _Search Operator_
    - Mechanisms for retrieving and editing specific parts of document.

#### Don't Need to know

1. _Terminal Vim_
    - Downloading and operating Vim from a terminal. The document will only be explaining _Vim_ concepts that can be utilized anywhere.
2. _REGEX_
    - REGEX is a advanced pattern matching tool that can be used in search strings, it is outside the scope of this document.
3. _Buffer Management_
    - The ability to open new visual panes, which display text concurrently.
4. _Configuration_
    - _Vim_ contains an entire scripting/configuration language, actually two entire languages. These topics require a deeper analysis than can be provided in this document.

### Content Strategy

The essential message of my document will be explaining how to properly utilize _Vim_ in an introductory manner.
As the program is very complex, it is essential that the guide covers only the most necessary features and concepts to allowing a new user to start working within it.
For this reason the guide will follow how to use an extension to the popular _VS Code_ that uses only the core features of _Vim_, rather than the actual terminal application.

The audience will require, in the following order, three key concepts in order to gain a basic understanding of _Vim_.
They will begin with an overview of the Modal Editing Paradigm, which is the concept of editing data through utilizing specific tools, or modes.
Applications like image editors or 3D modeling tools function in this manner, where users rotate between different tools that all behave differently.
Once modal editing has been established, navigation throughout a project will be the first topic covered.
This requires the explanation and memorization of the functions of a myriad of keys.
Each key in vim performs some action, and there are around ten keys to learn for basic navigation.
Now that the audience can navigate we will turn to actually performing some productive edits, with basic operators.
As with navigation, every key performs something different and thus has to be learned.
Finally the guide will end with file level commands, like saving or exiting.
These operate on a higher plane than a user's edits, with there being a core few that should be learned for basic usage.

There is an enormous amount of information that could be covered in the document but I have decided to ignore the majority of it.
Specifically I will not cover configuration and the command line.
_Vim_ can be configured through a file written with a _Domain Specific language_ (vimscript), learning an entire language in an introductory guide is impractical.
The program is also typically interacted within the terminal and the command line (CMD).
As the audience will instead be learning through the _VS Code_ extension, I will not mention any of the numerous command line quirks that can be found when using native _Vim_.

I intent for the audience to download and follow along to the guide themselves.
Following along will provide the most efficient manner to learning the information presented.
I have decided to use to use the _VS Code_ extension due to my audience's lack of command line knowledge.
It is simpler to introduce _Vim_ itself to begin with and then allow them to dive into the CMD when they are ready.
Additionally, I will be framing _Vim_ primarily as a code editing tool rather than a general purpose text editor (I'm using it currently to write this document).
This framing will appeal to the audience due to their programming background, as means for enhancing their efficiency.


## Part Two

1. _Vim_ utilizes different modes to edit text.
    - This allows for complex chains of actions and utilization of soley the keyboard.
2. Pressing 'I' enters insert mode.
    - This is one primary manner of adding text to a document.
3. Pressing 'Esc' or 'ctrl-c' returns the user to normal mode.
    - This is required to switch modes throughout vim.
4. The keys 'h', 'j', 'k', and 'l' control directional cursor navigation.
   - This keeps navigation bound entirely to the keyboard home row.
5. Pressing 'w' and 'b' advances the cursor forward and backward across words.
   - This enables rapid traversal through tokens without repeated keystrokes.
6. Pressing 'x' deletes the character currently under the cursor.
   - This allows quick single-character corrections without switching to insert mode.
7. Pressing 'dd' deletes a line, while 'yy' copies it to the clipboard.
   - This executes line-level manipulation commands in a single streamlined action.
8. Pressing 'p' pastes the most recently yanked or deleted text after the cursor.
   - This completes basic cut and paste operations entirely within normal mode.
9. Pressing 'u' undoes changes, while 'ctrl-r' redoes them.
   - This provides essential recovery controls directly through the keyboard interface.
10. Pressing ':' opens the command-line interface for ex-commands like ':w' and ':q'.
    - This executes core file operations such as saving and closing buffers.
