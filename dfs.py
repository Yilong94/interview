from stack import *


def sort_by_vertex_value(vertex):
    return vertex.value


def dfs_recursive(vertex, visited):
    visited.append(vertex.value)

    for neighbour in sorted(vertex.neighbours, key=lambda vertex: vertex.value):
        if neighbour.value in visited:
            continue

        dfs_recursive(neighbour, visited)

    return visited


def dfs_iterative(vertex):
    stack = Stack()
    visited = []

    stack.push(vertex)
    while len(stack.stack) != 0:
        current = stack.pop()

        # possibility that stack can contain duplicate values
        # if value is vistied, we ignore and go to next item in stack since
        # its neighbours are already visited anyway
        if current.value in visited:
            continue

        visited.append(current.value)

        for neighbour in sorted(
            current.neighbours, key=lambda vertex: vertex.value, reverse=True
        ):
            # if value is visited, we do not push into stack
            if neighbour.value in visited:
                continue

            stack.push(neighbour)

    return visited
