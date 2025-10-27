from pieces import *

'''
Requirements:
    Follow the provided class diagram exactly 
    Implement ChessPiece as an abstract class 
    Create all six concrete piece classes (Pawn, Rook, Knight, Bishop, Queen, King) 
    Implement canMoveTo(), getSymbol() methods 
    Create ChessGame class with whitePieces and blackPieces lists 
    Implement movePiece(), removePiece(), getPiecesLeft(), and getPieceAt() in ChessGame 
    Create correct number of pieces for each player 
    Set up pieces in starting positions 
    Demonstrate moving 5 different pieces 
    Implement basic move validation for each piece type 
    Use removePiece() method for capturing 
    Put all classes on 1 file separate from your running file 
    Add comments to explain your code 
    Test each piece type for correct movement 
    Focus on core functionality over advanced game logic

'''

# ■  □  ▢
# Each row is 15 chars, 8 blocks, 7 spaces
# First row is always 1 more than the others, (16 regularly)
#display_base = "■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■"
#a= 0
# [2,1] == a= 19
# [3,1] == 35
'''
for i in display_base:
    a += 1
    if a == 16:
        print(i, "okokd")
print("Done")
'''
board = [
         [1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],
         [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],
         [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],
         [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],
         [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],
         [6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],
         [7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],
         [8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8]]


def main():
    display_base = "■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■"
    white = [(white_pawn1 := Pawn('white', [2,1], 'pawn')),(white_pawn2 := Pawn('white', [2,2], 'pawn'))]
    black = [(black_pawn1 := Pawn('black', [3,1], 'pawn')), (black_pawn2 := Pawn('black', [7,2], 'pawn'))]

    ChessGame.show_board(white, black, display_base)

    choice = input('''1. Move Piece
2. Check Pieces
3. Get Position of Piece
4. Get Piece Symbol
5. Show board
5. Exit
    
    ''')
    for i in white:
        print(i.position, i.type, i.colour)
    for i in black:
        print(i.position, i.type, i.colour)
    if choice == "1":
        piece = ChessGame.find_piece(white, black)
        ie = list(map(int, input("What's the row and column of the move you want to do, seperated by a space?\n\n    ").split()))
        try:
            ChessGame.move_piece(piece, ie, white, black)
            return main()
        except:
            print("Invalid input/move")
            return main()
    elif choice == "2":
        try:
            ChessGame.pieces_left(white, black, input("What's your colour?\n\n    ".lower().strip()))
            return main()
        except:
            print("Error in finding pieces left")
            return main()
    elif choice == "3":
        try:
            typ = input("What's the type of your piece?")
            for i in black:
                if i.colour == typ.lower().strip():
                    ChessGame.piece_pos(i)  
            for i in white:
                if i.colour == typ.lower().strip():
                    ChessGame.piece_pos(i)
            return main()
        except:
            print("Invalid input!")
            return main()
    elif choice == "4":
        pi = ChessGame.find_piece(white, black)
        try:
            print(pi.get_symbol)
            return main()
        except:
            print("Error in finding character!")
            return main()
    elif choice == "5":
        return
    else:
        print("Invalid choice!")
        return main()
    

main()