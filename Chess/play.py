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



print("This chess game is run with [row, column], not letters and numbers, because I feel like it. Also, I had a skill issue, the board's rows are flipped.")


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