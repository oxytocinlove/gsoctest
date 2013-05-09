"""traverses a tree in post-order and names higher-order nodes
after the set of nodes that are its children
"""
from Bio import Phylo
def walk_through(n, nodes):
	if n.is_terminal():
		nodes.append(n)
	else:
		n.name = ""
		for c in n.clades:
			walk_through(c, nodes)
			if c.name is not None:
				n.name += c.name
		nodes.append(n)	
	return nodes
tree = Phylo.read("test.newick", "newick")
root = tree.clade
nodes = []
out = walk_through(root, nodes)
for i in out:
	print i




