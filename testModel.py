from model.model import Model

m = Model()
graph = m.buildGraph(year=1817)

for nodo in graph.nodes():
    print("Componente connessa:")
    conn = m.calcolaComponentiConnnesse(graph)
    print(conn)

m.getConnessa()
