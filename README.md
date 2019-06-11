# NetworX
NetworX is a program to find the nodes with the maximum betweenness centrality in an undirected and unweighted graph.

## Usage
1. Run [sbc.py](https://github.com/BhavyaC16/NetworX/blob/master/sbc.py)
2. Enter the list of space separated vertices of the graph.
3. Next, enter the number of edges.
4. Finally, enter all the edges.

The output displays the following information:
  -k(number of nodes with maximum betweenness centrality)
  -x(maximum betweenness centrality in the graph)
  -V(vertices having the maximum betweenness centrality)

## Sample Input and Output
### Input
```
  Enter all vertices, separated by space:
  1 2 3 4 5 6
  Enter the number of edges:
  7
  Enter the edges:
  1 2
  1 5
  2 3
  2 5
  3 4
  4 5
  4 6
```
### Output
```
  k=1, SBC=0.45, Top Nodes=4
```
## Description
The program uses the following methods for finding the standard betweenness centrality:
```
def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node
        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to
        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
```

```
def all_shortest_paths(self,start_node, end_node):
        '''
        Finds all shortest paths between start_node and end_node
        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths
        Returns:
            A list of path, where each path is a list of integers.
        '''
```

```
def all_paths(self,node, destination, dist, path):
        '''
        Finds all paths from node to destination with length = dist
        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed
        Returns:
            List of path, where each path is list ending on destination
            Returns None if there no paths
        '''
```

```
def betweenness_centrality(self, node):
        '''
        Find betweenness centrality of the given node
        Args:
            node: Node to find betweenness centrality of.
        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        '''
```

```
def top_k_betweenness_centrality(self):
        '''
        Find top k nodes based on highest equal betweenness centrality.
        
        Returns:
            List ofIntegers, denoting top k nodes based on betweenness
            centrality.
        
```
