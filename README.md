# Speedy's Redstone Computer
An 8-bit redstone computer built in survival Minecraft

# Showcase Videos
[Main Video](https://youtu.be/eiUsxeEPTxg) (clean) - shows the process of learning logical redstone, designing the computer in creative mode, gathering the materials, tediously building and debugging it in survival, and then begging for subs for my hard work.

[Supplementary Video](https://youtu.be/PHiXify_t88) - includes more in-depth explanations of how each component works, how the programs work, and how to make programs on the computer yourself. Also includes some of my final thoughts on the making of the video itself.

# Internal Specs
- 8-bit ALU with 12 different operations
- Unconditional and conditional jump instructions
- Custom 15-bit assembly language (instruction set [here](https://docs.google.com/spreadsheets/d/14Qfy51s3phwDlEMzL42IVlzITjZjRA52z8LBtbNxOmA/edit?usp=sharing))
- 64-line instruction memory
- 8-byte register file
- 16-byte RAM to which the I/O is mapped

# Peripherals
- Binary coded decimal input
- Directional "controller" input
- Random number generator
- Combinational numeric seven-segment display for a single number
- Sequential alphanumeric display for combinations of letters and digits
- 8x8 pixel screen

# Installing the world
All worlds were made in Minecraft 1.20.4 and have not been tested for compatibility with future or past versions.

[WorldEdit](https://www.curseforge.com/minecraft/mc-mods/worldedit) and [Carpet Mod](https://www.curseforge.com/minecraft/mc-mods/carpet) are also highly recommended, unless you want to wait 10 minutes for programs to run.

To install the creative world, do the following:
- Clone the repository
- In the saves folder of the repository, extract the zip of the world you want to install
- Put the resulting save folder in your Minecraft saves folder (`.minecraft/saves ` in most cases)

If you would like to explore the survival world, you must instead download it from [here](https://drive.google.com/drive/folders/1Lw7-j1egIcE07191JQoU-_3Eb2NIuFvM), as it is too large to upload to GitHub. Note that there is basically no advantage of making programs with the survival computer as opposed to the creative build.

# Programming the computer
The following is also covered at [58:36](https://youtu.be/PHiXify_t88?t=3516) in the supplementary video.

- Write your program in assembly
  - Use the [instruction set](https://docs.google.com/spreadsheets/d/14Qfy51s3phwDlEMzL42IVlzITjZjRA52z8LBtbNxOmA/edit?usp=sharing) and the already existing programs in the repository as a guide
  - All instructions must include a line number (e.g., `0. LDI...`)
  - Use `//` for comments
  - Optionally, use the provided `redstone_computer.xml` user-defined language file in Notepad++ for color formatting
 
- Assemble the program into machine code
  - Run `redstone_assembler.py`
  - Enter the name of your program, e.g., `program.txt`
  - The assembler will save the machine code in `program_assembled.txt`

- Put the program in the computer
  - Clear any existing program (repeaters) in the instruction memory (which is dark blue in the creative build)
    - This can more easily be done with WorldEdit:
      - `//wand` to get a wand (wood axe)
      - Select each side separately of the instruction memory where the machine code is
      - `//replace repeater air` to delete the repeaters
  - Put your new machine code in
    - Repeaters go where there is a 1, and blank spaces go where there is a 0
    - The left side of the machine code instruction is the top of the vertical line in the instruction memory
   
- Run and debug the program
  - Use Carpet Mod to speed up the game (`/tick rate 1000`)
  - Press the reset button (attached to the black wire in the creative build) to go back to line 0 and restart the program
  - If necessary, use the debug switch (on the lower gold platform) to switch to debug mode, where you can manually go one line at a time
  - If even further debugging is needed, use the switches on the program counter (which is colored magenta) to force the program to jump to an exact instruction

# Possible Improvements
There is a library called [mcschematic](https://pypi.org/project/mcschematic/) to procedurally generate schematics that can be pasted into a world. This has potential to eliminate the tedious process of manually placing repeaters to program the computer in creative mode. However, since the main point of the project was to build it in survival with no mods, for which this library would not help much, I have not looked into it yet.

This is my first (and possibly only) redstone computer, and as such, its design is quite inefficient. Other redstone computers exist with clock periods as fast as 3 Hz, whereas mine is 0.1 Hz. My computer could also benefit from other types of instructions such as branching with offsets.

# Special Thanks
First and foremost, the [old](https://www.youtube.com/playlist?list=PL5LiOvrbVo8ksCgm_HTLfwhHRdnx11Gms) and [new](https://www.youtube.com/playlist?list=PL5LiOvrbVo8keeEWRZVaHfprU4zQTCsV4) Logical Redstone series by mattbatwings were incredibly helpful places for me to start. If it were not for this series, the build would probably be 10 times bigger.

Some miscellaneous redstone help came from [Mumbo Jumbo](https://www.youtube.com/watch?v=fBdC1pvxfI0) and [ianxofour](https://youtu.be/n3mOlrMGjUg).

My team of early access reviewers for the main video includes [Contranaut](https://www.youtube.com/@iPodBen), [eewalktub](https://www.youtube.com/@eewalktub8907), [jr5000](https://www.youtube.com/@jr5000pwp), and [SchmidtPlays](https://www.youtube.com/@schmidt1816).

Editing inspiration for the main video came from [Testable](https://www.youtube.com/@testableyt), [RedPenGuin111](https://www.youtube.com/@redpenguin111), and [rekrap2](https://www.youtube.com/@rekrap2). The first two are also contributors to said video.
