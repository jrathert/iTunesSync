import lxml.etree as etree
import xml.etree.ElementTree as ET
import re
from urllib.parse import unquote

#xmlFile = 'sample.xml'
xmlFile = 'iTunes Music Library.xml'

def parse():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)


def listArtists():
    doc = etree.parse(xmlFile)
    artists_elems = doc.xpath(".//dict/dict/dict/key[text()='Artist']")
    for elem in artists_elems:
        a_elem = elem.getnext()
        print(a_elem.text)
    print ("Done")


def listAlbums():
    doc = etree.parse(xmlFile)
    all_locs = doc.xpath(".//dict/dict/dict/key[text()='Location']")

    album_set = set()

    my_re = r"(?<=Media/Music/)([^/]*)/([^/]*)"

    for elem in all_locs:
        location = unquote(elem.getnext().text)
        m = re.search(my_re, location)
        if m is not None:
            #print(m.group(0))
            alb = m.group(1) + " - " + m.group(2)
            #print(alb)
            album_set.add(alb)

    for alb in sorted(album_set):
        print(alb)

    print ("Done - {} albums".format(len(album_set)))


def listKey():
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    allKeys = root.findall(".//key")
    num = 0
    for elem in allKeys:
        print(elem, elem.text)
        num += 1
    print(num)