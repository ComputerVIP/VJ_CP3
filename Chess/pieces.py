from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, colour, position, type):
        self.colour = colour
        self.position = position
        self.type = type

    def get_position(self):
        return self.position

    @abstractmethod
    def move(self, position, new_position):
        pass
    @abstractmethod
    def get_symbol(self):
        pass

class ChessGame():
    def __init__(self, white, black):
        self.white = white
        self.black = black

    def move_piece(self, new_pos, white, black):
        if self.type == "pawn":
            Pawn.move(self, self.position, new_pos, white, black)
        elif self.type == "knight":
            Knight.move(self, self.position, new_pos, white, black)
        elif self.type == "rook":
            Rook.move(self, self.position, new_pos, white, black)
        elif self.type == "bishop":
            Bishop.move(self, self.position, new_pos, white, black)
        elif self.type == "king":
            King.move(self, self.position, new_pos, white, black)
        elif self.type == "queen":
            Queen.move(self, self.position, new_pos, white, black)

    def piece_pos(self):
        print(f"{self.type} at {self.position}")

    def pieces_left(white, black, colour):
        if colour == "white":
            for i in white:
                print(f"{i.type.capitalize()} at: {i.position}")
        elif colour == "black":
            for i in black:
                print(f"{i.type.capitalize()} at: {i.position}")
    
    def remove_piece(self, white, black):
        if self.colour == "white":
            print(f"Removing {self.type} at {self.position}")
            white.remove(self)

        elif self.colour == "black":
            black.remove(self)
        return
    
    def check_space(self, black, white, new_pos):
        print("In space")
        if self.colour == "white":
            for i in black:
                print(i, i.colour, i.position)
                print(self, self.colour, new_pos)
                if i.position == new_pos:
                    print(f"You have captured a {i.colour} {i.type} at {i.position}")
                    black.remove(i)
                    return True
        elif self.colour == "black":
            for i in white:
                if i.position == new_pos:
                    print(f"You have captured a {i.colour} {i.type} at {i.position}")
                    white.remove(i)
                    return True
        return False
    
    def check_pos(position, new_pos):
        print("In pos")
        if (1 < position[0] > 8) or (1 < position[1] > 8):
            return False
        else: return True

    def find_piece(white, black):
        pie = list(map(int, input("What's the row and column of the piece, seperated by a space?\n\n    ").split()))
        for i in white:
            if i.position == pie:
                print(f"Your piece is {i.colour}, a {i.type} and is at {i.position}")
                ch = i
        for i in black:
            if i.position == pie:
                print(f"Your piece is {i.colour}, a {i.type} and is at {i.position}")
                ch = i
        if ch:
            if int(input("1 if this is correct:\n\n    ")) == 1:
                return ch
    
    def show_board(white, black, display_base):
        temp = display_base
        f = 0
        print("In")
        for i in white:
            print(i)
            if i.position[0] > 1:
                for a in temp:
                    f += 1
                    if f == (i.position[0]*15 + i.position[1]*2 +1):
                        print(i.position[0]*15 + i.position[1]*2 +1)
                        print(a)
                    
            elif i.position[0] == 1:
                for a in temp:
                    f += 1
                    if f == (i.position[0]*15 + i.position[1]*2):
                        print("Row 1")
                        print(i.position[0]*15 + i.position[1]*2)
                        print(a)



class Pawn(Piece):
    def __init__(self, colour, position, type):
        super().__init__(colour, position, type)

    def move(self, position, new_position, white, black):
        if (self.colour == "white" and new_position == [(position[0]+1),position[1]]) or (self.colour == "black" and new_position == [(position[0]-1),position[1]]):
            if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                self.position = new_position
                print("Moved!, pos:", self.position)
                return
        elif (self.colour == "white" and (new_position == [(position[0]+1),(position[1]+1)]) or (new_position == [(position[0]+1),(position[1]-1)])) or (self.colour == "black" and (new_position == [(position[0]-1),(position[1]+1)]) or (new_position == [(position[0]-1),(position[1]-1)])):
            if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                self.position = new_position
                print("Moved!, pos:", self.position)
                return
        print("Invalid move for pawn!")
        return

    def get_symbol(self):
        return '♙' if self.colour == 'black' else '♟'
    
