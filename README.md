[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/agandar1/pyproject06">
    <img src="images/python.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">World's Hardest Game AI</h3>

  <p align="center">
    Python Project for CSCI-3329-90L-Spring2021
    <br />
    <br />
    <a href="https://github.com/agandar1/pyproject06/issues">Report Bug or Request Feature</a>
  </p>
</p>
 


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Running The Game</a></li>
    <li><a href="#roadmap">Progress</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Screenshot][product-screenshot]]() 

'[World's Hardest Game](https://www.crazygames.com/game/worlds-hardest-game)' is a browser flash game released in 2007.
The objective is to maneuver a red square across multiple maps, all while avoiding blue dots, and collecting yellow dots.
As the name suggests, this simple game is actually rather difficult to master. One can spend countless hours simply
trying over and over to complete a level.

The goal of this project is to create an implementation of the game in python, and then create an AI
that is capable of beating each level. To do this, we will use a genetic algorithm to have the program
solve levels through trial and error just like a human would.


### Built With

* [Python](https://www.python.org)
* [The Python Arcade Library](https://arcade.academy)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

For the program to run, you need to have python3 and the arcade library installed on your system.
* Linux
  * Python
  ```
  install via your package manager
  ```
  * Arcade 
  ```sh
  $ pip3 install --user arcade
  ```

### Installation

1. To get a copy of the project, simply clone the repo
   ```sh
   $ git clone https://github.com/agandar1/pyproject06.git
   ```


<!-- USAGE EXAMPLES -->
## Running the game

1. Go into the game directory 
   ```sh
   $ cd pyproject06/game
   ```
2. Run the main game file
   ```sh
   $ ./main.py
   ```



<!-- ROADMAP -->
## Progress

* This is what we have accomplished so far:
    * 8 levels of the game complete
    * Collisions with walls, enemies, and coins work
    * Enemy dots can follow a path or go in a circle
    * Player death and respawn works
    * Checkpoint system works
    * Winning a level works

* This is what we still have to add:
    * All of the AI system

* Features we would like but are not priority:
    * Extra game levels
    * A title screen
    * A menu to choose level
  
  

<!-- CONTACT -->
## Contact

Alfonso Barrera - a.barrera.29123@gmail.com  
Hugo Franco Rodriguez - hugo_afranco@hotmail.com  
Adan Gandarilla - agandarilla0502@gmail.com

Project Link: [https://github.com/agandar1/pyproject06](https://github.com/agandar1/pyproject06)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[alfonso-link]:https://github.com/null-integer
[hugo-link]:https://github.com/HugoFranc
[adan-link]:https://github.com/agandar1
[contributors-shield]: https://img.shields.io/github/contributors/agandar1/pyproject06.svg?style=for-the-badge
[contributors-url]: https://github.com/agandar1/pyproject06/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/agandar1/pyproject06.svg?style=for-the-badge
[issues-url]: https://github.com/agandar1/pyproject06/issues
[product-screenshot]: images/screenshot.png 
