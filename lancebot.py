import chess
import chess.pgn
import chess.polyglot
import urllib
import urllib.request
import json
import copy
from collections import defaultdict
from stockfish import Stockfish

#the functions below that gathers information on moves was switched for the website openingtree 
def downloadLance():
    username = "lancemarx" #change 
    baseUrl = "https://api.chess.com/pub/player/" + username + "/games/"
    archivesUrl = baseUrl + "archives"

    #read the archives url and store in a list
    f = urllib.request.urlopen(archivesUrl)
    archives = f.read().decode("utf-8")
    archives = archives.replace("{\"archives\":[\"", "\",\"")
    archivesList = archives.split("\",\"" + baseUrl)
    archivesList[len(archivesList)-1] = archivesList[len(archivesList)-1].rstrip("\"]}")

    #download all the archives
    for i in range(len(archivesList)-1):
        url = baseUrl + archivesList[i+1] + "/pgn"
        filename = archivesList[i+1].replace("/", "-")
        urllib.request.urlretrieve(url, "D:/Lancebot/Games/lance" + str(i) + ".pgn")
        print(filename + ".pgn has been downloaded.")
    print ("All files have been downloaded.")


    url = "https://lichess.org/api/games/user/lancemarx1?tags=true&clocks=true&evals=true&opening=true&perfType=ultraBullet%2Cbullet%2Cblitz%2Crapid%2Cclassical%2Ccorrespondence"
    urllib.request.urlretrieve(url, "D:/Lancebot/lichessGames/lance.pgn")

def buildJSONWhite(game, treeWhite):
    list = []
    board = game.board()
    count = 1
    if len(list) == 0:
        for move in game.mainline_moves():
            list.append([move, board, count])
            board.push(move)
            count += 1
    
    list.reverse()

    for moves in list:
        key = str(moves[1])
        if moves[2] % 2 != 0:
            move = moves[0]
            if treeWhite[key] == 0:
                tree = defaultdict(lambda: 0)
                tree = {str(move): 1}
                treeWhite[key] = tree
            else:
                holder = treeWhite[key]
                holder[str(move)] = holder[str(move)] + 1
                treeWhite[key] = holder  
    return treeWhite
    
def createTreeWhite():
    treeWhite = defaultdict(lambda: 0)
    pgn = open("lancemarx-white.pgn")
    LastGame = False
    for i in range(20845):
        print(i)
        games = chess.pgn.read_game(pgn)
        """"board = games.board()
        count = 1
        for move in games.mainline_moves():
            if count % 2 != 0:
                key = str(board)
                if treeWhite[key] == "DNE":
                    tree = defaultdict(lambda: "DNE")
                    tree = {str(move): 1}
                    treeWhite[key] = tree
                else:
                    holder = treeWhite[key]
                    holder[str(move)] = holder[str(move)] + 1
                    treeWhite[key] = holder  
            board.push(move)
            count += 1"""
        list = []
        try:
            board = games.board()
            if board == None:
                break
        except:
            break
        count = 1
        if len(list) == 0:
            for move in games.mainline_moves():
                list.append([move, board.copy(), count])
                board.push(move)
                count += 1

        for moves in list:
            key = str(moves[1])
            if moves[2] % 2 != 0:
                move = moves[0]
                if treeWhite[key] == 0:
                    tree = defaultdict(lambda: 0)
                    tree = {str(move): 1}
                    treeWhite[key] = tree
                else:
                    holder = defaultdict(lambda: 0)
                    holder = treeWhite[key]
                    try:
                        holder[str(move)] = holder[str(move)] + 1
                    except:
                        holder[str(move)] = 1
                    treeWhite[key] = holder 
        #treeWhite = buildJSONWhite(games, treeWhite)
    pgn = open("lancemarx1-white.pgn")
    for i in range(20845):
        print(i)
        games = chess.pgn.read_game(pgn)
        """"board = games.board()
        count = 1
        for move in games.mainline_moves():
            if count % 2 != 0:
                key = str(board)
                if treeWhite[key] == "DNE":
                    tree = defaultdict(lambda: "DNE")
                    tree = {str(move): 1}
                    treeWhite[key] = tree
                else:
                    holder = treeWhite[key]
                    holder[str(move)] = holder[str(move)] + 1
                    treeWhite[key] = holder  
            board.push(move)
            count += 1"""
        list = []
        try:
            board = games.board()
            if board == None:
                break
        except:
            break
        count = 1
        if len(list) == 0:
            for move in games.mainline_moves():
                list.append([move, board.copy(), count])
                board.push(move)
                count += 1

        for moves in list:
            key = str(moves[1])
            if moves[2] % 2 != 0:
                move = moves[0]
                if treeWhite[key] == 0:
                    tree = defaultdict(lambda: 0)
                    tree = {str(move): 1}
                    treeWhite[key] = tree
                else:
                    holder = defaultdict(lambda: 0)
                    holder = treeWhite[key]
                    try:
                        holder[str(move)] = holder[str(move)] + 1
                    except:
                        holder[str(move)] = 1
                    treeWhite[key] = holder 
    
    
    treeBlack = defaultdict(lambda: "DNE")
    pgn = open("lanceBlack.pgn")
    LastGame = False 
    for games in chess.pgn.read_game(pgn):
        board = games.board()
        count = 1
        for move in games.mainline_moves():
            if count % 2 == 0:
                key = str(board)
                if treeBlack[key] == "DNE":
                    tree = defaultdict(lambda: "DNE")
                    tree = {str(move): 1}
                    treeBlack[key] = tree
                else:
                    holder = treeBlack[key]
                    holder[str(move)] = holder[str(move)] + 1
                    treeBlack[key] = holder  
            board.push(move)
            count += 1

