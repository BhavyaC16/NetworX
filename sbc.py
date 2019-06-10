#!/usr/bin/env python3

import re
import itertools

#ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Bhavya Chopra"
    email = "bhavya18333@iiitd.ac.in"
    

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        self.edges    = ordered_edges
        self.validate()
        self.Adjacency_Lists = self.neighbors()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        #if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            #raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def neighbors(self):
    	Adj_List={}
    	for i in self.vertices:
    		Adj_List[i]=[]
    		for j in self.edges:
    			if j[0]==i:
    				Adj_List[i].append(j[1])
    			if j[1]==i:
    				Adj_List[i].append(j[0])
    	return Adj_List

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
        D_flags = {}
        Prev_Node = {}
        for i in self.vertices:
        	D_flags[i]   = False
        	Prev_Node[i] = -1
        Q = []
        D_flags[start_node]=True
        Q.append(start_node)
        while Q!=[]:
        	for j in range(0,len(self.Adjacency_Lists[Q[0]])):
        		if D_flags[self.Adjacency_Lists[Q[0]][j]]!=True:
        			Q.append(self.Adjacency_Lists[Q[0]][j])
        			D_flags[self.Adjacency_Lists[Q[0]][j]]=True
        			Prev_Node[self.Adjacency_Lists[Q[0]][j]]=Q[0]
        	Q.remove(Q[0])
        shortest_path = []
        current_node = end_node
        shortest_path.append(end_node)
        while current_node!=start_node:
        	shortest_path.append(Prev_Node[current_node])
        	current_node = Prev_Node[current_node]
        return len(shortest_path)-1

    def all_shortest_paths(self,start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        dist = self.min_dist(start_node,end_node)
        allpaths = self.all_paths(start_node,end_node,dist,[])
        paths = []
        n = len(allpaths)//(dist+1)
        p=0
        q=dist+1
        for i in range(0,n):
        	a = allpaths[p:q]
        	paths.append(a)
        	p+=(dist+1)
        	q+=(dist+1)
        return paths

    def all_paths(self,node, destination, dist, path):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """
        path=path+[node]
        if len(path)==dist+1:
        	if node==destination:
        		return path
        	else:
        		return None
        my_paths = []

        for i in self.Adjacency_Lists[node]:
        	if i not in path:
        		returned_paths = self.all_paths(i,destination,dist,path)
        		if returned_paths!=None:
        			my_paths=my_paths+returned_paths
        if my_paths!=[]:
        	return my_paths
        else:
        	return None
        
    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        sum = 0
        for i in self.vertices:
        	for j in self.vertices:
        		x = 0
        		y = 0
        		if i<j and i!=node and j!=node:
        			a = self.all_shortest_paths(i,j)
        			x = len(a)
        			for k in a:
        				if node in k:
        					y+=1
        			sum+=(y/x)
        b = len(self.vertices)
        c = (b-1)*(b-2)/2
        return sum/c

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        l = {}
        top_k = []
        top = 0
        for i in self.vertices:
        	a = self.betweenness_centrality(i)
        	l[i]=a
        	if a>=top:
        		top = a
        for j in self.vertices:
        	if l[j]==top:
        		top_k.append(j)
        s1 = str(top_k)[1:-1]
        s = "k="+str(len(top_k))+", SBC="+str(top)+", Top Nodes="+s1
        return s

if __name__ == "__main__":
    print("Enter all vertices, separated by space:")
    vertices = list(map(int, input().split()))
    print("Enter the number of edges:")
    E = int(input())
    print("Enter the edges:")
    edges = []
    for i in range(0,E):
        e = list(map(int, input().split()))
        T = (e[0],e[1])
        edges.append(T)
    #edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]

    graph = Graph(vertices, edges)
    print(graph.top_k_betweenness_centrality())
