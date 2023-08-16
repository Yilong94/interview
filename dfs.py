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
    traversal_order = []
    stack = Stack()
    visited = {}

    stack.push(vertex)

    while stack.peek():
        print([i.value for i in stack.stack])
        current = stack.pop()

        if current.value in visited:
            continue

        traversal_order.append(current.value)
        visited[current.value] = True

        for neighbour in sorted(
            current.neighbours, key=lambda vertex: vertex.value, reverse=True
        ):
            stack.push(neighbour)

    return traversal_order