def createTreeBlack():       
    treeBlack = defaultdict(lambda: 0)
    pgn = open("lancemarx-black.pgn")
    LastGame = False
    for i in range(20845):
        print(i)
        games = chess.pgn.read_game(pgn)
        list = []
        try:
            board = games.board()
            if board == None:
                break
        except:
            break
        count = 1
        if len(list) == 0:
            for move in games.mainline_moves():
                list.append([move, board.copy(), count])
                board.push(move)
                count += 1

        for moves in list:
            key = str(moves[1])
            if moves[2] % 2 == 0:
                move = moves[0]
                if treeBlack[key] == 0:
                    tree = defaultdict(lambda: 0)
                    tree = {str(move): 1}
                    treeBlack[key] = tree
                else:
                    holder = defaultdict(lambda: 0)
                    holder = treeBlack[key]
                    try:
                        holder[str(move)] = holder[str(move)] + 1
                    except:
                        holder[str(move)] = 1
                    treeBlack[key] = holder 
        #treeWhite = buildJSONWhite(games, treeWhite)
    pgn = open("lancemarx1-black.pgn")
    for i in range(20845):
        print(i)
        games = chess.pgn.read_game(pgn)
        list = []
        try:
            board = games.board()
            if board == None:
                break
        except:
            break
        count = 1
        if len(list) == 0:
            for move in games.mainline_moves():
                list.append([move, board.copy(), count])
                board.push(move)
                count += 1

        for moves in list:
            key = str(moves[1])
            if moves[2] % 2 == 0:
                move = moves[0]
                if treeBlack[key] == 0:
                    tree = defaultdict(lambda: 0)
                    tree = {str(move): 1}
                    treeBlack[key] = tree
                else:
                    holder = defaultdict(lambda: 0)
                    holder = treeBlack[key]
                    try:
                        holder[str(move)] = holder[str(move)] + 1
                    except:
                        holder[str(move)] = 1
                    treeBlack[key] = holder 
    
    with open('treeBlack.json', 'w', encoding='utf-8') as f:
        json.dump(treeBlack, f, ensure_ascii=False, indent=4)

def GetTreeWhite():
    f= open("treeWhite.json",)
    j= json.load(f)
    f.close()
    return j

def GetTreeBlack():
    f= open("treeBlack.json",)
    j= json.load(f)
    f.close()
    return j

def lanceMove(board, tree):
    try:
        print(board)
        possibleMoves = tree[str(board)]
    except:
        print("Stockfish")
        return stockfishMove()
    
    TheLanceMove = ["", -1]
    for m in possibleMoves:
        if possibleMoves[m] > TheLanceMove[1]:
            TheLanceMove = [m,possibleMoves[m]]
    if TheLanceMove[1] == -1:
        return stockfishMove()
    else:
        m = TheLanceMove[0]
        stockfish.make_moves_from_current_position([m])
        print(stockfish.get_board_visual())
        return m

def stockfishMove():
    move = stockfish.get_top_moves(1)
    m = move[0]["Move"]
    stockfish.make_moves_from_current_position([m])
    print(stockfish.get_board_visual())
    print(m)
    return m

def playerMoves(m):
    stockfish.make_moves_from_current_position([m])
    return m

stockfish = Stockfish("stockfish/stockfish_14.1_win_x64_avx2.exe")


game = True
while(game == True):
    print("Would you like to play white (w) or Black (b)")
    x = True
    while x == True:
        color = input()
        if color == "w":
            tree = GetTreeBlack()
            x = False
            end = False
            board = chess.Board()
            while end == False:
                print(stockfish.get_board_visual())
                print("your move")
                player = input()
                if player == "end":
                    break
                board.push(chess.Move.from_uci(playerMoves(player)))
                board.push(chess.Move.from_uci(playerMoves(lanceMove(board, tree))))
        if color == "b":
            tree = GetTreeWhite()
            x = False
            end = False
            board = chess.Board()
            while end != True:
                board.push(chess.Move.from_uci(playerMoves(lanceMove(board, tree))))
                print("your move")
                player = input()
                if player == "end":
                    end = True
                else:
                    board.push(chess.Move.from_uci(playerMoves(player)))
        else:
            print("try again")

    


