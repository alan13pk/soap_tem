import xml.etree.ElementTree as ET
tree = ET.parse('MovieAll_SPN.xml')
root = tree.getroot()
time_tag = ET.Element('time')
time_tag.text = "100"
resolution_tag = ET.Element('resolution')
resolution_tag.text = "HD"
for movie in root.findall('movie'):
	movie.append(time_tag)
	movie.append(resolution_tag)
tree.write('MovieAll_SPN.xml')