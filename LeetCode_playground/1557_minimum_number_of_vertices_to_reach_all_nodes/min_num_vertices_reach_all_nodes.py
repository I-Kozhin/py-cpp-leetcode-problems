"""Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [
fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique
solution exists.

Notice that you can return the vertices in any order.
"""

from typing import List
from collections import defaultdict

TEST_CASES = [
    [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]],  # test case 1
    [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]  # test case 2
]

N = [
    6,  # test case 1
    5  # test case 2
]


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """

        :param n: The number of vertices in the graph. It ranges from 2 to 10^5.
        :param edges: The list of edges in the graph. Each edge is represented by a pair (fromi, toi) where
        fromi and toi are distinct integers between 0 and n-1. The length of the edges list is between 1 and the
        minimum of 10^5 and n * (n - 1) / 2.
        :return: The smallest set of vertices from which all nodes in the graph are reachable

        >>> findSmallestSetOfVertices(n=N[0], edges=TEST_CASES[0])
        [0,3]
        >>> findSmallestSetOfVertices(n=N[1], edges=TEST_CASES[1])
        [0,2,3]
        """

        def dfs(g, c, vis, res):
            vis[c] = True
            for adj in g[c]:
                if not vis[adj]:
                    dfs(g, adj, vis, res)
                # adj can be visited by current vertex so we dont have to add adj in res
                elif adj in res:
                    res.remove(adj)

        # Make a adjecency list
        g = defaultdict(list)
        for e in edges:
            u, v = e
            g[u].append(v)

        res = set()
        vis = [False] * n
        for i in range(n):
            if not vis[i]:
                dfs(g, i, vis, res)
                # add vertex from which we start traversing
                res.add(i)
        return list(res)


def main():
    solution = Solution()
    # By using zip(N, TEST_CASES), the corresponding elements of N and TEST_CASES will be paired together,
    # and you can iterate over them simultaneously.
    for n, test_case in zip(N, TEST_CASES):
        result = solution.findSmallestSetOfVertices(n, test_case)
        print(result)


if __name__ == "__main__":
    main()
