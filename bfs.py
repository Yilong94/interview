from queue_custom import *


def bfs(vertex):
    traversal_order = []
    visited = {}
    queue = Queue()

    visited[vertex.value] = True
    queue.enqueue(vertex)

    while queue.peek():
        current = queue.dequeue()

        traversal_order.append(current.value)

        for neighbour in current.neighbours:
            if neighbour.value in visited:
                continue

            # the visit happens when you are iterating through each neighbour
            # not when the node is removed from the queue
            #
            # => this means that before it goes into the queue, it MUST have been visited
            visited[neighbour.value] = True
            queue.enqueue(neighbour)

    return traversal_order


# this solution is more intuitive than bfs() in my opinion
# since I would think `visited` means that I am actually pointing to the vertex than I am visiting
# instead of the neighbouring vertex that I can 'see'
def bfs2(vertex):
    traversal_order = []
    visited = {}
    queue = Queue()

    queue.enqueue(vertex)

    while queue.peek():
        current = queue.dequeue()

        if current.value in visited:
            continue

        traversal_order.append(current.value)
        visited[current.value] = True

        for neighbour in sorted(current.neighbours, key=lambda vertex: vertex.value):
            queue.enqueue(neighbour)

    return traversal_order
