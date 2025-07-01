def minimum(self, node):
        """
        find the minimum node when node regard as a root node   
        :param node:
        :return: minimum node 
        """
        temp_node = node
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node