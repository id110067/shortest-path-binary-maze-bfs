import utils
import collections
from collections import defaultdict
import heapq


class Solution(object):
    def leastStepQ1b(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0]) # don't remove this line
        # Please code below

        # check if the is only 1 cell in the matrix grid
        if m == 1 and n == 1:
            return 0
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        # initialise q with [(step count, x-coordinate, y-coordinate, obstacle-elimination-allowed)]
        # initialise visited with (x-coordinate, y-coordinate, obstacle-elimination-allowed)
        q = collections.deque([(0, 0, 0, 1)])
        visited = set()
        visited.add((0, 0, 1))
        # BFS Algorithm
        # loop till q is not empty 
        while q:
            step, cur_x, cur_y, obs = q.popleft()
            # check if the destination coordinates have been reached
            if cur_x == m-1 and cur_y == n-1: 
                return step
            # for each of the current matrix grid cell’s adjacent cells
            for r, c in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                # 1. if the cell is not empty, and, 
                # 2. obstacle elimination allowed count > 0, and, 
                # 3. we have not yet visited the cell, 
                if (r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1 and obs > 0 and (r, c, obs) not in visited):
                    # a. we append the respective matrix cell grid coordinates, the step count (increased by 1 unit) along with the obstacle eliminations 
                    #    allowed after the current step (decreased by 1 unit) to the collections.deque() (q), and, 
                    # b. add the coordinates as well the obstacle eliminations allowed after the current step (decreased by 1 unit) to the set (visited).
                    visited.add((r, c, obs - 1))
                    q.append((step + 1, r, c, obs - 1))
                # 4. else, if the cell is empty, and,
                # 5. we have not yet visited the cell,
                elif (r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 0 and (r, c, obs) not in visited):
                    # a. we append the respective matrix cell grid coordinates, the step count (increased by 1 unit) along with the obstacle eliminations 
                    #    allowed after the current step (no change) to the collections.deque() (q), and, 
                    # b. add the coordinates as well the obstacle eliminations allowed after the current step (no change) to the set (visited).
                    visited.add((r, c, obs))
                    q.append((step + 1, r, c, obs))
        return -1


if __name__ == '__main__':
    utils.A3_P1_1b_score()

