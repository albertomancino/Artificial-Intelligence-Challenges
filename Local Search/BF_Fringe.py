class Fringe_list:
    def __init__(self):
        self.list = []

    def add(self, node, problem = None):
        self.list.append(node)

    def pop(self):
        if (len(self.list) == 0):
            print("EMPTY LIST!!")
            return None
        return self.list.pop(0)

    def get_list(self):
        print('--- Fringe List: ---\n')
        for node in self.list:
            print('Node name:' ,node.id, '\nNode Depth:', node.depth, '\nNode actual path cost:',node.path_cost)

