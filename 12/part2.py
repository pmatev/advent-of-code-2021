import sys
from dataclasses import dataclass
from collections import defaultdict
from typing import DefaultDict, List, Set
from pprint import pprint



@dataclass
class Edge:
    start: str
    end: str


class Graph:
    def __init__(self) -> None:
        self.nodes: DefaultDict[str, Set[str]] = defaultdict(set)

    def __getitem__(self, node: str) -> List[str]:
        return sorted(list(self.nodes[node]), key=str.lower)

    def add_edge(self, start: str, end: str):
        self.nodes[start].add(end)
        self.nodes[end].add(start)


    def __str__(self) -> str:
        return str(self.nodes)


def main():
    with open(sys.argv[1], 'r') as f:  
        edges = _parse_input(f)
    
    # build graph
    graph = Graph()
    for edge in edges:
        graph.add_edge(edge.start, edge.end)
    
    paths = find_all_paths_dfs(graph)
    pprint(paths)
    print(len(paths))


def find_all_paths_dfs(graph: Graph) -> List[List[str]]:
    '''
    start - A
    start - A - b
    start - A - b - A
    start - A - b - A - c
    start - A - b - A - c - A
    start - A - b - A - c - A - end
    start - A - b - A - c - A
    start - A - b - A - c
    start - A - b - A
    start - A - b - A - end
    start - A - b - A
    start - A - b
    start - A - b - end
    start - A - b
    start - A
    start - A - c
    start - A - c - A
    start - A - c - A - end
    start - A - c - A
    ...
    '''
    paths = []
    stack = ['start']
    visited: Set[str] = set()

    def can_visit(path: List[str], node: str) -> bool:
        if not node.islower() or node == 'end':
            return True
        
        counter: DefaultDict[str, int] = defaultdict(lambda: 0)

        for key in path:
            if key.islower():
                counter[key] += 1

        has_double = any(key for key, value in counter.items() if value >= 2)
        
        for key, value in counter.items():
            if key == node:
                if has_double and value > 0:
                    return False
            
        return True


    while len(stack):
        visited.add(','.join(stack))

        node = stack[-1]
        
        if node == 'end':
            paths.append(stack.copy())
            stack.pop()
            continue
        
        for neighbor in graph[node]:
            if neighbor == 'start':
                continue

            if not can_visit(stack, neighbor):
                continue

            if ','.join(stack + [neighbor]) in visited:
                continue
            
            stack.append(neighbor)
            break
                
        else:
            stack.pop()
    
    return paths
        

def _parse_input(file) -> List[Edge]:
    lines = [l.strip() for l in file.readlines()]

    edges = []
    for line in lines:
        a, b = line.split('-')
        edges.append(Edge(start=a, end=b))

    return edges
        


if __name__ == '__main__':
    main()