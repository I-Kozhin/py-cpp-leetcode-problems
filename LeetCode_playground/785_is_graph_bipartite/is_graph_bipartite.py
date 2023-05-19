from collections import deque
from typing import List

TEST_CASES = [
    [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],  # test case 1
    [[1, 3], [0, 2], [1, 3], [0, 2]]  # test case 2
]


class Solution:
    def isBipartite(self, gr: List[List[int]]) -> bool:
        """

        :param gr: The input graph is an undirected graph with n vertices, where each vertex u has unique and
        non-repeating values in its adjacent vertex list graph[u], and if vertex u is connected to vertex v,
        then vertex v is also connected to vertex u.
        :return: Return true if and only if it is bipartite

        >>> isBipartite(gr=TEST_CASES[0])
        False
        >>> isBipartite(gr=TEST_CASES[1])
        True
        """
        n = len(gr)
        colour = [0] * n

        for node in range(n):
            if colour[node] != 0:
                continue

            q = deque()
            q.append(node)
            colour[node] = 1

            while q:
                cur = q.popleft()

                for ne in gr[cur]:
                    if colour[ne] == 0:
                        colour[ne] = -colour[cur]
                        q.append(ne)
                    elif colour[ne] != -colour[cur]:
                        return False

        return True


def main():
    solution = Solution()
    for test_case in TEST_CASES:
        result = solution.isBipartite(test_case)
        print(result)


if __name__ == "__main__":
    main()
