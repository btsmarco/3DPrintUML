from math import floor

class Card:
    # A card represents a class in a UML diagram, it takes in 2 params
    # 1. name: string, 2. coordinates: tuple(int, int) 3. width: int
    def __init__(self,name,coordinates,width):
       self.name = name
       #TODO check if tuple too
       if (len(coordinates) == 2):
            self.x = float(coordinates[0])
            self.y = float(coordinates[1])
       else:
           print("Error, coordinates must be a tuple of x an y coordinates")
           exit(1)

       self.width = width
       self.position = [0,0,0.5]  # [X,Y,Z]

    def GetName(self):
        return self.name

    def GetCoordinates(self):
        return (self.x,self.y)

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetWidth(self):
        return self.width

    def SetPosition(self, OldW, OldH, NewW, NewH):
        # Normalize coordinates to new value
        BoolResult = False

        if( NewW < 20 or NewH < 10 ):
            BoolResult = False
        elif( OldW < int(self.x) or OldH < int(self.y) ):
            BoolResult = False
        else:
            # The first part of the calculation we normalize the value
            # to fit in the new slate size then we take away the decimals
            # then we subtract it from (New/2) to make it relative to center
            # not the upper left corner as it was

            X = floor((self.x/OldW)* NewW) - (NewW/2)
            Y = floor((self.y/OldH)* NewH) - (NewH/2)

            self.position[0] = X
            self.position[1] = Y
            BoolResult = True

        return BoolResult

    def GetPosition(self):
        return self.position

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

