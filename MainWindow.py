import os
from Maze import Maze
from ga import *
import config as cf
import grpc

import minecraft_pb2
import minecraft_pb2_grpc
from minecraft_pb2 import *

channel = grpc.insecure_channel('localhost:5001')
client = minecraft_pb2_grpc.MinecraftServiceStub(channel)


class MainWindow:
    width = 100
    height = 100
    maze = None

    def __init__(self, width, height):
        self.maze = Maze(width, height)
        self.width = self.maze.width
        self.height = self.maze.height
    def genMaze(self):
        self.resetMaze()
        blocks = []
        genMaze = True
        while genMaze:
            for y, x in self.maze.getToDraw():
                blocks.append(Block(position=Point(x=x, y=3, z=y), type=self.maze.getBlock(y, x), orientation=NORTH))
            if len(self.maze.frontier) == 0:
                genMaze = False
                break
            self.maze.workOneStep()
        client.spawnBlocks(Blocks(blocks=blocks))

    def resetMaze(self):
        blocks = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                blocks.append(Block(position=Point(x=x, y=3, z=y), type=OBSIDIAN, orientation=NORTH))
        client.spawnBlocks(Blocks(blocks=blocks))
