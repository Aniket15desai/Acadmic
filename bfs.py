graph = {
  'A' : ['B','C', 'D'],
  'B' : ['E', 'F'],
  'C' : ['G'],
  'D' : ['H'],
  'E' : [],
  'F' : [],
  'G' : [],
  'H' : []
}

#visited = [] 
queue = []

def bfs(graph, node):
  queue.append(node)
  #visited.append(node)

  while len(queue) != 0:
    k = queue.pop(0) 
    print (k, end = " ") 

    for i in graph[k]:
      queue.append(i)
	

# Driver Code
node = input("Enter start node:")
print("BFS Traversal: ")
bfs(graph, node)
