import networkx as nx #this is a simple module for building graphs

class Solution:
    def make_graph_from_letters(self, words, graph):
        #makes nodes from set of unique letters in a file
        letters = set()
        for i in range(len(words)):
            for letter in words[i]:
                if letter != '' :
                    letters.add(letter)
        graph.add_nodes_from([i for i in letters])
        nodes = graph.nodes()
        return nodes

    def find_order(self, word1, word2):
        # a helper function to add_edges, compares consecutive pairs of words
        prefix = ''
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                prefix += word1[i]
            else:
                next_symbol_1 = word1[i]
                next_symbol_2 = word2[i]
                return next_symbol_1, next_symbol_2

    def add_edges(self, graph, words):
        # creates edges from comparing consecutive pairs. An edge points from symbol with less lexicographic
        #order to the symbol with more lexicographic order
        pointer1 = 0
        pointer2 = 1
        while pointer1 < len(words) and pointer2 < len(words) :
            edge = self.find_order(words[pointer1], words[pointer2])
            if edge is not None:
                graph.add_edge(edge[0], edge[1])

            pointer2 += 1
            pointer1 += 1

        return graph.edges()

    def find_root(self, graph):
         #the graph shouldn't contain cycles, so a root must exist
         for node in graph.nodes():
            if not graph.predecessors(node): # a list of node's predecessors
                return node                       #returns the first letter of an alphabet

    def visit(self, graph, start_node, visited):
        #
        if start_node not in visited:
            children = [child for child in graph.successors(start_node) if
                        (start_node, child) in graph.edges()]
            for child in children:
                self.visit(graph, child, visited)
            visited.append(start_node)
        return visited

    def return_alphabet(self, graph):
        #This is a library function for validation
        return nx.topological_sort_recursive(graph)

    def solve(self, filename):
        with open(filename, 'r') as file:
            words = tuple([line.rstrip(' \n') for line in file.readlines()])
        graph = nx.DiGraph()
        self.make_graph_from_letters(words, graph)
        self.add_edges(graph, words)
        root = self.find_root(graph)
        visited = []
        alphabet = self.visit(graph, root, visited)
        alphabet.reverse()
        print ('Check with library algorithm: ', self.return_alphabet(graph) == alphabet)
        return alphabet

if __name__ == '__main__':
    my_solution = Solution()
    print('My answer: ', my_solution.solve('alphabet.txt'))
