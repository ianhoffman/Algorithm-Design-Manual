Implementations of data structures and algorithms inspired by Steven S. Skiena's *The Algorithm Design Manual*, The Second Edition.

Algorithms currently implemented:

##### Graphs
* Breadth-First Search
* Prim's Algorithm for finding the minimum-spanning tree
* Kruskal's Algorithm for finding the minimum-spanning-tree
* Floyd's Algorithm for finding all shortest path pairs in a graph
* Dijkstra's Algorithm for finding the shortest path
* A generic network flow algorithm for calculating the maximum flow possible in a network
* A bipartite matching algorithm which uses a network flow algorithm to find the largest possible matching in a graph

##### Backtracking
* Backtracking for subsets and permutations

##### Dynamic Programming
* A brute-force recursive partition-optimization routine
* Matrix-based edit distance

##### Reductions
* Translations into 3SAT for any satisfiability instance
* *is_satisfiable*: Whether a given set of clauses *C* over a set of variables *V* can be satisfied via some truth 
assignment of each variable *v<sub>i</sub>*.
* *set_cover*: Whether a set cover for a set *X* can be constructed from *k* subsets chosen from a family of subsets 
*F*.
* *vertex_cover_to_set*: Solve a vertex cover instance by converting it to a satisfiability instance.
* *vertex_cover_to_set_cover*: Prove that set cover is NP-complete with a reduction from vertex cover.