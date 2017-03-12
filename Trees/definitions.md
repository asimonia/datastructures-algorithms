##NODE
A node is a fundamental part.  It has a name called the "key".
A node also has additional info called the "payload".

##EDGE
An edge connects two nodes to show the that there is a
relationship between them.  Every node (except the root) is
connected by exactly one incoming edge from another node.

##ROOT
The root of the tree is the only node that has no incoming edges.

##PATH
An ordered list of nodes that are connected by edges.
For example, Mammal → Carnivora → Felidae → Felis

##CHILDREN
The set of nodes c that have incoming edges from the same node
are said to be the children of that node. <li> would be the children of <ul>

##PARENT
A node is the parent of all the nodes it connects to with outgoing edges.
<ul> would be the parent of <li>

##SIBLING
Nodes in the tree that are children of the same parent are said to be siblings.
The nodes etc/ and usr/ are siblings in the filesystem tree.

##SUBTREE
A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.

##LEAF NODE
A leaf node is a node that has no children.

##LEVEL
The level of a node nn is the number of edges on the path from the root node to nn

##HEIGHT
The height of a tree is equal to the maximum level of any node in the tree. 




##Definition One: A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following properties:

#One node of the tree is designated as the root node.

#Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n.

#A unique path traverses from the root to each node.

#If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

