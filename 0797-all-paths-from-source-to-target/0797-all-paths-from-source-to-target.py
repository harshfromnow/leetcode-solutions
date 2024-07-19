class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            path.append(node)  
            if node == len(graph) - 1:
                result.append(path.copy())  
            else:
                for next_node in graph[node]:
                    dfs(next_node, path)  
            path.pop()  
        result = []
        dfs(0, [])
        return result