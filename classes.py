#############################################################
# The BingoCard class is used to represent a card as data. 
# Each card belongs to a page, which has an ID. There are 6
# cards per page, and each card has a coordinate (1-6). Each 
# card has 3 booleans indicating whether they have at least 
# one line completed, at least two lines completed, or the 
# whole card completed.
#############################################################
class BingoCard:
    def __init__(self, id: int, coordinate: int, single: bool, double: bool, full: bool):
        self.pageID = id
        self.pageCoordinate = coordinate
        self.hasSingleWon = single
        self.hasDoubleWon = double
        self.hasFullWon = full