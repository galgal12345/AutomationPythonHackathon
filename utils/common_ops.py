import xml.etree.ElementTree as ET


def get_browser(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/AutomationPythonHackathon/AaConfig_file/config.xml').getroot()
    return root.find(".//" + node_name).text


def get_driver(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/AutomationPythonHackathon/AaConfig_file/config.xml').getroot()
    return root.find(".//" + node_name).text
