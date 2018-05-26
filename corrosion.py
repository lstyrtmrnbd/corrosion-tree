from tkinter import *
from tkinter import ttk

class MetalInfo:

    def __init__(self, starting_dict):
        self.info = starting_dict

metal_infos = [
    MetalInfo({
        "name":"Carbon Steel",
        "picture":"",
        "Price":"1",
        "Density":"490",
        "Tensile strength":"92.1",
        "Thermal conductivity":"132-645",
        "Melting point":"2600 - 2800",
        "Specific heat":"0.12",
    }),

    MetalInfo({
        "name":"SS 304",
        "picture":"",
        "Price":"4.69",
        "Density":"490 - 500",
        "Tensile strength":"74 - 90",
        "Thermal conductivity":"112-149",
        "Melting point":"2552 - 2642",
        "Specific heat":"0.37 - 0.41",
    }),

    MetalInfo({
        "name":"SS 316",
        "picture":"",
        "Price":"4.69",
        "Density":"491-504",
        "Tensile strength":"70 - 90",
        "Thermal conductivity":"113",
        "Melting point":"2507 - 2552",
        "Specific heat":"0.38 - 0.41",
    }),

    MetalInfo({
        "name":"Aluminum",
        "picture":"",
        "Price":"1",
        "Density":"168.5",
        "Tensile strength":"1.8-20.3",
        "Thermal conductivity":"625-1710",
        "Melting point":"1220",
        "Specific heat":"0.165",
    }),

    MetalInfo({
        "name":"Aluminum 3xxx",
        "picture":"",
        "Price":"1",
        "Density":"169 - 171",
        "Tensile strength":"18.9",
        "Thermal conductivity":"1200",
        "Melting point":"1170-1210",
        "Specific heat":"0.21",
    }),

    MetalInfo({
        "name":"Nickel 200",
        "picture":"",
        "Price":"12",
        "Density":"555",
        "Tensile strength":"68",
        "Thermal conductivity":"487",
        "Melting point":"2615-2635",
        "Specific heat":"0.109",
    }),

    MetalInfo({
        "name":"Nickel 205",
        "picture":"",
        "Price":"9",
        "Density":"555",
        "Tensile strength":"65",
        "Thermal conductivity":"306",
        "Melting point":"2615-2635",
        "Specific heat":"0.109",
    }),

    MetalInfo({
        "name":"Nickel 270",
        "picture":"",
        "Price":"9",
        "Density":"555",
        "Tensile strength":"50",
        "Thermal conductivity":"597",
        "Melting point":"2649",
        "Specific heat":"0.11",
    }),

    MetalInfo({
        "name":"Inconel 600",
        "picture":"",
        "Price":"8",
        "Density":"529",
        "Tensile strength":"95",
        "Thermal conductivity":"103.32",
        "Melting point":"2469 - 2575",
        "Specific heat":"0.106",
    }),

    MetalInfo({
        "name":"Inconel 690",
        "picture":"",
        "Price":"8.5",
        "Density":"511",
        "Tensile strength":"110",
        "Thermal conductivity":"84",
        "Melting point":"2450-2510",
        "Specific heat":"0.108",
    }),

    MetalInfo({
        "name":"Incoloy 800",
        "picture":"",
        "Price":"7",
        "Density":"496",
        "Tensile strength":"87",
        "Thermal conductivity":"84.96000000000001",
        "Melting point":"2475 - 2525",
        "Specific heat":"0.11",
    }),

    MetalInfo({
        "name":"NiMo",
        "picture":"",
        "Price":"20-50",
        "Density":"574",
        "Tensile strength":"125",
        "Thermal conductivity":"76.92",
        "Melting point":"2840",
        "Specific heat":"0.09 - 0.093",
    }),

    MetalInfo({
        "name":"Titanium",
        "picture":"",
        "Price":"25.5",
        "Density":"281.7",
        "Tensile strength":"31.9",
        "Thermal conductivity":"117.96000000000001",
        "Melting point":"3000 - 3040",
        "Specific heat":"0.13",
    }),

    MetalInfo({
        "name":"Aluminum 7xxx",
        "picture":"",
        "Price":"2",
        "Density":"169-180",
        "Tensile strength":"10-105",
        "Thermal conductivity":"798-1540",
        "Melting point":"889-1220",
        "Specific heat":"0.205-0.229",
    }),

    MetalInfo({
        "name":"Ti-6Al-4V",
        "picture":"",
        "Price":"10.00-12.00",
        "Density":"276",
        "Tensile strength":"131",
        "Thermal conductivity":"46.5",
        "Melting point":"2919-3020",
        "Specific heat":"0.1258",
    }),

    MetalInfo({
        "name":"Ti 6-2-4-2",
        "picture":"",
        "Price":"8",
        "Density":"283",
        "Tensile strength":"146",
        "Thermal conductivity":"49.3",
        "Melting point":"3090",
        "Specific heat":"0.11",
    }),

    MetalInfo({
        "name":"TIMETAL 834",
        "picture":"",
        "Price":"???",
        "Density":"283",
        "Tensile strength":"153",
        "Thermal conductivity":"49",
        "Melting point":"3020",
        "Specific heat":"0.125",
    }),

    MetalInfo({
        "name":"Haynes Waspaloy",
        "picture":"",
        "Price":"8",
        "Density":"511",
        "Tensile strength":"194",
        "Thermal conductivity":"87.4 (392F)",
        "Melting point":"2430-2480",
        "Specific heat":"0.125",
    }),

    MetalInfo({
        "name":"Inconel 718",
        "picture":"",
        "Price":"9",
        "Density":"511",
        "Tensile strength":"160",
        "Thermal conductivity":"79.1",
        "Melting point":"2300-2437",
        "Specific heat":"0.104",
    }),

    MetalInfo({
        "name":"Arsenical Aluminum Brass C68700",
        "picture":"",
        "Price":"4.00 - 4.50",
        "Density":"520",
        "Tensile strength":"60",
        "Thermal conductivity":"58",
        "Melting point":"1710",
        "Specific heat":"0.09",
    }),

    MetalInfo({
        "name":"Invar 36",
        "picture":"",
        "Price":"18",
        "Density":"503",
        "Tensile strength":"90",
        "Thermal conductivity":"70.44",
        "Melting point":"2600",
        "Specific heat":"0.123",
    }),

    MetalInfo({
        "name":"Super Invar 32-5",
        "picture":"",
        "Price":"18",
        "Density":"508",
        "Tensile strength":"70",
        "Thermal conductivity":"72.6",
        "Melting point":"2600",
        "Specific heat":"0.12",
    }),

    MetalInfo({
        "name":"42 Alloy",
        "picture":"",
        "Price":"15",
        "Density":"506",
        "Tensile strength":"71",
        "Thermal conductivity":"72.9",
        "Melting point":"2600",
        "Specific heat":"0.12",
    }),

    MetalInfo({
        "name":"45 Alloy",
        "picture":"",
        "Price":"15",
        "Density":"509",
        "Tensile strength":"85-115",
        "Thermal conductivity":"75",
        "Melting point":"2600",
        "Specific heat":"0.12",
    }),

    MetalInfo({
        "name":"50 Alloy",
        "picture":"",
        "Price":"15",
        "Density":"512",
        "Tensile strength":"85-115",
        "Thermal conductivity":"94",
        "Melting point":"2600",
        "Specific heat":"0.12",
    }),

    MetalInfo({
        "name":"Kovar",
        "picture":"",
        "Price":"20",
        "Density":"522",
        "Tensile strength":"75",
        "Thermal conductivity":"120",
        "Melting point":"2640",
        "Specific heat":"0.105-0.155",
    }),

    MetalInfo({
        "name":"HyMu 80",
        "picture":"",
        "Price":"34",
        "Density":"546",
        "Tensile strength":"79",
        "Thermal conductivity":"240",
        "Melting point":"2649",
        "Specific heat":"0.118",
    }),

    MetalInfo({
        "name":"Bronze",
        "picture":"",
        "Price":"7",
        "Density":" 462 - 556",
        "Tensile strength":"37",
        "Thermal conductivity":"180",
        "Melting point":"1675",
        "Specific heat":"0.104",
    }),

    MetalInfo({
        "name":"Aluminum Bronze C95400",
        "picture":"",
        "Price":"5",
        "Density":" 481 - 543",
        "Tensile strength":"75",
        "Thermal conductivity":"528",
        "Melting point":"1881 - 1900",
        "Specific heat":"0.09",
    }),

    MetalInfo({
        "name":"Copper Nickel 90/10",
        "picture":"",
        "Price":"4.5",
        "Density":"556",
        "Tensile strength":"44-60",
        "Thermal conductivity":"277",
        "Melting point":"2012 - 2093",
        "Specific heat":"0.09",
    }),

    MetalInfo({
        "name":"Copper Nickel 70/30 (C71500)",
        "picture":"",
        "Price":"4.5",
        "Density":"559",
        "Tensile strength":"25-43",
        "Thermal conductivity":"201",
        "Melting point":"2138 - 2264",
        "Specific heat":"0.09",
    }),

    MetalInfo({
        "name":"Copper-Nickel Alloy",
        "picture":"",
        "Price":"4.5",
        "Density":"551",
        "Tensile strength":"56-160",
        "Thermal conductivity":"121-204",
        "Melting point":"1170-1350",
        "Specific heat":"0.12",
    }),

    MetalInfo({
        "name":"Al 2xxx",
        "picture":"",
        "Price":"1",
        "Density":"161-180",
        "Tensile strength":"25-97.2",
        "Thermal conductivity":"583-1390",
        "Melting point":"935-1240",
        "Specific heat":"0.2-0.221",
    }),

    MetalInfo({
        "name":"Cobalt Alloys",
        "picture":"",
        "Price":"25",
        "Density":"430-743",
        "Tensile strength":"11.6-368",
        "Thermal conductivity":"58.3-1390",
        "Melting point":"2000-2820",
        "Specific heat":"0.0837-0.12",
    }),

    MetalInfo({
        "name":"Copper 101/102",
        "picture":"",
        "Price":"3.86",
        "Density":"558",
        "Tensile strength":"32-66",
        "Thermal conductivity":"226",
        "Melting point":"1981",
        "Specific heat":"0.092",
    }),

    MetalInfo({
        "name":"Phosphor Bronze C52400",
        "picture":"",
        "Price":"4.72",
        "Density":"548",
        "Tensile strength":"66-147",
        "Thermal conductivity":"348",
        "Melting point":"1550-1830",
        "Specific heat":"0.09",
    }),

    MetalInfo({
        "name":"Nickel-Silver (Alloy 770)",
        "picture":"",
        "Price":"5.76",
        "Density":"543",
        "Tensile strength":"61-120",
        "Thermal conductivity":"204",
        "Melting point":"1930",
        "Specific heat":"0.09",
    }),

    MetalInfo({
        "name":"Molybdenum",
        "picture":"",
        "Price":"11.7",
        "Density":"638",
        "Tensile strength":"120-200",
        "Thermal conductivity":"985",
        "Melting point":"4730",
        "Specific heat":"0.0621",
    }),

    MetalInfo({
        "name":"Tungsten",
        "picture":"",
        "Price":"31.4",
        "Density":"1202",
        "Tensile strength":"100-500",
        "Thermal conductivity":"813-1133",
        "Melting point":"6170",
        "Specific heat":"0.032",
    }),

    MetalInfo({
        "name":"Tantalum",
        "picture":"",
        "Price":"400",
        "Density":"1042",
        "Tensile strength":"41-120",
        "Thermal conductivity":"377",
        "Melting point":"5162",
        "Specific heat":"0.036",
    }),

    MetalInfo({
        "name":"Nichrome",
        "picture":"",
        "Price":"13.5",
        "Density":"524",
        "Tensile strength":"70-115",
        "Thermal conductivity":"78.3",
        "Melting point":"2550",
        "Specific heat":"0.107",
    }),

    MetalInfo({
        "name":"Copper",
        "picture":"",
        "Price":"3",
        "Density":"557.5",
        "Tensile strength":"30.3-50",
        "Thermal conductivity":"2761",
        "Melting point":"1985",
        "Specific heat":"0.092",
    }),

    MetalInfo({
        "name":"Low-Alloy Steel",
        "picture":"",
        "Price":"0.5",
        "Density":"468-504",
        "Tensile strength":"26.1-396",
        "Thermal conductivity":"222-435",
        "Melting point":"",
        "Specific heat":"0.081-0.120",
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
    metal_name = ttk.Label(frame, text=metal_info.info["name"])
    metal_name.grid(column=2, row=1)
    metal_price = ttk.Label(frame, text=metal_info.info["Price"])
    metal_price.grid(column=2, row=2)
    metal_density = ttk.Label(frame, text=metal_info.info["Density"])
    metal_density.grid(column=2, row=3)
    metal_tensile = ttk.Label(frame, text=metal_info.info["Tensile strength"])
    metal_tensile.grid(column=2, row=4)
    metal_thermal = ttk.Label(frame, text=metal_info.info["Thermal conductivity"])
    metal_thermal.grid(column=2, row=5)
    metal_melting = ttk.Label(frame, text=metal_info.info["Melting point"])
    metal_melting.grid(column=2, row=6)
    metal_specific = ttk.Label(frame, text=metal_info.info["Specific heat"])
    metal_specific.grid(column=2, row=7)
    return frame
        
def main():

    root = Tk()

    root.title("Corrosion Decisions")
    
    frame = ttk.Frame(root, padding="3 3 3 3")
    frame.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    info_into_frame(frame, metal_infos[0])

    root.mainloop()
    
# misc. API examples: 
# blue1 = Node("Whatever end")
# red1 = Node("Whatever i say", blue1, child2)
# Node.branch(childValue)
# Tree(rootNode)

if __name__=="__main__":
   main()
