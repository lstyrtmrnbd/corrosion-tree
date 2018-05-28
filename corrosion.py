from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as et

class MetalInfo:

    def __init__(self, starting_dict):
        self.info = starting_dict
        self.name = self.info["name"]

def read_metalinfo(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    metal_infos = []
    
    for child in root:
        current_info = MetalInfo(child.attrib)
        metal_infos.append(current_info)

    return metal_infos

def info_into_frame(frame, metal_info):
    metal_name = ttk.Label(frame, text=metal_info.info["name"])
    metal_name.grid(column=1, row=1)
    metal_price = ttk.Label(frame, text=metal_info.info["price"])
    metal_price.grid(column=1, row=2)
    metal_density = ttk.Label(frame, text=metal_info.info["density"])
    metal_density.grid(column=1, row=3)
    metal_tensile = ttk.Label(frame, text=metal_info.info["tensile_strength"])
    metal_tensile.grid(column=1, row=4)
    metal_thermal = ttk.Label(frame, text=metal_info.info["thermal_conductivity"])
    metal_thermal.grid(column=1, row=5)
    metal_melting = ttk.Label(frame, text=metal_info.info["melting_point"])
    metal_melting.grid(column=1, row=6)
    metal_specific = ttk.Label(frame, text=metal_info.info["specific_heat"])
    metal_specific.grid(column=1, row=7)

def message_into_frame(frame, message):
    message_label = ttk.Label(frame, text=message)
    message.grid(column=1, row=1)

## fills a frame with a grid of frames
def fill_frame(mainframe, width, height):
    frames = []

    for w in range(0, width):
        for h in range(0, height):
            current_frame = ttk.Frame(mainframe)
            current_frame.grid(column=w, row=h)
            frames.append(current_frame)
        
    return frames

class Tree:

    def __init__(self, root_node):
        self.current_node = root_node

    def branch(self, child_index):
        self.current_node = self.current_node.children[child_index]

class Node:

    def __init__(self, options, *children):
        self.children = children
        self.options = options

    def option_button(self, frame, option_index):
        button = ttk.Button(frame, text=options[option_index])

    def into_frame(self, frame):
        frames = fill_frame(frame, options.length(), 1)

        for i in range(0, frames.length()):
            self.option_button(frame[i], i)

class Leaf(Node):

    def __init__(self, metal_infos_list):
        Node.__init__(self, "")
        self.metal_infos = metal_infos_list
     
def main():

    root = Tk()

    root.title("Corrosion Decisions")
    
    mainframe = ttk.Frame(root, padding="3 3 3 3")
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    frames = fill_frame(mainframe, 7, 1)

    metal_infos = read_metalinfo("data/MetalInfo.xml")

    info_into_frame(frames[0], metal_infos[0])
    info_into_frame(frames[1], metal_infos[1])
    info_into_frame(frames[2], metal_infos[2])

    root.mainloop()
    
# misc. API examples: 
# blue1 = Node("Whatever end")
# red1 = Node("Whatever i say", blue1, child2)
# Node.branch(childValue)
# Tree(rootNode)

if __name__=="__main__":
   main()
