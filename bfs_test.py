import unittest

from undirected_graph import *
from bfs import *


def initialize_bfs():
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")
    vertexH = Vertex("H")
    vertexI = Vertex("I")
    vertexJ = Vertex("J")
    vertexK = Vertex("K")
    vertexL = Vertex("L")
    vertexM = Vertex("M")
    vertexN = Vertex("N")
    vertexO = Vertex("O")
    vertexP = Vertex("P")

    vertexA.add_neighbours(vertexB)
    vertexA.add_neighbours(vertexC)
    vertexA.add_neighbours(vertexD)

    vertexB.add_neighbours(vertexE)
    vertexB.add_neighbours(vertexF)
    vertexB.add_neighbours(vertexA)

    vertexC.add_neighbours(vertexG)
    vertexC.add_neighbours(vertexA)

    vertexD.add_neighbours(vertexH)
    vertexD.add_neighbours(vertexI)
    vertexD.add_neighbours(vertexA)

    vertexE.add_neighbours(vertexJ)
    vertexE.add_neighbours(vertexB)

    vertexF.add_neighbours(vertexJ)
    vertexF.add_neighbours(vertexB)

    vertexG.add_neighbours(vertexK)

    vertexH.add_neighbours(vertexL)
    vertexH.add_neighbours(vertexM)
    vertexH.add_neighbours(vertexD)

    vertexI.add_neighbours(vertexD)
    vertexI.add_neighbours(vertexM)
    vertexI.add_neighbours(vertexN)

    vertexJ.add_neighbours(vertexO)
    vertexJ.add_neighbours(vertexE)
    vertexJ.add_neighbours(vertexF)

    vertexK.add_neighbours(vertexG)

    vertexL.add_neighbours(vertexH)

    vertexM.add_neighbours(vertexH)
    vertexM.add_neighbours(vertexI)

    vertexN.add_neighbours(vertexI)
    vertexN.add_neighbours(vertexP)

    vertexO.add_neighbours(vertexJ)

    vertexP.add_neighbours(vertexN)

    return vertexA


class TestBFS(unittest.TestCase):
    def test_bfs(self):
        vertex = initialize_bfs()
        self.assertEqual(
            bfs(vertex),
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
            ],
        )

    def test_bfs2(self):
        vertex = initialize_bfs()
        self.assertEqual(
            bfs2(vertex),
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
            ],
        )


if __name__ == "__main__":
    unittest.main()
