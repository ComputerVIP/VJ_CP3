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
        # Determine friends/enemies
        friends = white if self.colour == "white" else black
        enemies = black if self.colour == "white" else white

        # Bounds check
        if not (1 <= new_pos[0] <= 8 and 1 <= new_pos[1] <= 8):
            return False

        # Destination occupied by friend -> illegal
        if any(p.position == new_pos for p in friends):
            return False

        # helper to find any piece at a given square
        def piece_at(pos):
            for p in friends + enemies:
                if p.position == pos:
                    return p
            return None

        # Pawn: forward moves must be clear; diagonal moves require an enemy
        if self.type == "pawn":
            dr = new_pos[0] - self.position[0]
            dc = new_pos[1] - self.position[1]
            direction = 1 if self.colour == "white" else -1

            # diagonal capture
            if dr == direction and abs(dc) == 1:
                for p in enemies:
                    if p.position == new_pos:
                        enemies.remove(p)
                        return True
                return False

            # straight move (one or two on first move)
            if dc == 0:
                # two-step from starting rank
                start_row = 2 if self.colour == "white" else 7
                if self.position[0] == start_row and dr == 2 * direction:
                    intermediate = [self.position[0] + direction, self.position[1]]
                    if piece_at(intermediate) is not None or piece_at(new_pos) is not None:
                        return False
                    return True
                # single step
                if dr == direction:
                    if piece_at(new_pos) is None:
                        return True
                    return False
            return False

        # Knight: jumps — only destination matters (friend already handled)
        if self.type == "knight":
            for p in enemies:
                if p.position == new_pos:
                    enemies.remove(p)
                    return True
            return True

        # King: one-square move
        if self.type == "king":
            dr = abs(new_pos[0] - self.position[0])
            dc = abs(new_pos[1] - self.position[1])
            if max(dr, dc) > 1:
                return False
            for p in enemies:
                if p.position == new_pos:
                    enemies.remove(p)
                    return True
            return True

        # Sliding pieces: rook, bishop, queen -> must check intermediate squares
        dr = new_pos[0] - self.position[0]
        dc = new_pos[1] - self.position[1]
        step_row = 0 if dr == 0 else (1 if dr > 0 else -1)
        step_col = 0 if dc == 0 else (1 if dc > 0 else -1)

        # validate movement vector for piece type
        if self.type == "rook" and not (dr == 0 or dc == 0):
            return False
        if self.type == "bishop" and not (abs(dr) == abs(dc) and dr != 0):
            return False
        if self.type == "queen" and not (dr == 0 or dc == 0 or abs(dr) == abs(dc)):
            return False

        steps = max(abs(dr), abs(dc))
        # check squares between start and destination (exclude destination)
        for i in range(1, steps):
            check = [self.position[0] + i * step_row, self.position[1] + i * step_col]
            if piece_at(check) is not None:
                return False

        # destination: capture enemy if present
        for p in enemies:
            if p.position == new_pos:
                enemies.remove(p)
                return True

        # empty destination -> allowed
        return True
    
    def check_pos(position, new_pos):
        # Proper bounds check: both indices must be between 1 and 8 inclusive
        if not (1 <= new_pos[0] <= 8 and 1 <= new_pos[1] <= 8):
            return False
        return True

    def find_piece(white, black):
        pie = list(map(int, input("What's the row and column of the piece, seperated by a space?\n\n    ").split()))
        ch = None
        for i in white:
            if i.position == pie:
                print(f"Your piece is {i.colour}, a {i.type} and is at {i.position}")
                ch = i
        for i in black:
            if i.position == pie:
                print(f"Your piece is {i.colour}, a {i.type} and is at {i.position}")
                ch = i
        if ch is None:
            print("No piece found at that position.")
            return None
        try:
            if int(input("1 if this is correct:\n\n    ")) == 1:
                return ch
        except:
            return None
    
    def show_board(white, black, display_base):
        # Split and make mutable
        lines = [list(line) for line in display_base.split('\n')]

        pieces = white + black

        for piece in pieces:
            row, col = piece.position  # (1–8, 1–8)
            symbol = piece.get_symbol()

            # Flip vertically: row 1 (bottom) becomes last line
            flipped_row = 8 - row

            # Each cell is 2 chars wide ("■ " or "□ ")
            char_index = (col - 1) * 2

            # Replace symbol
            lines[flipped_row][char_index] = symbol

        # Join and print
        temp = '\n'.join(''.join(line) for line in lines)
        print(temp)

    def king_ded(white, black):
        cnt = 0
        cnt2 = 0
        for i in white:
            if i.type == "king":
                cnt += 1
        for i in black:
            if i.type == "king":
                cnt2 += 1
        if cnt == 0:
            print("Black wins!")
            return True
        elif cnt2 == 0:
            print("White wins!")
            return True
        return False





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
        # check diagonal moves (1..7 steps)
        for i in range(1, 8):
            if (new_position == [position[0] + i, position[1] + i]) or (new_position == [position[0] - i, position[1] + i]) or (new_position == [position[0] + i, position[1] - i]) or (new_position == [position[0] - i, position[1] - i]):
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