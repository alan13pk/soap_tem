import xml.etree.ElementTree as ET
tree = ET.parse('Movie.xml')
root = tree.getroot()
time_tag = ET.Element('time')
time_tag.text = "100"
resolution_tag = ET.Element('resolution')
resolution_tag.text = "HD"