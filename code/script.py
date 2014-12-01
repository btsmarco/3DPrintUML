# UML3D project - CSE 435 MSU honors project
# Author: Marco Botros
# Objective: Convert UML diagrams (XML format) to Collada for 3D printing (also XML)

import xml.etree.ElementTree as ET
from solid import *
from models import Card,Line
from factory import assembly

# Variables
# TODO turn to dictionary if needed
Cards = []
Lines = []

# Import the UML XML file
UMLFilePath = '../UML/project.xml'

UMLFile = open(UMLFilePath,'r')

# Extract the required tags from the XML
tree = ET.parse(UMLFile)

# getroot() and find() both return an 'Element' which
# in turn has attributes, children...etc
root = tree.getroot()
Diagrams = root.find('Diagrams')
ClassDiagram = Diagrams.find('ClassDiagram')
Shapes = ClassDiagram.find('Shapes')
Connectors = ClassDiagram.find('Connectors')

# Use the classes defined in the file models.py and extract information
# from the xml nodes to create instances of those classes, then store them
for shape in Shapes.findall('Class'):
    c = Card(shape.get('Name'),(shape.get('X'),shape.get('Y')), shape.get('Width'))
    Cards.append(c)

for connector in Connectors:
    l = Line(connector.tag,(connector.get('X'),connector.get('Y')),connector.get('Width'))
    Lines.append(l)

#Just to check

for card in Cards:
    print 'Card name is %s'%(card.GetName())
    coordinates = [card.GetX(),card.GetY()]
    print 'Card coordinates are (%s,%s)'%(coordinates[0],coordinates[1])
    print 'Card width is %s'%(card.GetWidth())
    print ''

for line in Lines:
    print 'Line Type is %s'%(line.GetType())
    coordinates = [line.GetX(),line.GetY()]
    print 'Line coordinates are (%s,%s)'%(coordinates[0],coordinates[1])
    print 'Line width is %s'%(line.GetWidth())
    print ''

#-----------------------------

# Find the largest X and Y value in the cards to
# find out the approximate size of the old diagram

BufValue = 15
SampleHeight = 150
# These functions are given to the max builtin function
def Xcoord(c):
    return c.GetX()

def Ycoord(c):
    return c.GetY()

MaxX = max(Cards, key=Xcoord)
MaxY = max(Cards, key=Ycoord)

# TODO do something about the 200 value
OldWidth = MaxX.GetX() + BufValue + 200
OldHeight = MaxY.GetY() + SampleHeight + BufValue

# Values of the 3D slate base
SlatX = 100
SlatY = 60

for card in Cards:
    b = card.SetPosition(OldWidth, OldHeight, SlatX, SlatY)
    k = card.SetWidth(OldWidth, SlatX)

    # TODO delete in production
    assert(b)
    assert(k)

    P = card.GetPosition()
    W = card.GetWidth()
    print 'New Card Position [%f,%f,%f] and width %f'%(P[0],P[1],P[2],W)

for line in Lines:
    o = line.SetPosition(OldWidth, OldHeight, SlatX, SlatY)
    k = line.SetWidth(OldWidth, SlatX)

    # TODO delete in production
    assert(o)
    assert(k)

Slat = assembly(SlatX,SlatY,Cards,Lines)

SEGMENTS = 48
scad_render_to_file( Slat, file_header='$fn = %s;'%SEGMENTS, include_orig_code=True)
