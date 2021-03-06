# D&D character creator

![Image](/images/demo.png)

### About

This program is used to generate a random level 1 character for dungeons & dragons game, written completely in python

The project was created in order to speed up character creation process for one-shot style games, where players don't need to invest so much into their characters.

**This program heavily relies upon pseudorandom number generation**

All data related to character creation is from [D&D Beyond](https://www.dndbeyond.com/). You can find more about D&D and it's details from the website. The application is limited to contain only details listed in "The Player's Handbook" -module.

### Features
Currently the program has the following features:
- Saving rolled characters in .json format
- Character details:
  - Class traits
  - Attributes
  - Starting items (bags, tools, etc.)
  - Starting equipment
  - Races, Racial attributes and abilities

Nice to haves and potential development ideas:
- Make a GUI for the application
- Add random name generation based on race
- Add spell and trait details

### Usage

Clone the latest version and run start.bat (Windows) or start.sh (Unix).

### Determining random elements

**Attributes**
The program uses a standard procedure for attribute generation:

`4d6 - the smallest roll`

This gives the generated character a start with attributes between 3-18, with a weight towards larger numbers.

*Note: the attributes can be larger than 18 with racial bonuses.*

**Equipment**
- Equipment is selected by selecting one option of from all available options

**Spells, skills and skewing the random factor**
- Spells are randomly selected from the class' spell pool
- The number of spells and spell slots are defined by the class

- Skills are not selected randomly (may be subject to change)
  - This is means that you should still select the skills your character is proficient in.
  - This option was chosen in order to still have some freedom in character creation

## Development environment

To start the development of this program, simply clone the repository and start modifying the code via your favorite text editor or IDE for python.

### Project Structure

```
D-D-charCreator:. (root Directory)
├───data (data files, created after first startup)
├───images (images to display in github page)
└───src (source code for the program)
```

Notes:
- The src -directory contains all the code related to the application
- The data folder is created when the application is run for the first time and it contains all the data generated by the application
