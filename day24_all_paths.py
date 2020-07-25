class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        N = len(graph)

        def goto(n, visited):
            visited.append(n)
            if n == N-1:
                self.ans.append(visited)
                return True
            else:
                for i in graph[n]:
                    v = visited[:]
                    goto(i, v)
                visited.pop()
        goto(0, [])
        return self.ans
