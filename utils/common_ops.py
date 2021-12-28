import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/AutomationPythonHackathon/AaConfig_file/config.xml').getroot()
    return root.find(".//" + node_name).text


