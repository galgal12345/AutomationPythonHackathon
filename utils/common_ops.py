import os
import xml.etree.ElementTree as ET


def get_data(node_name):
    print(os.path.dirname(os.path.abspath(__file__)))
    root = ET.parse(r'..\AaConfig_file\config.xml').getroot()
    return root.find(".//" + node_name).text

