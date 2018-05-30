from tkinter import *
from tkinter import ttk
from math import *
import xml.etree.ElementTree as et

gui_columns = 5 # amount of columns in a gui row

class MetalInfo:

    def __init__(self, starting_dict):
        self.info = starting_dict
        self.name = self.info["name"]

def read_metal_info(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    metal_infos = {}
    
    for child in root:
        current_info = MetalInfo(child.attrib)
        metal_infos[current_info.name] = current_info
        #metal_infos.append(current_info)

    return metal_infos

def info_into_frame(frame, metal_info):
    Label(frame, text=metal_info.info["name"]).grid(column=1, row=1)
    Label(frame, text=metal_info.info["price"]).grid(column=1, row=2)
    Label(frame, text=metal_info.info["density"]).grid(column=1, row=3)
    Label(frame, text=metal_info.info["tensile_strength"]).grid(column=1, row=4)
    Label(frame, text=metal_info.info["thermal_conductivity"]).grid(column=1, row=5)
    Label(frame, text=metal_info.info["melting_point"]).grid(column=1, row=6)
    Label(frame, text=metal_info.info["specific_heat"]).grid(column=1, row=7)

## these two could be genericized together but it isn't worth the effort
def label_into_frame(frame):
    Label(frame, anchor="w", text="").grid(column=1, row=1)
    Label(frame, anchor="w", text="Price").grid(column=1, row=2)
    Label(frame, anchor="w", text="Density").grid(column=1, row=3)
    Label(frame, anchor="w", text="Tensile strength").grid(column=1, row=4)
    Label(frame, anchor="w", text="Thermal conductivity").grid(column=1, row=5)
    Label(frame, anchor="w", text="Melting point").grid(column=1, row=6)
    Label(frame, anchor="w", text="Specific heat").grid(column=1, row=7)

## fills a frame with a grid of frames
def fill_frame(mainframe, width, height):
    frames = []

    for w in range(0, width):
        for h in range(0, height):
            current_frame = ttk.Frame(mainframe, padding="3 3 3 3")
            current_frame.grid(column=w, row=h)
            frames.append(current_frame)
        
    return frames

## parses tree and returns base frame
def read_frame_tree(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    return root.find("Frame")

def grid_frames(count, frame):
    height = ceil(count / gui_columns)
    
    return fill_frame(frame, gui_columns, height)

class TreeStepper:

    def __init__(self, base_frame, mainframe, metal_infos):
        self.base = base_frame
        self.current_tag = self.base
        self.mainframe = mainframe
        self.supframe = None
        self.regrid(len(list(self.base)))
        self.metal_infos = metal_infos

    def regrid(self, count):
        if self.supframe != None:
            self.supframe.destroy()
            
        self.supframe = ttk.Frame(self.mainframe, padding="3 3 3 3")
        self.supframe.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frames = grid_frames(count, self.supframe)

    def step(self, index):
        """ Step one tag deeper into the tree """
        self.current_tag = self.current_tag[index]
        #self.output.configure(text=self.current_tag.tag)
        self.evaluate_current()
        
    def options_to_buttons(self):
        buttons = []
        i = 0
        
        def make_option_select(index):

            def option_select():
                self.step(index)

            return option_select

        for options in self.current_tag:
            option_select = make_option_select(i)
            current_button = Button(self.frames[i],
                                    text=self.current_tag[i].attrib["value"],
                                    wraplength=100,
                                    command=option_select)
            current_button.grid(column=0, row=0)
            i += 1

    def leaves_to_labels(self):
        i = 0
        length = len(list(self.current_tag))
        self.regrid(length + ceil(length / gui_columns)) # add one more frame to each row for labels
        for leaf in self.current_tag:
            if i % gui_columns == 0:
                label_into_frame(self.frames[i])
            else:
                info_into_frame(self.frames[i], self.metal_infos[leaf.attrib["value"]])
            i += 1

    def evaluate_current(self):
        """ Act based on current tag """
        if self.current_tag.tag == "Option":
            if self.current_tag[0].tag == "Leaf":
                self.leaves_to_labels()
            else:
                self.current_tag = self.current_tag[0] 
        
        if self.current_tag.tag == "Frame":
            self.regrid(len(list(self.current_tag)))
            self.options_to_buttons()

def main():

    root = Tk()

    root.title("Corrosion Decisions")
    
    mainframe = ttk.Frame(root, padding="3 3 3 3")
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    metal_infos = read_metal_info("data/MetalInfo.xml")

    frame_tree = read_frame_tree("data/MyMaterialV2.xml")

    stepper = TreeStepper(frame_tree, mainframe, metal_infos)

    #dump all metal info
    #frames = grid_frames(43, mainframe)
    #for i in range(0, 42):
    #    info_into_frame(frames[i], metal_infos[i])

    stepper.options_to_buttons()
    
    root.mainloop()
    
if __name__=="__main__":
   main()
