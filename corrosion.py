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
        "Thermal conductivity":"26.2 - 31.8",
        "Melting point":"2552 - 2642",
        "Specific heat":"0.37 - 0.41",
    }),

    MetalInfo({
        "name":"SS 316",
        "picture":"",
        "Price":"4.69",
        "Density":"491-504",
        "Tensile strength":"70 - 90",
        "Thermal conductivity":"24.3 - 31.8",
        "Melting point":"2507 - 2552",
        "Specific heat":"0.38 - 0.41",
    }),

    MetalInfo({
        "name":"Aluminum",
        "picture":"",
        "Price":"1.95",
        "Density":"160 - 184",
        "Tensile strength":"10.9 - 52.2",
        "Thermal conductivity":"150 - 412",
        "Melting point":"931 - 1304",
        "Specific heat":"0.214",
    }),

    MetalInfo({
        "name":"Aluminum 3xxx",
        "picture":"",
        "Price":"1.95",
        "Density":"169 - 171",
        "Tensile strength":"18.9",
        "Thermal conductivity":"100",
        "Melting point":"1190 - 1210",
        "Specific heat":"0.21",
    }),

    MetalInfo({
        "name":"Nickel",
        "picture":"",
        "Price":"6.34",
        "Density":"551 - 559",
        "Tensile strength":"50 - 145",
        "Thermal conductivity":"52",
        "Melting point":"2614 - 2670",
        "Specific heat":"0.35 - 0.36",
    }),

    MetalInfo({
        "name":"Nickel Alloy",
        "picture":"",
        "Price":"8",
        "Density":"510",
        "Tensile strength":"65-120",
        "Thermal conductivity":"5.7",
        "Melting point":"2350 - 2460",
        "Specific heat":"0.1",
    }),

    MetalInfo({
        "name":"NiCrFe 600",
        "picture":"",
        "Price":"8",
        "Density":"529",
        "Tensile strength":"75.4 - 120",
        "Thermal conductivity":"8.61",
        "Melting point":"2469 - 2575",
        "Specific heat":"0.106",
    }),

    MetalInfo({
        "name":"NiCrFe690",
        "picture":"",
        "Price":"8.5",
        "Density":"511",
        "Tensile strength":"66.8 - 84",
        "Thermal conductivity":"7",
        "Melting point":"2450-2510",
        "Specific heat":"0.108",
    }),

    MetalInfo({
        "name":"NiCrFe800",
        "picture":"",
        "Price":"7",
        "Density":"496",
        "Tensile strength":"75 - 85",
        "Thermal conductivity":"7.08",
        "Melting point":"2475 - 2525",
        "Specific heat":"0.11",
    }),

    MetalInfo({
        "name":"NiMo",
        "picture":"",
        "Price":"20-50",
        "Density":"574",
        "Tensile strength":"125",
        "Thermal conductivity":"6.41",
        "Melting point":"2840",
        "Specific heat":"0.09 - 0.093",
    })
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
