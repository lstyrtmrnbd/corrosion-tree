from tkinter import *
from tkinter import ttk

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

def main():

    root = Tk()

    root.title("Corrosion Decisions")
    
    frame = ttk.Frame(root, padding="3 3 3 3")
    frame.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    root.mainloop()

# misc. API examples: 
# blue1 = Node("Whatever end")
# red1 = Node("Whatever i say", blue1, child2)
# Node.branch(childValue)
# Tree(rootNode)

if __name__=="__main__":
   main()
