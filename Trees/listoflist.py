myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])

def BinaryTree(r):
	"""Constructs a list with a root node and two empty sublists
	for the children.
	"""
	return [r, [], []]


def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root


def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
