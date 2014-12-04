from math import floor

class Card:
    # A card represents a class in a UML diagram, it takes in 2 params
    # 1. name: string, 2. coordinates: tuple(int, int) 3. width: int
    def __init__(self,name,coordinates,width,height):
       self.name = name
       #TODO check if tuple too
       if (len(coordinates) == 2):
            self.x = float(coordinates[0])
            self.y = float(coordinates[1])
       else:
           print("Error, coordinates must be a tuple of x an y coordinates")
           exit(1)

       self.width = float(width)
       self.height = float(height)
       self.position = [0,0,1]  # [X,Y,Z]

    def GetName(self):
        return self.name

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetWidth(self):
        return self.width

    def GetHeight(self):
        return self.height

    # Normalize takes input var:str ('width' or height'),
    # OldV:int (UML diagram Value), NewV:int (3D slate size Value)
    #
    # The first part of the calculation we normalize the value
    # to fit in the new slate size then we take away the decimals
    def Normalize(self,Var,OldV, NewV):
        BoolResult = False

        if( NewV < 20 ):
            BoolResult = False

        if(Var == 'width'):
            if( OldV < self.x):
                BoolResult = False
            else:
                #self.width = floor((self.width/OldV)* NewV)
                self.width = round((self.width/OldV)* NewV,2)
                BoolResult = True

        elif( Var == 'height'):
            if( OldV < self.y):
                BoolResult = False
            else:
                #self.width = floor((self.width/OldV)* NewV)
                self.height = round((self.height/OldV)* NewV,2)
                BoolResult = True
        else:
            BoolResult = False

        return BoolResult

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

#            X = floor((self.x/OldW)* NewW) - (NewW/2)
#            Y = floor((self.y/OldH)* NewH) - (NewH/2)

            X = round( ((self.x/OldW)* NewW) - (NewW/2),2)
            Y = round( ((self.y/OldH)* NewH) - (NewH/2),2)


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

        self.linetype = linetype
        if (len(coordinates) == 2):
            self.x = float(coordinates[0])
            self.y = float(coordinates[1])

        else:
           print("Error, coordinates must be a tuple of x an y coordinates")
           exit(1)

        self.width = float(width)
        self.position = [0,0,1]

    def GetType(self):
        return self.linetype

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetWidth(self):
        return self.width

    def SetWidth(self,OldW, NewW):
        BoolResult = False

        if( NewW < 20 ):
            BoolResult = False
        elif( OldW < int(self.x)):
            BoolResult = False
        else:
            # The first part of the calculation we normalize the value
            # to fit in the new slate size then we take away the decimals
            # then we subtract it from (New/2) to make it relative to center
            # not the upper left corner as it was

            #self.width = floor((self.width/OldW)* NewW)
            self.width = round((self.width/OldW)* NewW,2)

            BoolResult = True

        return BoolResult


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

           #X = floor((self.x/OldW)* NewW) - (NewW/2)
           #Y = floor((self.y/OldH)* NewH) - (NewH/2)
            X = round( ((self.x/OldW)* NewW) - (NewW/2),2)
            Y = round( ((self.y/OldH)* NewH) - (NewH/2),2)


            self.position[0] = X
            self.position[1] = Y
            BoolResult = True

        return BoolResult

    def GetPosition(self):
        return self.position

