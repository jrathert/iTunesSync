import xml.etree.ElementTree as ET

xmlFile = 'sample.xml'
xmlFile = 'iTunes Music Library.xml'

def parse():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)


def listArtists():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for child in root.findall("[key='Artist']"):
        print(child.tag)