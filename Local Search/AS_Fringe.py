class Fringe_list:
    def __init__(self):
        self.list = []

    def add(self, node, problem = None):

        if problem != None:
            node.heuristic = problem.heuristic_func(node.state) + node.path_cost

        if len(self.list) < 1: # Primo in problem,serimento è sicuramente all'indice 0
            self.list.insert(0,node)
            return 1
        else:
            for index, element in enumerate(self.list):
                if element.heuristic > node.heuristic: # se trovo un nodo con path cost maggiore mi inserisco al suo posto
                    self.list.insert(index, node)
                    return 1
                elif index == len(self.list)-1: # se non lo trovo e sono arrivato a fine lista allora nessuno ha un path cost maggiore del mio
                    self.list.append(node)
                    return 1
            return 0

    def pop(self):
        if (len(self.list) == 0):
            print("EMPTY LIST!!")
            return None
        return self.list.pop(0)

    def get_list(self):
        print('--- Fringe List: ---\n')
        for node in self.list:
            print('Node name:' ,node.id, '\nNode Depth:', node.depth, '\nNode actual path cost:',node.path_cost)

