class Card:
    # A card represents a class in a UML diagram, it takes in 2 params
    # 1. name: string, 2. coordinates: tuple(int, int) 3. width: int
    def __init__(self,name,coordinates,width):
       self.name = name
       #TODO check if tuple too
       if (len(coordinates) == 2):
            self.x = coordinates[0]
            self.y = coordinates[1]
       else:
           print("Error, coordinates must be a tuple of x an y coordinates")
           exit(1)

       self.width = width
       self.position = (0,0)

    def GetName(self):
        return self.name

    def GetCoordinates(self):
        return (self.x,self.y)

    def GetWidth(self):
        return self.width

    def SetPosition(self,value):
        #Set to position relative on collada
        pass

    def GetPosition(self):
        return self.position

    def Plot(self):
        #Return as collada node, ready to be put in file
        node ='''<geometry id="Cube_001-mesh" name="Cube.001">
      <mesh>
        <source id="Cube_001-mesh-positions">
          <float_array id="Cube_001-mesh-positions-array" count="24">-1 -1 -1 -1 1 -1 1 1 -1 1 -1 -1 -1 -1 1 -1 1 1 1 1 1 1 -1 1</float_array>
          <technique_common>
            <accessor source="#Cube_001-mesh-positions-array" count="8" stride="3">
              <param name="X" type="float"/>
              <param name="Y" type="float"/>
              <param name="Z" type="float"/>
            </accessor>
          </technique_common>
        </source>
        <source id="Cube_001-mesh-normals">
          <float_array id="Cube_001-mesh-normals-array" count="36">-1 0 0 0 1 0 1 0 0 0 -1 0 0 0 -1 0 0 1 -1 0 0 0 1 0 1 0 0 0 -1 0 0 0 -1 0 0 1</float_array>
          <technique_common>
            <accessor source="#Cube_001-mesh-normals-array" count="12" stride="3">
              <param name="X" type="float"/>
              <param name="Y" type="float"/>
              <param name="Z" type="float"/>
            </accessor>
          </technique_common>
        </source>
        <vertices id="Cube_001-mesh-vertices">
          <input semantic="POSITION" source="#Cube_001-mesh-positions"/>
        </vertices>
        <polylist count="12">
          <input semantic="VERTEX" source="#Cube_001-mesh-vertices" offset="0"/>
          <input semantic="NORMAL" source="#Cube_001-mesh-normals" offset="1"/>
          <vcount>3 3 3 3 3 3 3 3 3 3 3 3 </vcount>
          <p>4 0 5 0 1 0 5 1 6 1 2 1 6 2 7 2 3 2 7 3 4 3 0 3 0 4 1 4 2 4 7 5 6 5 5 5 0 6 4 6 1 6 1 7 5 7 2 7 2 8 6 8 3 8 3 9 7 9 0 9 3 10 0 10 2 10 4 11 7 11 5 11</p>
        </polylist>
      </mesh>
    </geometry>'''
        return node

class Line:
    # A line represents an assosiation or inheritance in a UML diagram,
    # It takes 4 params, 1. linetype: string, 2. coordinates: tuple (x,y)
    # 3. width: int
    def __init__(self,linetype, coordinates, width):
        #self.FromCard = FromCard
        #self.ToCard = ToCard
        self.linetype = linetype
        if (len(coordinates) == 2):
            self.x = coordinates[0]
            self.y = coordinates[1]
        else:
           print("Error, coordinates must be a tuple of x an y coordinates")
           exit(1)

        self.width = width
        self.position = (0,0)

    def GetType(self):
        return self.linetype

    def GetCoordinates(self):
        #Get the coordinates from relative cards
        return (self.x, self.y)

    def GetWidth(self):
        return self.width

    def SetPosition(self,value):
        #Set to position relative on collada
        pass

    def GetPosition(self):
        return self.position

    def Plot(self):
        #Return as collada node, ready to be put in file
        node ='''<geometry id="Cube_001-mesh" name="Cube.001">
      <mesh>
        <source id="Cube_001-mesh-positions">
          <float_array id="Cube_001-mesh-positions-array" count="24">-1 -1 -1 -1 1 -1 1 1 -1 1 -1 -1 -1 -1 1 -1 1 1 1 1 1 1 -1 1</float_array>
          <technique_common>
            <accessor source="#Cube_001-mesh-positions-array" count="8" stride="3">
              <param name="X" type="float"/>
              <param name="Y" type="float"/>
              <param name="Z" type="float"/>
            </accessor>
          </technique_common>
        </source>
        <source id="Cube_001-mesh-normals">
          <float_array id="Cube_001-mesh-normals-array" count="36">-1 0 0 0 1 0 1 0 0 0 -1 0 0 0 -1 0 0 1 -1 0 0 0 1 0 1 0 0 0 -1 0 0 0 -1 0 0 1</float_array>
          <technique_common>
            <accessor source="#Cube_001-mesh-normals-array" count="12" stride="3">
              <param name="X" type="float"/>
              <param name="Y" type="float"/>
              <param name="Z" type="float"/>
            </accessor>
          </technique_common>
        </source>
        <vertices id="Cube_001-mesh-vertices">
          <input semantic="POSITION" source="#Cube_001-mesh-positions"/>
        </vertices>
        <polylist count="12">
          <input semantic="VERTEX" source="#Cube_001-mesh-vertices" offset="0"/>
          <input semantic="NORMAL" source="#Cube_001-mesh-normals" offset="1"/>
          <vcount>3 3 3 3 3 3 3 3 3 3 3 3 </vcount>
          <p>4 0 5 0 1 0 5 1 6 1 2 1 6 2 7 2 3 2 7 3 4 3 0 3 0 4 1 4 2 4 7 5 6 5 5 5 0 6 4 6 1 6 1 7 5 7 2 7 2 8 6 8 3 8 3 9 7 9 0 9 3 10 0 10 2 10 4 11 7 11 5 11</p>
        </polylist>
      </mesh>
    </geometry>'''
        return node



