"""
    ? Problem Statement: BFT Graph
    
    ! Time Complexity: O(v + e)
    ! Space Complexity: O(v)
"""

def bfs(edges: list[list[int]], graphType: str, startNode: int or None = None) -> None:
    """
        graphType refers to undirected or directed type passed as string. It is also a mandatory parameter.
    """
    if len(edges) == 0: return
    
    adjacencyList = getAdjacencyList(edges, graphType)
    
    bfsQueue: list[int] = []
    visitedSet: set[int] = set()
    
    if startNode is None:
        bfsQueue.append(edges[0][0])
        visitedSet.add(edges[0][0])
    else:
        bfsQueue.append(startNode)
        visitedSet.add(startNode)
    
    
    while len(bfsQueue) > 0:
        currentNode = bfsQueue.pop(0)
        adjacentNodes = adjacencyList[currentNode]
        
        for adjacentNode in adjacentNodes:
            if adjacentNode not in visitedSet:
                bfsQueue.append(adjacentNode)
                visitedSet.add(adjacentNode)
                
        print(currentNode)
    
    

def getAdjacencyList(edges: list[list[int]], graphType) -> dict[int, list[int]]:
    adjacencyList: dict[int, list[int]] = dict()
    
    for edge in edges:
        if edge[0] not in adjacencyList:
            adjacencyList[edge[0]] = [edge[1]]
        else:
            adjacencyList[edge[0]].append(edge[1])
        
        if graphType == "undirected":   
            if edge[1] not in adjacencyList:
                adjacencyList[edge[1]] = [edge[0]]
            else:
                adjacencyList[edge[1]].append(edge[0])
            
    return adjacencyList

bfs([
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 0],
    [2, 3],
    [3, 3]
], "directed", 1)