import unittest
from dfs import *
from undirected_graph import *


def initialize_dfs():
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


class TestDFS(unittest.TestCase):
    def test_dfs_recursive(self):
        vertex = initialize_dfs()
        self.assertEqual(
            dfs_recursive(vertex, []),
            [
                "A",
                "B",
                "E",
                "J",
                "F",
                "O",
                "C",
                "G",
                "K",
                "D",
                "H",
                "L",
                "M",
                "I",
                "N",
                "P",
            ],
        )

    def test_dfs_iterative(self):
        vertex = initialize_dfs()
        self.assertEqual(
            dfs_iterative(vertex),
            [
                "A",
                "B",
                "E",
                "J",
                "F",
                "O",
                "C",
                "G",
                "K",
                "D",
                "H",
                "L",
                "M",
                "I",
                "N",
                "P",
            ],
        )


if __name__ == "__main__":
    unittest.main()
