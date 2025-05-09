import flet as ft

from model.state import State


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._view._ddStatesValue = None

    def handleCalcola(self, e):
        input = self._view._txtAnno.value

        if input is None or input == "":
            self._view.create_alert("Inserire un valore!")
            return

        try:
            anno = int(input)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un numero!", color="red"))
            self._view.update_page()
            return

        if anno < 1815 or anno > 2006:
            self._view.create_alert("Il valore inserito è fuori dal range!")
        else:
            self._view._txt_result.controls.clear()
            graph = self._model.buildGraph(anno)
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
            conn = self._model.calcolaComponentiConnnesse(graph)
            self._view._txt_result.controls.append(ft.Text(f"Il grafo presenta {conn} componenti connesse"))
            stati = []
            for nodo in graph.nodes():
                grado = graph.degree(nodo)
                stati.append((nodo.StateNme, grado))
            stati.sort()
            for nome_stato, grado in stati:
                self._view._txt_result.controls.append(ft.Text(f"{nome_stato}: {grado} stati confinanti"))
            self._view.update_page()

    def fillDD(self):
        sortedStates = sorted(self._model.states, key=lambda s: s.StateNme) #itero su una lista ordinata
        for s in sortedStates:
            self._view._ddStates.options.append(ft.dropdown.Option(key=s.StateNme, data=s, on_click=self.choiceDD))
        self._view.update_page()

    def choiceDD(self, e):
        self._view._ddStatesValue = e.control.data #recupero l'oggetto
        return self._view._ddStatesValue

    def handleRaggiungibili(self, e):
        source = self._view._ddStatesValue
        successori = self._model.getConnessa(source)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"I nodi raggiungibili da {source.StateNme} sono:"))
        for list in successori:
            for s in list:
                self._view._txt_result.controls.append(ft.Text(f"{s.__str__()}"))
        self._view.update_page()