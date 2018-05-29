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

def new_frame_callback(tag_parent, gui_frame):
    return None

def refresh_frame(frame):
    if frame is not None:
        frame.destroy()
    frame = ttk.Frame(root, padding="3 3 3 3")
    frame.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.columconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

def find_info(name):
    # finds the metal_info with this name
    return None

def into_frame(tag_frame, gui_frame):
    max_width = 5
    length = list(tag_frame).length()
    height = ceil(length / 5)

    refresh_frame(gui_frame)

    frames = fill_frame(gui_frame, max_width, height)
    
    if tag_frame is option:
        # loop through leaves and output the correct metal_infos
        for i in range(0, frames.length()):
            info_into_frame(frames[i], find_info(gui_frame[i].attrib["value"]))
        
    if tag_frame is frame:
        # loop through leaves and output the options as buttons
        for i in range(0, frames.length()):
            button = ttk.Button(frames[i], text=tag_frame[i].attrib["value"])
            button.grid(column=0, row=0)
        
                
def main():

    root.title("Corrosion Decisions")
    
    mainframe = ttk.Frame(root, padding="3 3 3 3")
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    frames = fill_frame(mainframe, 7, 1)

    metal_infos = read_metalinfo("data/MetalInfo.xml")

    #frame_tree = read_frame_tree("data/MyMaterialV2.xml")

    info_into_frame(frames[0], metal_infos[0])
    info_into_frame(frames[1], metal_infos[1])
    info_into_frame(frames[2], metal_infos[2])

    root.mainloop()
    
if __name__=="__main__":
   main()
