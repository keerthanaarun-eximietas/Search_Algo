from collections import deque
from collections.abc import Hashable, Mapping, Sequence
from typing import TypeVar


Node = TypeVar("Node", bound=Hashable)


def breadth_first_search(
    graph: Mapping[Node, Sequence[Node]], start: Node, goal: Node
) -> list[Node] | None:
    """Return a shortest unweighted path from start to goal, if one exists."""
    queue = deque([start])
    parents: dict[Node, Node | None] = {start: None}
    while queue:
        node = queue.popleft()
        if node == goal:
            return _reconstruct_path(parents, goal)
        for neighbor in graph.get(node, ()):
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
    return None


def depth_first_search(
    graph: Mapping[Node, Sequence[Node]], start: Node, goal: Node
) -> list[Node] | None:
    """Return a depth-first path from start to goal, if one exists."""
    stack = [start]
    parents: dict[Node, Node | None] = {start: None}
    while stack:
        node = stack.pop()
        if node == goal:
            return _reconstruct_path(parents, goal)
        for neighbor in reversed(graph.get(node, ())):
            if neighbor not in parents:
                parents[neighbor] = node
                stack.append(neighbor)
    return None


def _reconstruct_path(
    parents: Mapping[Node, Node | None], goal: Node
) -> list[Node]:
    path: list[Node] = []
    current: Node | None = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    return list(reversed(path))
