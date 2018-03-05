import xml.etree.ElementTree as ET

#xmlFile = 'sample.xml'
xmlFile = 'iTunes Music Library.xml'

def parse():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)


def listArtists():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    allKeys = root.findtext("Artist")
    num = 0
    for elem in allKeys:
        print(elem, elem.text)
        num += 1
    print(num)


def listKey():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    allKeys = root.findall(".//key")
    num = 0
    for elem in allKeys:
        print(elem, elem.text)
        num += 1
    print(num)