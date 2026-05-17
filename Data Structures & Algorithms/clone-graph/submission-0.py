"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {node: Node(node.val, [])}
        q = collections.deque([node])

        while q:
            curr = q.popleft()
            for child in curr.neighbors:
                if child not in nodes:
                    nodes[child] = Node(child.val, [])
                    q.append(child)
                nodes[curr].neighbors.append(nodes[child])
        
        return nodes[node]
            


