import TreeNode as TN
import Problem as P
import Problem_State as PS
import timeit

if __name__ == '__main__':
    start_time = timeit.default_timer()

    print('Inserisci larghezza della griglia N:')
    N = int(input()) # LARGHEZZA

    print('Inserisci altezza della griglia M:')
    M = int(input()) # ALTEZZA

    print('Inserisci numero elementi della griglia non raagiungibili K:')
    K = int(input()) # NUMERO WALL

    V = [] #LISTA di Wall
    for x in range(K):
        print('inserisci coordinata x muro')
        auxX = int(input())
        print('inserisci coordinata y muro')
        auxY = int(input())
        V.append((auxX,auxY))

    print('Inserisci posizione INIZIALE nella griglia')
    print('inserisci coordinata x della posizione INIZIALE')
    auxX = int(input())
    print('inserisci coordinata y della posizione INIZIALE')
    auxY = int(input())
    I = (auxX,auxY)

    print('Inserisci posizione GOAL nella griglia')
    print('inserisci coordinata x della posizione GOAL')
    auxX = int(input())
    print('inserisci coordinata y della posizione GOAL')
    auxY = int(input())
    G = (auxX, auxY)

    #CHECK START & GOAL
    problem = P.Problem(N, M, K, V, PS.State(I), PS.State(G), 'BF')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(N, M, K, V, PS.State(I), PS.State(G), 'DF')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(N, M, K, V, PS.State(I), PS.State(G), 'AS')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

