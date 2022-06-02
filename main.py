import os
from Maze import Maze
import random
from ga import *
import config as cf
import time
import grpc

import minecraft_pb2
import minecraft_pb2_grpc
from Maze import Maze
from MainWindow import MainWindow

from minecraft_pb2 import *
channel = grpc.insecure_channel('localhost:5001')
client = minecraft_pb2_grpc.MinecraftServiceStub(channel)


if __name__ == '__main__':
    window = MainWindow(cf.MAZE_WIDTH, cf.MAZE_HEIGHT)
    window.genMaze()
    ga = GA(cf.GENERATIONS, cf.POPULATION_SIZE, cf.MUTATION_RATE, cf.START_COORDS, cf.END_COORDS, window.maze)

    run = True

    while run and ga.curgen < ga.gen and not ga.victory:
        print("Current generation:", ga.curgen)
        ga.nextGen()
        toReset = set()
        for p in ga.population:
            blocks = []
            for y, x in p.path:
                toReset.add((y, x))
                blocks.append(Block(position=Point(x=x, y=3, z=y), type=p.color, orientation=NORTH))
            client.spawnBlocks(Blocks(blocks=blocks))

        blocks = []

        for y, x in toReset:
            blocks.append(Block(position=Point(x=x, y=3, z=y), type=STONE, orientation=NORTH))
        client.spawnBlocks(Blocks(blocks=blocks))

        #time.sleep(0.5)

    print("Best path found", ga.bestPlayer)
    run = True
    while run:
        blocks = []
        for y, x in ga.bestPlayer.path:
            blocks.append(Block(position=Point(x=x, y=3, z=y), type=EMERALD_BLOCK, orientation=NORTH))
            client.spawnBlocks(Blocks(blocks=blocks))
