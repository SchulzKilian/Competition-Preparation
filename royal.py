def findhamiltonians(graph, current, goal,visited):
    if current ==goal:
        for node in visited:
            hamiltonians.add(node)

    else:
        for possibility in graph[current]:
            if possibility in visited:
                continue
            vis = visited.copy()
            vis.add(possibility)
            findhamiltonians(graph, possibility, goal, vis)


def findpathwithout(graph, current, goal, visited):
    if current == goal:
        return True
    else:
        for possibility in graph[current]:
            if possibility in hamiltonians or possibility in visited:
                continue
            vis = visited.copy()
            vis.add(possibility)

            if findpathwithout(graph,possibility, goal, vis):
                return True

    return False
    



hamiltonians = set()
graph = {}

x = input().split()

numCities, numRoads, days = int(x[0]), int(x[1]), int(x[2])

for i in range(numRoads):
    x = input().split()
    firstcity = x[0]
    secondcity = x[1]
    if firstcity in graph.keys():
        graph[firstcity].append(secondcity)
    else:
        graph[firstcity]=[secondcity]
    if secondcity in graph.keys():
        graph[secondcity].append(firstcity)
    else:
        graph[secondcity]=[firstcity]

for i in range(days):
    
    x = input().split()
    celestia1, celestia2, luna1,luna2,  = x[0],x[1],x[2],x[3]
    if luna1  in (celestia1,celestia2) or luna2 in (celestia1,celestia2):
        print("NO")
        continue
    #find hamiltonian paths for celestia
    visited = {celestia1}
    current = celestia1
    hamiltonians = set()
    findhamiltonians(graph, current, celestia2, visited)
    visited = {luna1}
    if luna1 in hamiltonians or luna2 in hamiltonians:
        print("NO")
        continue
    value = findpathwithout(graph, luna1, luna2,visited)
    if value:
        print("YES")
    else:
        print("NO")
    






    

