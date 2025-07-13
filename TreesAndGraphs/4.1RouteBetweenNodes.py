"""
Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
"""

def bfs(graph:dict, start:str, end:str) -> bool:
    from collections import deque
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)

    while queue:
        curr = queue.popleft()
        if curr == end:
            return True
        for n in graph[curr]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
    return False

if __name__ == "__main__":
    assert bfs({"A": ["B"], "B": [], "C": []}, "A", "B") == True
    assert bfs({"A": ["B"], "B": ["C"], "C": []}, "A", "C") == True
    assert bfs({"A": ["B"], "B": [], "C": []}, "A", "C") == False
    assert bfs({"A": ["B"], "B": ["C"], "C": ["A"]}, "A", "C") == True
    assert bfs({"A": ["B"], "B": [], "C": ["D"], "D": []}, "A", "D") == False
    assert bfs({"A": ["B"], "B": ["C"], "C": []}, "A", "A") == True
    assert bfs({str(i): [str(i+1)] for i in range(10)}, "0", "9") == True
    assert bfs({"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": ["F"], "F": []}, "A", "F") == True
    assert bfs({"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": [], "F": []}, "A", "F") == False
    assert bfs({"A": ["A"]}, "A", "A") == True
