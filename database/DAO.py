from database.DB_connect import DBConnect
from model.border import Border
from model.state import State

class DAO():

    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select DISTINCT c.* 
                    from country c, contiguity c2 
                    where c.CCode = c2.state1no or c.CCode = c2.state2no"""

        cursor.execute(query)

        for row in cursor:
            res.append(State(row["StateAbb"], row["CCode"], row["StateNme"]))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getStatesYear(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select DISTINCT c.* 
                    from country c, contiguity c2 
                    where (c.CCode = c2.state1no or c.CCode = c2.state2no) and c2.`year` < %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            res.append(State(row["StateAbb"], row["CCode"], row["StateNme"]))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getBorders(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select c.year, c.state1ab, c.state2ab, LEAST(c.state1no, c.state2no) AS stato1, GREATEST(c.state1no, c.state2no) as stato2
                    from contiguity c 
                    where c.`year` < %s
                    and c.conttype = 1
                    GROUP BY LEAST(c.state1no, c.state2no), GREATEST(c.state1no, c.state2no), c.year, c.state1ab, c.state2ab
                    order by c.state1ab ASC"""
        cursor.execute(query, (year, ))

        for row in cursor:
            res.append(Border(row["stato1"], row["stato2"], row["year"]))

        cursor.close()
        conn.close()
        return res