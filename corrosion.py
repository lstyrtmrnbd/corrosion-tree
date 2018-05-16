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

    # argument is tuples of key:value pairs for dictionary
    def __init__(self, starting_dict):
        #self.picture = pairs.get("picture")
        #self.price = pairs.get("price")
        #self.melting_pt = pairs.get("melting_pt")
        #self.tensile_str = pairs.get("tensile_str")
        #self.density = pairs.get("density")
        #self.other_facts = pairs.get("other_facts") # list of other facts

        self.info = starting_dict
        
def info_into_frame(frame, metal_info):
    return None
        
def main():

    root = Tk()

    root.title("Corrosion Decisions")
    
    frame = ttk.Frame(root, padding="3 3 3 3")
    frame.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    ss_304 = MetalInfo({
        "name":"SS 304",
        "picture":"",
        "Price":"4.69",
        "Density":"490 - 500",
        "Tensile strength":"74 - 90",
        "Thermal conductivity":"2.62 - 3.18",
        "Melting point":"2552 - 2642",
        "Specific Heat":"0.37 - 0.41"
    })

    root.mainloop()

# misc. API examples: 
# blue1 = Node("Whatever end")
# red1 = Node("Whatever i say", blue1, child2)
# Node.branch(childValue)
# Tree(rootNode)

if __name__=="__main__":
   main()
