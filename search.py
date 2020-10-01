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
line_of_sight = {               #line of sight distance
    "Arad":366,
    "Bucharest":0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 178,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 98,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

# make a list of the cities
cities = list(graph.keys())
# set start and end nodes
start_node = "Oradea"
goal_node = "Bucharest"

def guess_function(prev, stack):        #used for DFS heuristic
    distance = {}

    for items in stack:                 #dictionary used to sum up the distances with the line of sight
        distance.update({(graph[prev][items]+line_of_sight[items]):items})
   
    #print("Min", stack)
    return distance[min(distance)] #return city with minimum distance

def aStar(start, end):            #DFS
    stack = []                  #stack for putting nodes
    visited = {}                #dictionary where key is the city and their values are boolean
    path = []                   #Path to destination
    distance = 0
    previous = ""

    stack.append(start)         #stack to start

    for city in cities:         #set all nodes to unvisited
        visited.update({city:False})

    while(len(stack)):
        print(path + stack)
        if (len(stack)>1):
            node = guess_function(previous,stack)   #get the minimum based on distance
            stack = []
        else:
            node = stack.pop()

        if (visited[node] == False):    #if not visited then make true
            visited[node] = True
            if (len(path) > 0):         #add the distances if the path > 0
                #print ("path",path)
                previous = path[-1]
                distance += graph[previous][node]
                # print distance
            
            path.append(node)       #add to path
            
            if (visited[end]):          #reached destination? then end
                #print("\nA* Search")
                print("Path:",path)
                print("Distance:", distance, "\n")
                break
            
            for adj in graph[node]:
                if (visited[adj] == False):         #add the 
                    stack.append(adj)
        previous = node

def djikstra(graph,src,dest, visited=[],distances={},predecessors={}):
    if src == dest:
        # build the shortest path
        path = []
        pred = dest
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
        print(visited)
        next = min(unvisited, key = unvisited.get)
        # recurse !!
        djikstra(graph, next, dest, visited, distances, predecessors)



#DFS(start_node, goal_node)
#BFS(start_node, goal_node)
print("\nDijikstra: ")
djikstra(graph, start_node, goal_node)
print("A* search: ")
aStar(start_node, goal_node)



