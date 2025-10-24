from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position

    def get_position(self):
        return self.position

    @abstractmethod
    def move(self, position, new_position):
        pass
    @abstractmethod
    def get_symbol(self):
        pass


class Pawn(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)

    def move(self, position, new_position):
        if (self.colour == "white" and new_position == [(position[0]+1),position[1]]) or (self.colour == "black" and new_position == [(position[0]-1),position[1]]):
            self.position = new_position
        elif (self.colour == "white" and (new_position == [(position[0]+1),(position[1]+1)]) or (new_position == [(position[0]+1),(position[1]-1)])) or (self.colour == "black" and (new_position == [(position[0]-1),(position[1]+1)]) or (new_position == [(position[0]-1),(position[1]-1)])):
            self.position = new_position

    def get_symbol(self):
        return '♙' if self.colour == 'black' else '♟'
    
class Rook(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)

    def move(self, position, new_position):
        if (position[0] == new_position[0]) or (position[1] == new_position[1]):
            self.position = new_position

    def get_symbol(self):
        return '♖' if self.colour == 'black' else '♜'
    
class Knight(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)

    def move(self, position, new_position):
        if (new_position == [(position[0]+2),(position[1]+1)]) or (new_position == [(position[0]+2),(position[1]-1)]) or (new_position == [(position[0]-2),(position[1]+1)]) or (new_position == [(position[0]-2),(position[1]-1)]) or (new_position == [(position[0]+1),(position[1]+2)]) or (new_position == [(position[0]+1),(position[1]-2)]) or (new_position == [(position[0]-1),(position[1]+2)]) or (new_position == [(position[0]-1),(position[1]-2)]):
            self.position = new_position
    
    def get_symbol(self):
        return '♘' if self.colour == 'black' else '♞'
    
class Bishop(Piece):
    def __init__(self,colour,position):
        super().__init__(colour,position)

    def move(self,position,new_position):
        for i in range(8):
            if (new_position == [(position[0]+i),(position[1]+i)]) or (new_position == [(position[0]-i),(position[1]+i)]) or (new_position == [(position[0]+i),(position[1]-i)]) or (new_position == [(position[0]-i),(position[1]-i)]):
                self.position = new_position

    def get_symbol(self):
        return '♗' if self.colour == 'black' else '♝'
    
class Queen(Piece):
    def __init__(self,colour,position):
        super().__init__(colour,position)

    def move(self,position,new_position):
        for i in range(8):
            if (new_position == [(position[0]+i),(position[1]+i)]) or (new_position == [(position[0]-i),(position[1]+i)]) or (new_position == [(position[0]+i),(position[1]-i)]) or (new_position == [(position[0]-i),(position[1]-i)]):
                self.position = new_position
        if (position[0] == new_position[0]) or (position[1] == new_position[1]):
            self.position = new_position

    def get_symbol(self):
        return '♕' if self.colour == 'black' else '♛'

class King(Piece):
    def __init__(self,colour,position):
        super().__init__(colour,position)

    def move(self,position,new_position):
        if (new_position == [(position[0]+1),(position[1])]) or (new_position == [(position[0]-1),(position[1])]) or (new_position == [(position[0]),(position[1]+1)]) or (new_position == [(position[0]),(position[1]-1)]) or (new_position == [(position[0]+1),(position[1]+1)]) or (new_position == [(position[0]+1),(position[1]-1)]) or (new_position == [(position[0]-1),(position[1]+1)]) or (new_position == [(position[0]-1),(position[1]-1)]):
            self.position = new_position
            return
        print("Invalid move for King")

    def get_symbol(self):
        return '♔' if self.colour == 'black' else '♚'