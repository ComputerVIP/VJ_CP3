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



print("This chess game is run with [row, column], not letters and numbers, because I feel like it.")


def main():
    display_base = "■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■\n■ □ ■ □ ■ □ ■ □\n□ ■ □ ■ □ ■ □ ■"
    white = [(white_pawn1 := Pawn('white', [2,1], 'pawn')),(white_pawn2 := Pawn('white', [2,2], 'pawn')),(white_pawn3 := Pawn('white', [2,3], 'pawn')),(white_pawn4 := Pawn('white', [2,4], 'pawn')),(white_pawn5 := Pawn('white', [2,5], 'pawn')),(white_pawn6 := Pawn('white', [2,6], 'pawn')),(white_pawn7 := Pawn('white', [2,7], 'pawn')),(white_pawn8 := Pawn('white', [2,8], 'pawn')),(white_rook1 := Rook('white',[1,1],'rook')),(white_rook2 := Rook('white',[1,8],'rook')),(white_knight1 := Knight('white',[1,2],'knight')),(white_knight2 := Knight('white',[1,7],'knight')),(white_bishop1 := Bishop('white',[1,3],'bishop')),(white_bishop2 := Bishop('white',[1,6],'bishop')),(white_king := King('white',[1,4],'king')),(white_queen := Queen('white',[1,5],'queen'))]

    black = [(black_pawn1 := Pawn('black', [7,1], 'pawn')),(black_pawn2 := Pawn('black', [7,2], 'pawn')),(black_pawn3 := Pawn('black', [7,3], 'pawn')),(black_pawn4 := Pawn('black', [7,4], 'pawn')),(black_pawn5 := Pawn('black', [7,5], 'pawn')),(black_pawn6 := Pawn('black', [7,6], 'pawn')),(black_pawn7 := Pawn('black', [7,7], 'pawn')),(black_pawn8 := Pawn('black', [7,8], 'pawn')),(black_rook1 := Rook('black',[8,1],'rook')),(black_rook2 := Rook('black',[8,8],'rook')),(black_knight1 := Knight('black',[8,2],'knight')),(black_knight2 := Knight('black',[8,7],'knight')),(black_bishop1 := Bishop('black',[8,3],'bishop')),(black_bishop2 := Bishop('black',[8,6],'bishop')),(black_king := King('black',[8,4],'king')),(black_queen := Queen('black',[8,5],'queen'))]

    # run the UI/game loop using the same piece lists so state persists
    while True:
        ChessGame.show_board(white, black, display_base)
        if ChessGame.king_ded(white, black) is True:
            print("Game over!")
            break

        choice = input('''1. Move Piece
2. Check Pieces
3. Get Position of Piece
4. Get Piece Symbol
5. Exit
    
    ''').strip()

        if choice == "1":
            piece = ChessGame.find_piece(white, black)
            if piece is None:
                continue
            ie = list(map(int, input("What's the row and column of the move you want to do, seperated by a space?\n\n    ").split()))
            try:
                # operate on the same piece instance so its .position is updated in the lists
                piece.move(piece.position, ie, white, black)
            except Exception as e:
                print("Invalid input/move:", e)
            continue

        elif choice == "2":
            try:
                ChessGame.pieces_left(white, black, input("What's your colour?\n\n    ").lower().strip())
            except:
                print("Error in finding pieces left")
            continue

        elif choice == "3":
            try:
                typ = input("What's the type of your piece?").lower().strip()
                for i in black + white:
                    if i.type == typ:
                        ChessGame.piece_pos(i)  
            except:
                print("Invalid input!")
            continue

        elif choice == "4":
            pi = ChessGame.find_piece(white, black)
            try:
                if pi:
                    print(pi.get_symbol())
            except:
                print("Error in finding character!")
            continue

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
            continue
    

main()
