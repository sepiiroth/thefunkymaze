# **The Funky Maze**
This project is a Maze solver that also generate a new maze everytime the project is launched.
Everytime the maze is regenerated, we made sure that the maze is solvable. This project use the
algogen with the Manhattan distance. Here is how the it works, It will go trought every possible way
until it’s stuck, and comparing all the differents direction it will choose the one with the shortest way
to the end.
Each generation represent multiple tries to move in the maze, and each try in this generation is an
individual.
Each individual will move in the maze while it’s not stuck. At the end of each generation it will return
the best individual (the closest to the finish line). Theses generations will keep going until the fitness
is 1 (Got to the finish line) or if the max number generation is reached.


1 - Install Evocraft here : https://github.com/real-itu/Evocraft-py
2 - Copy files on root server 
3 - Run main with "py main.py"
4 - Enjoy !

Presentation video here : https://www.youtube.com/watch?v=Om1x9R1SdxA
