import Game as G

if __name__ == '__main__':

    FirstMove = 'MAX'
    min_max_depth = 10
    board_dimension = 5

    g = G.Game(board_dimension, FirstMove, min_max_depth) #inizializzo gioco

    g.min_max_alfa_beta()


