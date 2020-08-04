def arc_3(CSP):
    print(' DEBUG - Inizio Arc_3 Consistency')
    queue = load_queue(CSP) #a queue of arcs, initially all the arcs in csp

    while len(queue) != 0:
        actual_arc = queue.pop()
        xi = actual_arc[0]
        xj = actual_arc[1]
        if revise(CSP, xi, xj) == True:
            if len(CSP.domains[xi]) == 0:
                return False

            for var in CSP.variables:
                for constraint in CSP.constraints[var]:
                    if constraint.variables[1] == xi:
                        queue.append(constraint.variables)
                        aux = constraint.variables[1], constraint.variables[0] #direzione inversa
                        queue.append(aux)
    print(' DEBUG - Fine Arc_3 Consistency')
    return True


def load_queue(CSP):

    queue = []
    for var in CSP.variables:
        for constraint in CSP.constraints[var]:
            if constraint.variables not in queue:
                if len(constraint.variables) > 1:
                    queue.append(constraint.variables)
                    aux = list()
                    aux.append(constraint.variables[1])
                    aux.append(constraint.variables[0])
                    queue.append(aux) #direzione inversa
    return queue

def revise(CSP, xi, xj): #returns true iff we revise the domain of Xi
    revised = False
    flag = True

    test = [] #lista temporanea usata per eliminare valori dal dominio (dic[var][domain])
    for index, x in enumerate(CSP.domains[xi]):
        flag = True
        for y in CSP.domains[xj]:
            if revise_condition(CSP, x,y ,xi,xj): #vincolo soddisfatto
                flag = False

        if flag != False:
            revised = True
        else:
            test.append(CSP.domains[xi][index])

    CSP.domains[xi] = test

    return revised

def revise_condition(CSP, x, y, xi, xj):
    assignment = {}
    assignment[xi] = x
    assignment[xj] = y

    return CSP.consistent(xi, assignment)
