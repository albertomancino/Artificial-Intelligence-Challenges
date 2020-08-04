from copy import deepcopy
from random import randint

class State:

    def __init__(self, N, player='MAX'):

        self.min = 'MIN'
        self.max = 'MAX'
        self.empty = '.'
        self.special = '*'
        # met è il simbolo che si ottiene quando MIN E MAX sono nella stessa cella
        self.met = 'X'

        self.N = N

        self.special_points_number = round(N * N / 4)
        self.special_points = list()

        self.max_position = (0,0)
        self.min_position = (N-1,N-1)

        self.max_actual_points = 0

        self.initialize_state(N)

        self.player_turn = player


        #todo
        self.worst_max_case = 0 - 1
        self.worst_min_case = (N - 1) + (N - 1) + self.special_points_number + 1

    def initialize_state(self, N):

        # CREAZIONE PUNTI SPECIALI
        while len(self.special_points) < self.special_points_number:

            x_point = randint(0, N-1)
            y_point = randint(0, N-1)

            point = (x_point, y_point)
            # controllo non sia già presente
            if point not in self.special_points:
                self.special_points.append(point)

        # CASO: PUNTO SPECIALE = PUNTO DI PARTENZA MAX
        if (0,0) in self.special_points:
            self.special_points.remove((0,0))
            self.max_actual_points += 1

    def copy(self, turn):

        new_state = State(self.N, turn)
        new_state.special_points = deepcopy(self.special_points)
        new_state.max_position = self.max_position
        new_state.min_position = self.min_position
        new_state.max_actual_points = self.max_actual_points

        return new_state


    def draw_board(self):
        # print header
        print('\t', end='')
        for column in range(0, self.N):
            print(column, '\t\t', end='')
        print()

        for i in range(0, self.N):
            print(i, end='')
            for j in range(0, self.N):
                if (i,j) == self.min_position == self.max_position:
                    print('\t{}\t|'.format(self.met), end=" ")
                elif (i,j) == self.min_position:
                    print('\t{}\t|'.format(self.min), end=" ")
                elif (i,j) == self.max_position:
                    print('\t{}\t|'.format(self.max), end=" ")
                elif (i,j) in self.special_points:
                    print('\t{}\t|'.format(self.special), end=" ")

                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()



    def action(self):

        # Le azioni possibili sono gli inserimenti nella colonna 0,1,2,3,4,5 se questa non è piena

        action_list = ['SU','GIU','DX','SX']

        if self.player_turn == 'MAX':
            position = self.max_position
        else:
            position = self.min_position
        #check SU
        if position[0] == 0:
            action_list.remove('SU')
        if position[0] == self.N-1:
            action_list.remove('GIU')
        if position[1] == 0:
            action_list.remove('SX')
        if position[1] == self.N-1:
            action_list.remove('DX')

        return action_list

    def result(self, action):

        new_state = self.copy(self.player_turn)

        # Azione non consentita
        if action not in self.action():
            print('Azione non consentita!')
            return new_state

        else:
            if self.player_turn == 'MAX':
                if action == 'SU':
                    new_x = self.max_position[0] - 1
                    new_y =  self.max_position[1]
                    new_pos = (new_x,new_y)
                    new_state.max_position = new_pos

                    #controllo se max mangia un punto speciale
                    if new_pos in new_state.special_points:
                        new_state.special_points.remove(new_pos)
                        new_state.max_actual_points += 1

                elif action == 'GIU':
                    new_x = self.max_position[0] + 1
                    new_y =  self.max_position[1]
                    new_pos = (new_x,new_y)
                    new_state.max_position = new_pos

                    #controllo se max mangia un punto speciale
                    if new_pos in new_state.special_points:
                        new_state.special_points.remove(new_pos)
                        new_state.max_actual_points += 1

                elif action == 'DX':
                    new_x = self.max_position[0]
                    new_y =  self.max_position[1] + 1
                    new_pos = (new_x,new_y)
                    new_state.max_position = new_pos

                    #controllo se max mangia un punto speciale
                    if new_pos in new_state.special_points:
                        new_state.special_points.remove(new_pos)
                        new_state.max_actual_points += 1

                elif action == 'SX':
                    new_x = self.max_position[0]
                    new_y =  self.max_position[1] - 1
                    new_pos = (new_x,new_y)
                    new_state.max_position = new_pos

                    # controllo se max mangia un punto speciale
                    if new_pos in new_state.special_points:
                        new_state.special_points.remove(new_pos)
                        new_state.max_actual_points += 1


            else:
                if action == 'SU':
                    new_x = self.min_position[0] - 1
                    new_y =  self.min_position[1]
                    new_pos = (new_x,new_y)
                    new_state.min_position = new_pos
                elif action == 'GIU':
                    new_x = self.min_position[0] + 1
                    new_y =  self.min_position[1]
                    new_pos = (new_x,new_y)
                    new_state.min_position = new_pos
                elif action == 'DX':
                    new_x = self.min_position[0]
                    new_y =  self.min_position[1] + 1
                    new_pos = (new_x,new_y)
                    new_state.min_position = new_pos
                elif action == 'SX':
                    new_x = self.min_position[0]
                    new_y =  self.min_position[1] - 1
                    new_pos = (new_x,new_y)
                    new_state.min_position = new_pos



        # scambio il giocatore di turno
        new_state.player_turn = self.next_player()

        return new_state

    def terminal_state(self):

        if self.max_position == self.min_position:
            return 'MIN'
        if self.special_points_number == self.max_actual_points:
            return 'MAX'

        return None


    def next_player(self):

        if self.player_turn == 'MAX':
            return 'MIN'
        elif self.player_turn == 'MIN':
            return 'MAX'

    def manhattan_distance(self):

        x_distance = abs(self.min_position[0]-self.max_position[0])
        y_distance = abs(self.min_position[1]-self.max_position[1])

        return x_distance + y_distance



    def heuristic(self):

        return self.manhattan_distance() + self.max_actual_points

