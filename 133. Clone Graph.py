class Node:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Hash map to store the mapping between original and cloned nodes
        visited = {}
        
        # Helper function to perform DFS and clone the graph
        def dfs(node):
            if node in visited:
                return visited[node]
            
            # Create a new node for the current node
            clone_node = Node(node.val)
            visited[node] = clone_node
            
            # Clone all the neighbors
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        return dfs(node)
