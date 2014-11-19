from models import Card
from models import Line

class Test_Card:
    # This class is to test the class cards
    def __init__(self):
        # Create multiple cards to be tested in the bottom
        self.card1 = Card('card1',(1,1))

    def Test_GetName(self):
        assert(self.card1.GetName() == 'card1')

    def Test_GetCoordinates(self):
        assert(self.card1.GetCoordinates() == (1,1))

    def Test_SetPosition(self):
        pass

    def Test_GetPosition(self):
        assert(self.card1.GetPosition() == (0,0))

    def Test_Plot(self):
        pass


class Test_Line:
    # This class tests the line class

    def __init__(self):
        # Create multiple lines (and cards) with different senarios
        pass

    def Test_GetCoordinates(self):
        pass

    def Test_SetPosition(self):
        pass

    def Test_GetPosition(self):
        pass

    def Test_Plot(self):
        pass

