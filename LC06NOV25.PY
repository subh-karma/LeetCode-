class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return

        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1


class Solution:
    def processQueries(self, c, connections, queries):
        dsu = DisjointSet(c)

        # Build connectivity
        for u, v in connections:
            dsu.union(u, v)

        # Build sorted sets for online stations
        groups = defaultdict(SortedSet)
        for i in range(1, c + 1):
            groups[dsu.find(i)].add(i)

        # Process queries
        ans = []
        for typ, x in queries:
            root = dsu.find(x)

            if typ == 1:  # Maintenance check
                if x in groups[root]:
                    ans.append(x)
                else:
                    ans.append(groups[root][0] if groups[root] else -1)
            else:  # Station goes offline
                groups[root].discard(x)

        return ans