class Rook(Piece):
    def __init__(self, colour, position, type):
        super().__init__(colour, position, type)

    def move(self, position, new_position, white, black):
        if (position[0] == new_position[0]) or (position[1] == new_position[1]):
            if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                self.position = new_position
                print("Moved!, pos:", self.position)
                return
        print("Invalid move for rook!")
        return

    def get_symbol(self):
        return '♖' if self.colour == 'black' else '♜'
    
class Knight(Piece):
    def __init__(self, colour, position, type):
        super().__init__(colour, position, type)

    def move(self, position, new_position, white, black):
        if (new_position == [(position[0]+2),(position[1]+1)]) or (new_position == [(position[0]+2),(position[1]-1)]) or (new_position == [(position[0]-2),(position[1]+1)]) or (new_position == [(position[0]-2),(position[1]-1)]) or (new_position == [(position[0]+1),(position[1]+2)]) or (new_position == [(position[0]+1),(position[1]-2)]) or (new_position == [(position[0]-1),(position[1]+2)]) or (new_position == [(position[0]-1),(position[1]-2)]):
            if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                self.position = new_position
                print("Moved!, pos:", self.position)
                return
        print("Invalid move for knight!")
        return
    
    def get_symbol(self):
        return '♘' if self.colour == 'black' else '♞'
    
class Bishop(Piece):
    def __init__(self,colour,position, type):
        super().__init__(colour,position, type)

    def move(self,position,new_position, white, black):
        for i in range(8):
            if (new_position == [(position[0]+i),(position[1]+i)]) or (new_position == [(position[0]-i),(position[1]+i)]) or (new_position == [(position[0]+i),(position[1]-i)]) or (new_position == [(position[0]-i),(position[1]-i)]):
                if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                    self.position = new_position
                    print("Moved!, pos:", self.position)
                    return
            print("Invalid move for bishop!")
            return

    def get_symbol(self):
        return '♗' if self.colour == 'black' else '♝'
    
class Queen(Piece):
    def __init__(self,colour,position, type):
        super().__init__(colour,position, type)

    def move(self,position,new_position, white, black):
        for i in range(8):
            if (new_position == [(position[0]+i),(position[1]+i)]) or (new_position == [(position[0]-i),(position[1]+i)]) or (new_position == [(position[0]+i),(position[1]-i)]) or (new_position == [(position[0]-i),(position[1]-i)]):
                if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                    self.position = new_position
                    print("Moved!, pos:", self.position)
                    return
        if (position[0] == new_position[0]) or (position[1] == new_position[1]):
            if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                self.position = new_position
                print("Moved!, pos:", self.position)
                return
        print("Invalid move for queen!")
        return

    def get_symbol(self):
        return '♕' if self.colour == 'black' else '♛'

class King(Piece):
    def __init__(self,colour,position, type):
        super().__init__(colour,position, type)

    def move(self,position,new_position, white, black):
        if (new_position == [(position[0]+1),(position[1])]) or (new_position == [(position[0]-1),(position[1])]) or (new_position == [(position[0]),(position[1]+1)]) or (new_position == [(position[0]),(position[1]-1)]) or (new_position == [(position[0]+1),(position[1]+1)]) or (new_position == [(position[0]+1),(position[1]-1)]) or (new_position == [(position[0]-1),(position[1]+1)]) or (new_position == [(position[0]-1),(position[1]-1)]):
            if ChessGame.check_pos(self.position, new_position) and ChessGame.check_space(self, black, white, new_position) is True:
                self.position = new_position
                print("Moved!, pos:", self.position)
                return
        print("Invalid move for King")
        return

    def get_symbol(self):
        return '♔' if self.colour == 'black' else '♚'