def add_child(self, u, v):
        ''' add child to search tree itself.
        Arguments:
            u {int} -- father id
            v {int} --  child id
        '''

        if u == -1:
            self.root = v
            self.adj_list[v] = []
            return
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if v not in self.adj_list:
            self.adj_list[v] = []