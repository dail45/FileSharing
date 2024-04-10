from typing import List
from Structures import File


class Directory:
    def __init__(self, name):
        self.name = name
        self.children: List[File | Directory] = []
