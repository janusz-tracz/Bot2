import pygame

from enum import Enum
from collections import defaultdict

import random
import copy
import pprint

from gupb2.model import characters

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


class BotController:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BotController):
            return True
        return False

    def __hash__(self) -> int:
        return 47

    def reset(self) -> None:
        pass

    def decide(self) -> characters.Action:
        return 550

    @property
    def name(self) -> str:
        return self.__name

