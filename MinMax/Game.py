import time
import random
from ChallengeGame import State

class Game:
    def __init__(self, N, first_player_turn, max_depth = 1000):

        self.current_state = State(N, first_player_turn)
        self.current_state.initialize_state(N)
        self.player_turn = first_player_turn #variabile che tiene conto quale giocatore deve muovere
        self.max_depth = max_depth
        self.depth = 1


#   ---------------- ALFA BETA ALGORITHM ----------------

    def max_value_alfa_beta(self, state, alfa, beta):

        max_v = self.current_state.worst_max_case

        # variabile utilizzata quando la scelta della mossa non è randomica
        #best_move = -1

        # caso nodo foglia dell'albero, stato di termine gioco
        result = state.terminal_state()

        if result == 'MIN':
            return (state.heuristic(), None)
        if result == 'MAX':
            return (state.heuristic(), None)

        possible_moves = list()


        # Prova a fare un'altra mossa
        if self.depth < self.max_depth:

            for action in state.action():

                new_state = state.result(action)

                self.depth += 1

                # alfa è il miglior valore per la funzione MAX, ergo max_v
                (new_max_v, new_move) = self.min_value_alfa_beta(new_state, max_v, beta)

                self.depth -= 1

                # controllo alfa beta
                if new_max_v > beta:
                    return (new_max_v, action)

                # ho trovato una mossa che ha un'euristica pari a quella migliore trovata fin'ora
                if new_max_v == max_v:
                    possible_moves.append(action)

                # ho trovato una mossa che ha un'euristica migliore
                elif new_max_v > max_v:

                    max_v = new_max_v
                    #best_move = action

                    possible_moves.clear()
                    possible_moves.append(action)

            actual_move = random.choice(possible_moves)
            #actual_move = best_move

            return (max_v,actual_move)

        # Non procedere più con le mosse
        else:
            return (state.heuristic(), None)


    def min_value_alfa_beta(self, state, alfa, beta):

        min_v = self.current_state.worst_min_case  # inizializzata a +2, worse than the worst case

        # variabile utilizzata quando la scelta della mossa non è randomica
        #best_move = -1

        # caso nodo foglia dell'albero, stato di termine gioco
        result = state.terminal_state()

        if result == 'MIN':
            return (state.heuristic(), None)
        if result == 'MAX':
            return (state.heuristic(), None)

        possible_moves = list()


        # Prova a fare un'altra mossa
        if self.depth < self.max_depth:

            for action in state.action():

                new_state = state.result(action)

                self.depth += 1

                # beta è il miglior valore per la funzione MIN, ergo min_v
                (new_min_v,new_move) = self.max_value_alfa_beta(new_state, alfa, min_v)

                self.depth -= 1

                # controllo alfa beta
                if new_min_v < alfa:
                    return (new_min_v, action)

                # ho trovato una mossa che ha un'euristica pari a quella migliore trovata fin'ora
                if new_min_v == min_v:
                    possible_moves.append(action)

                # ho trovato una mossa che ha un'euristica migliore
                elif new_min_v < min_v:

                    min_v = new_min_v
                    #best_move = action

                    possible_moves.clear()
                    possible_moves.append(action)

            actual_move = random.choice(possible_moves)
            #actual_move = best_move

            return (min_v, actual_move)

        # Non procedere più con le mosse
        else:
            return (state.heuristic(), None)


    def min_max_alfa_beta(self):

        alfa = self.current_state.worst_max_case
        beta = self.current_state.worst_min_case

        while True:

            self.current_state.draw_board()
            result = self.current_state.terminal_state()

            if result != None:
                if result == 'MIN':
                    print('The winner is', self.current_state.min)
                elif result == 'MAX':
                    print('The winner is', self.current_state.max)

                return 1    # Game ended sucessfully

            # If it's MIN turn
            if self.current_state.player_turn == 'MIN':

                #input('Lancia MIN (premi invio per continuare)\n')

                start = time.time()

                (m, move) = self.min_value_alfa_beta(self.current_state, alfa, beta)

                end = time.time()

                print('Tempo elaborazione mossa: {}s'.format(round(end - start, 7)))
                print('La mossa pensata da', self.current_state.min ,'è: ', move,' con euristica = ',m, 'euristica attuale: ', self.current_state.heuristic())

                self.current_state = self.current_state.result(move)

            else:

                #input('Lancia MAX (premi invio per continuare)\n')

                start = time.time()

                (m, move) = self.max_value_alfa_beta(self.current_state, alfa, beta)


                end = time.time()
                print('Tempo elaborazione mossa: {}s'.format(round(end - start, 7)))
                print('La mossa pensata da', self.current_state.max ,'è: ', move,' con euristica = ',m)
                self.current_state = self.current_state.result(move)


