from CSP import Constraint, CSP
import ARC_3 as arc
import timeit

class item_constraint_together(Constraint):
    def __init__(self, p1: str, p2: str):
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment, variable):
        if self.p1 not in assignment or self.p2 not in assignment:
            return True
        return assignment[self.p1][0] == assignment[self.p2][0]

class items_constraint_split(Constraint):
    def __init__(self, p1: str, p2: str):
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment, variable):
        if self.p1 not in assignment or self.p2 not in assignment:
            return True
        return assignment[self.p1][0] != assignment[self.p2][0]

class item_constraint_alldiff(Constraint):
    def __init__(self, p1: str):
        super().__init__([p1])
        self.p1  = p1

    def satisfied(self, assignment, variable):
        for x in assignment:
            if x != variable and assignment[x] == assignment[variable]:
                return False
        return True

if __name__ == "__main__":
    rifiuti = ["t1", "t2", "t3", "t4", "t5"]
    alimentari = ["f1","f2","f3"]
    esplosivo = ["e1","e2"]
    surgelati = ["fz1","fz2","fz3"]
    freschi = ["fs1"]
    variables = []
    for r in rifiuti:
        variables.append(r)
    for a in alimentari:
        variables.append(a)
    for e in esplosivo:
        variables.append(e)
    for s in surgelati:
        variables.append(s)
    for f in freschi:
        variables.append(f)

    domains = {}
    for variable in variables:
        domains[variable] = [("Container 1",1),("Container 1",2),("Container 1",3),("Container 1",4),("Container 1",5),("Container 1",6),
                             ("Container 2",1),("Container 2",2),("Container 2",3),("Container 2",4),("Container 2",5),("Container 2",6),
                             ("Container 3",1),("Container 3",2),("Container 3",3),("Container 3",4),("Container 3",5),("Container 3",6),
                             ("Container 4",1),("Container 4",2),("Container 4",3),("Container 4",4),("Container 4",5),("Container 4",6)]

    csp = CSP(variables, domains)
    # vincolo sugli esplosivi
    for esp1 in esplosivo:
        for esp2 in esplosivo:
            if esp1 != esp2:
                csp.add_constraint( items_constraint_split(esp1,esp2))

    # vincolo alimentari non con i rifiuti
    for r in rifiuti:
        for a in alimentari:
            csp.add_constraint(items_constraint_split(r, a))
            csp.add_constraint(items_constraint_split(a, r))

    # vincolo freschi non con surgelati
    for f in freschi:
        for s in surgelati:
            csp.add_constraint(items_constraint_split(f, s))
            csp.add_constraint(items_constraint_split(s, f))

    # vincolo surgelati tutti nello stesso container
    for s1 in surgelati:
        for s2 in surgelati:
            csp.add_constraint(item_constraint_together(s1, s2))

    # constraint valido per tutti: tutti in posti diversi dei container
    for item in variables:
        csp.add_constraint( item_constraint_alldiff(item)) #condition = 1 insieme, 0 altrimenti

    arc.arc_3(csp)
    start_time = timeit.default_timer()
    solution = csp.backtracking_search()
    end_time = timeit.default_timer()

    if solution is None:
        print("Nessuna soluzione trovata")
    else:
        print('\nSoluzione:')
        for var in solution:
            print('\t',var, '\t:', solution[var])
        time = end_time - start_time
        print('\nTempo impiegato = ', time)
