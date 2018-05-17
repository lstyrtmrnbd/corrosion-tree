from tkinter import *
from tkinter import ttk

class MetalInfo:

    def __init__(self, starting_dict):
        self.info = starting_dict

metal_infos = [

    MetalInfo({
        "name":"SS 304",
        "picture":"",
        "Price":"4.69",
        "Density":"490 - 500",
        "Tensile strength":"74 - 90",
        "Thermal conductivity":"2.62 - 3.18",
        "Melting point":"2552 - 2642",
        "Specific heat":"0.37 - 0.41"
    }),

    MetalInfo({
        "name":"SS 316",
        "picture":"",
        "Price":"4.69",
        "Density":"491-504",
        "Tensile strength":"70 - 90",
        "Thermal conductivity":"24/3 - 3.18",
        "Melting point":"2507 - 2552",
        "Specific heat":"0.38 - 0.41"
    }),

    MetalInfo({
        "name":"",
        "picture":"",
        "Price":"",
        "Density":"",
        "Tensile strength":"",
        "Thermal conductivity":"",
        "Melting point":"",
        "Specific heat":""
    }),

    ]

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

    def __init__(self, metal_infos_list):
        Node.__init__(self, "")
        self.metal_infos = metal_infos_list

def info_into_frame(frame, metal_info):
    return None
        
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
