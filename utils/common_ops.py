import xml.etree.ElementTree as ET

def get_browser(node_name):
    root = ET.parse('C:\Automation\mimi_hackathon\AaConfig_file\config.xml').getroot()
    return root.find(".//" + node_name).text


def get_driver(node_name):
    root = ET.parse('C:\Automation\mimi_hackathon\AaConfig_file\config.xml').getroot()
    return root.find(".//" + node_name).text

def get_data(node_name):
    root = ET.parse('C:\Automation\mimi_hackathon\AaConfig_file\config.xml').getroot()
    return root.find(".//" + node_name).text