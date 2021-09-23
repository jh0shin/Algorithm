# Data Structure

## Big O notation

## Types of analyses
#### Best case analysis
#### Worst case analysis
#### Average case analysis
#### Amortized analysis
- In insertion array doubling
    - Worst case : _O(n)_
    - Amortized time : _O(1)_

## List
#### Array
- Each item access in _O(1)_
- Insertion and resize (when overflow) in _O(n)_
#### Linked list
- Insertion in _O(1)_ (if reference already given)
- Item access in _O(n)_
- Single linked list, Double linked list, Circular linked list
#### Applications
- Stack, Queue, Hashing(Chaining)

## Stack
- Last In First Out
- ArrayStack
    - isEmpty : _O(1)_
    - push, pop : Amortized _O(1)_
    - array doubling when array is full
    - array shrinking when array is 1/4 full
- LinkedListStack
    - isEmpty, pop, push : worst _O(1)_
    - no overflow or resizing
    - overhead for storing references, dealing with links
#### Infix, Postfix, Prefix
- Postfix does not require parenthesis, so compilers use it
- Conversion between infix and postfix, infix and prefix

## Queue
- First In First Out
- Priority queue with time as priority
- ArrayQueue (CircularQueue)
- LinkedListQueue
- Producer / Consumer problem

## Tree
- Finite set of one or more nodes
#### Binary tree
- Empty or consists of the root and two subtrees
- ArrayTree
- NodeTree
- Tree traversals : inorder, preorder, postorder
    - Store parent's reference in node to traversal without stack

## Union-Find
#### Forest
- A set of ***n*** disjoint trees
- Array representation
    - i = set[i] if i is root of tree
- Find operation
- Path compression : after performing find, compress all the ref on the path
  just traversed to reference to the root
- Amortized _O(nlogn)_
- Kruskal Miminum Spanning Tree algorithm

## Huffman Code
- Text compressing with minheap and binary tree
- Complexity:
    - Heap init : _O(n)_
    - _2(n-1)_ removals & _n-1_ insert op : _O(nlogn)_
    - Total : _O(nlogn)_

## Binary heap
- Data structure to implement a priority queue
- Heap is a complete binary tree with priority
- Implementation with array
    - Insert end of array, comparing with parent
    - Remove root, replace root with end of array, comparing with children
    - Insert, remove : _O(logn)_
- Bottom-up construction : _O(n)
- HeapSort : _O(nlogn)_

## Binary search tree
- Balanced BST : height _O(logn)_ in worst case
    - ex) AVL, 2-3, 2-3-4, RB tree
- AVL tree : lotate to balance. search, insert, delete in _O(logn)_
- 2-3 tree : each node has two or three child node, one or two value
- RB tree : only _O(1)_ structural changes after an update, but color-changes may
  propagate upward. insert, delete in _O(logn)_
    1. Root property : root is black
    2. external property : externel node is black
    3. internal property : red node's child is black
    4. depth property : every leaf node's black depth is same

## Graph
- Consists of vertices and edges
- Directed or undirected graph
- No self loops and no multiple edges
- Strongly connected : for any pair of vertices _u_ and _v_ in a directed graph, 
  there is a path from _u_ to _v_ and vice versa
- Graph representations
    - Adjacency Matrix
    - Adjacency List
    - Inverse Adjecency List
#### Depth First Search
- _O(V+E)_ time
#### Breadth First Search
- _O(V+E)_ time
#### Biconnected components
- maximum biconnected subgraph that has no articulation point
#### Minimum spanning tree
- Kruskal's MST algorithm : priority queue (minheap) + union-find
- Prim's MST algorithm : priority queue with adjacent edges
- Sollin's MST algorithm : in each step, select an edge with minimum weight
  incident to each tree
#### Shortest path
- Dijkstra's shortest path algorithm
    - linear search : _O(n^2)_
    - binary heap : _O(Elogn)_
    - not work for negative-weight edges
- Bellman-Ford shortest path algorithm
    - edges may have negative costs
    - no negative cycle
- Floyd-Warshall algorithm
    - All-pairs shortest paths
    - _O(n^3)_
#### Directed Acyclic Graph
- directed graph taht has no directed cycles
- Topological ordering

## Sorting
- _O(n^2)_ : Bubble sort, selection sort, insertion sort, shell sort
- _O(nlogn)_ : Merge sort, quick sort, heap sort
- Stable sort : Bubble, insertion, merge sort
- Unstable sort : Selection, quick, heap sort
- Bucket sort, radix sort

## Hashing
#### Static Hashing
- _O(1)_ time search on the average
- Java hashCode()
- Mid-square, folding - other ways to scramble the keys than hashCode()
- Collision handling
    - Open addressing : linear, quadratic, random probing / double hashing
    - Closed addressing : chaining
#### Dynamic hashing
- Used in DBMS
- Extendible hashing / Linear hashing

## Priority Queue

## Trie
- digital tree, radix tree, lexicographic search tree
- more flexible than BST
- faster than hashing