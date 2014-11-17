# UML3D project - CSE 435 MSU honors project
# Author: Marco Botros
# Objective: Convert UML diagrams (XML format) to Collada for 3D printing (also XML)

import xml.etree.ElementTree as ET

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

root = tree.getroot()
Diagrams = root.find('Diagrams')
ClassDiagram = Diagrams.find('ClassDiagram')
Shapes = ClassDiagram.find('Shapes')

for i in Shapes.findall('Class'):
    print i.get('Name')

# Make node for each box in the UML and line respectively into Collada



