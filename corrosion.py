from tkinter import *


class Tree:

    def __init__(self, root_node):
        self.current_node = root_node

    def branch(self, child_val):
        self.current_node = self.current_node.children[child_val]

class Node:

    def __init__(self, text, *children):
        self.children = children
        self.text = text

class Leaf(Node):

    def __init__(self, *metal_infos):
        Node.__init__(self, "")
        self.metal_infos = metal_infos

class MetalInfo:

    def __init__(self, **kwargs):
        self.picture = kwargs.get("picture")
        self.price = kwargs.get("price")
        self.melting_pt = kwargs.get("melting_pt")
        self.tensile_str = kwargs.get("tensile_str")
        self.density = kwargs.get("density")
        self.other_facts = kwargs.get("other_facts") # list of other facts
        

blue1 = Node("Whatever end")

red1 = Node("Whatever i say", blue1, child2)

Node.branch(childValue)

Tree(rootNode)

tree1 = Tree(red1)

tree1.branch(val)

    currentNode = currentNode.child(val)
