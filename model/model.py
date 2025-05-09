import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.states = DAO.getStates()
        self.graph = nx.Graph()
        self._idMap = {}
        for state in self.states:
            self._idMap[state.CCode] = state


    def buildGraph(self, year):
        self.graph.clear()
        states = DAO.getStatesYear(year)
        self.graph.add_nodes_from(states)
        self.addAllEdges(year)
        return self.graph

    def addAllEdges(self, year):
        edges = DAO.getBorders(year)
        for e in edges:
            u = self._idMap[e.s1Id] #così gli archi sono costituti da oggetti State e non da interi
            v = self._idMap[e.s2Id]
            self.graph.add_edge(u, v)

    def calcolaComponentiConnnesse(self, graph):
        return nx.number_connected_components(graph)

    def getConnessa(self, source):
        succ = nx.dfs_successors(self.graph, source).values()
        res = []
        for s in succ:
            res.append(s)
        return res