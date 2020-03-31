"""Implement the three data structures: queue, stack, and priority queue with integers.
        Note, queue and stack ignores any number or weight in graph.
    Implement BFS, DFS, and djikstra's

    Use your search algorithms to input the Romanian road-network map from the textbook (Fig. 3.2, p68),
       Start node is Bucharest and the goal node is Timisoara.
       Children from the root Bucharest to be expanded are in this order: Urziceni, Fagaras, Giurgiu, and then Pitesti.

    Note, the priority queue may rearrange the node orders, which is ok.
     The priority queue will use the shortest distances from Bucharest to the nodes in it using the road-distances on the map (
     NOT the straight-line-distances) and hence, should find a shortest path.
     Your algorithm should print the nodes as they are traversed by your algorithm.

     Erika Ambrioso
     eambrioso2017@my.fit.edu
     Intro to Artificial Intellignce
"""
import heapq

# build my graph
graph = {           #graph dictionary
        "Arad": {"Zerind":75, "Timisoara":118, "Sibiu":140},
        "Bucharest": {"Urziceni":85, "Giurgiu":90, "Fagaras":211, "Pitesti": 101, "Bucharest": 0},
        "Craiova": {"Dobreta":120, "Rimnicu Vilcea":146, "Pitesti":138},
        "Dobreta": {"Mehadia":75, "Craiova":120},
        "Eforie": {"Hirsova":86},
        "Fagaras": {"Bucharest":211, "Sibiu": 99},
        "Giurgiu": {"Bucharest":90},
        "Hirsova": {"Urziceni": 98, "Eforie":86},
        "Iasi": {"Neamt": 87, "Vaslui":92},
        "Lugoj": {"Mehadia":70, "Timisoara":111},
        "Mehadia": {"Dobreta": 75, "Lugoj":70},
        "Neamt": {"Iasi":87},
        "Oradea": {"Zerind":71, "Sibiu":151},
        "Pitesti": {"Rimnicu Vilcea":97, "Craiova":138, "Bucharest":101},
        "Rimnicu Vilcea": {"Sibiu":80, "Pitesti":97, "Craiova":146},
        "Sibiu": {"Arad":140, "Oradea":151, "Rimnicu Vilcea":80, "Fagaras":99},
        "Timisoara": {"Arad":118, "Lugoj":70},
        "Urziceni":{"Vaslui":142, "Hirsova":98, "Bucharest":85},
        "Vaslui": {"Iasi":92, "Urziceni":98},
        "Zerind": {"Oradea": 71, "Arad": 75}
        }

# make a list of the cities
cities = list(graph.keys())
# set start and end nodes
start_node = "Bucharest"
goal_node = "Timisoara"

def DFS(src, goal):
    """ Implement depth first search of the graph using a stack """
    visited = {}
    path = []
    stack = []
    distance = 0

    # add the inital node to the stack
    stack.append(src)

    for city in cities:
        visited.update({city: False})

    while(len(stack)):
        node = stack.pop(len(stack)-1)
        # check if visited, mark as visited if not
        if(visited[node] == False):
            visited[node] = True
            # update the path
            path.append(node)
            # GOAL IS REACHED
            if(visited[goal]):
                print("DFS Path:", path)
                break
            # add the neighbors to the stack
            for adj in graph[node]:
                if(visited[adj] == False):
                    stack.append(adj)

def BFS(src, goal):
    """ Implement breadth-first search of the given graph using a queue"""
    visited = {}
    path = []
    queue = []
    distance = 0

    # add the inital node to the queue
    queue.append(src)
    # mark all as unvisted
    for city in cities:
        visited.update({city: False})

    while(len(queue)):
        node = queue.pop(0)
        # mark as visited
        if(visited[node] == False):
            visited[node] = True

            path.append(node)           # update path
            # GOAL REACHED
            if(visited[goal]):
                print("BFS Path:", path)
                break
            # add neighbors(adj nodes) to the queue
            for adj in graph[node]:
                if(visited[adj] == False):
                    queue.append(adj)

def djikstra(graph,src,dest, visited=[],distances={},predecessors={}):
    if src == dest:
        # build the shortest path
        path = []
        pred= dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        # print in a readable format
        readable = path[0]
        for i in range(1, len(path)):
            readable = path[i]+ '->' + readable
        print("Path: "+ readable + ",  cost= " +str(distances[dest]))
    else:
        if not visited:
            distances[src] = 0
        #visit adjacent nodes
        for adj in graph[src]:
            if adj not in visited:
                new_distance = distances[src] + graph[src][adj]
                if new_distance < distances.get(adj, float('inf')):
                    distances[adj] = new_distance
                    predecessors[adj] = src
        visited.append(src)

        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))

        next = min(unvisited, key = unvisited.get)
        # recurse !!
        djikstra(graph, next, dest, visited, distances, predecessors)



DFS(start_node, goal_node)
BFS(start_node, goal_node)
print("\n")

for city in cities:
    djikstra(graph, "Bucharest", city)




