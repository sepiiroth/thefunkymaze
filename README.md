# <p align="center"> **The Funky Maze** </p>
## <p align="center"> Rafael, Kyllian, Julien, Ruben </p>
This project is a Maze solver that also generate a new maze everytime the project is launched.  
Everytime the maze is generated, we made sure that the maze is solvable.  
  
  
This project uses the genetic algorithm with the Manhattan distance.  
Here is how it works. It will go through every possible way until it’s stuck, and comparing all the possible direction it will choose the one with the shortest way to the end.
  
   
Each generation represent multiple tries to move in the maze, and each try in this generation is an individual.  
Each individual will move in the maze while it’s not stuck. At the end of each generation it will return the best individual (the closest to the finish line).  
  
  
  
Theses generations will keep going until the fitness is 1 (Got to the finish line) or if the max number generation is reached.

  
# <p align="center"> **How to use it** </p>
## 1 - Install Evocraft
Install [Evocraft-py](https://github.com/real-itu/Evocraft-py#evocraft-py), a Python interface for Minecraft.
## 2 - Copy files
Download and copy to root of minecraft server.
## 3 - Run it
Run the project with `py main.py`
## 4 - Enjoy !

Presentation video available [here](https://www.youtube.com/watch?v=Om1x9R1SdxA)
