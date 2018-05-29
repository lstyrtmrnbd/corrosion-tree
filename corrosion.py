from tkinter import *
from tkinter import ttk
from math import *
import xml.etree.ElementTree as et

root = Tk()

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

## fills a frame with a grid of frames
def fill_frame(mainframe, width, height):
    frames = []

    for w in range(0, width):
        for h in range(0, height):
            current_frame = ttk.Frame(mainframe)
            current_frame.grid(column=w, row=h)
            frames.append(current_frame)
        
    return frames

## parses tree and returns base frame
def read_frame_tree(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    return root.find("Frame")

def make_select_option(tag_frame):

    def select_option():
        into_frame(tag_frame[0], gui_frame)
        
        return None
        
    return select_option

def refresh_frame(frame):
    if frame is not None:
        frame.destroy()
    frame = ttk.Frame(root, padding="3 3 3 3")
    frame.grid(column=0, row=0, sticky=(N, S, E, W))

def find_info(name):
    # finds the metal_info with this name
    return None

def grid_frames(count, frame):
    max_width = 5
    height = ceil(count / 5)
    
    return fill_frame(frame, max_width, height)
    
def into_frame(tag_frame, gui_frame):

    if tag_frame.tag == "Option":
        # loop through leaves and output the correct metal_infos
        for i in range(0, len(frames)):
            info_into_frame(frames[i], find_info(tag_frame[i].attrib["value"]))

    if tag_frame.tag == "Frame":
        # loop through and output the options as buttons
        for i in range(0, len(frames)):
            button = ttk.Button(frames[i], text=tag_frame[i].attrib["value"], command=select_option)
            button.grid(column=0, row=0)

class TreeWalker:

    def __init__(self, base_frame, mainframe):
        self.base = base_frame
        self.current_frame = self.base
        self.current_option = self.base[0]
        self.mainframe = mainframe
        self.frames = grid_frames(len(list(self.base)), mainframe)
        
    def options_to_buttons(self):

        def option_select():
            return None
    
        buttons = []
        i = 0
        for options in self.current_frame:
            i += 1
            current_button = ttk.Button(self.frames[i], command=option_select)
            current_button.grid(column=0, row=0)
            
        
def main():

    root.title("Corrosion Decisions")
    
    mainframe = ttk.Frame(root, padding="3 3 3 3")
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    metal_infos = read_metalinfo("data/MetalInfo.xml")

    frame_tree = read_frame_tree("data/MyMaterialV2.xml")

    #walker = TreeWalker(frame_tree, mainframe)

    frames = grid_frames(43, mainframe)

    for i in range(0, 42):
        info_into_frame(frames[i], metal_infos[i])

    #walker.options_to_buttons()
    
    root.mainloop()
    
if __name__=="__main__":
   main()
