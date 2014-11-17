# UML3D project - CSE 435 MSU honors project
# Author: Marco Botros
# Objective: Convert UML diagrams (XML format) to Collada for 3D printing (also XML)

import xml.etree.ElementTree as ET
from models import Card,Line

# Variables
# TODO turn to dictionary if needed
Cards = []
Lines = []

# Import the UML XML file
# Import Collada template
UMLFilePath = '../UML/project.xml'
ColladaFilePath = '../blender/plain.dae'
OutputFilePath = '../Output/diagram.dae'

UMLFile = open(UMLFilePath,'r')
ColladaFile = open(ColladaFilePath,'r')
OutputFile = open( OutputFilePath, 'w')

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

#for card in Cards:
#    print 'Card name is %s'%(card.GetName())
#    coordinates = card.GetCoordinates()
#    print 'Card coordinates are (%s,%s)'%(coordinates[0],coordinates[1])
#    print 'Card width is %s'%(card.GetWidth())
#    print line.Plot()
#    print ''

#for line in Lines:
#    print 'Line Type is %s'%(line.GetType())
#    coordinates = line.GetCoordinates()
#    print 'Line coordinates are (%s,%s)'%(coordinates[0],coordinates[1])
#    print 'Line width is %s'%(line.GetWidth())
#    print line.Plot()
#    print ''


# Make node for each box in the UML and line respectively into Collada



