class Card:
    # A card represents a class in a UML diagram, it takes in 2 params
    # 1. name: string, 2. coordinates: tuple(int, int)
    def __init__(self,name,coordinates):
       self.name = name
       #TODO check if tuple too
       if (len(coordinates) == 2):
            self.x = coordinates[0]
            self.y = coordinates[1]
       else:
           print("Error, coordinates must be a tuple of x an y coordinates")
           exit(1)

       self.position = (0,0)

    def GetName(self):
        return self.name

    def GetCoordinates(self):
        return (self.x,self.y)

    def SetPosition(self,value):
        #Set to position relative on collada
        pass

    def GetPosition(self):
        return self.position

    def Plot(self):
        #Return as collada node, ready to be put in file
        pass


class Line:
    # A line represents an assosiation or inheritance in a UML diagram,
    # It takes 4 params, 1. FromCard: Card, 2. ToCard: Card, 3. Type: enum/string
    def __init__(self,FromCard, ToCard,Type):
        self.FromCard = FromCard
        self.ToCard = ToCard
        self.Type = Type
        self.position = (0,0)

    def GetCoordinates(self):
        #Get the coordinates from relative cards
        pass

    def SetPosition(self,value):
        #Set to position relative on collada
        pass

    def GetPosition(self):
        return self.position

    def Plot(self):
        #Return as collada node, ready to be put in file
        pass




