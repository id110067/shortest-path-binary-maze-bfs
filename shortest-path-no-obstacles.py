import utils
import collections
from collections import defaultdict
import heapq

class Solution(object):
    def leastStepQ1a(self, grid):
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
        
        # initialise q with [(step count, x-coordinate, y-coordinate)]
        # initialise visited with (x-coordinate, y-coordinate)
        q = collections.deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0)) 

        # BFS Algorithm
        # loop till q is not empty                    
        while q:                  
            steps, cur_x, cur_y = q.popleft()

            # check if the destination coordinates have been reached
            if cur_x == m-1 and cur_y == n-1:
                return steps

            # for each of the current matrix grid cell’s adjacent cells, if the cells are empty, 
            # we append the respective along with the step count (increased by 1 unit) to the collections.deque() (q), 
            # and also add the coordinates to the set (visited).
            for r, c in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                if (r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 0 and (r,c) not in visited):
                    visited.add((r,c))
                    q.append((steps + 1,r,c))
        return -1       
        

if __name__ == '__main__':
    utils.A3_P1_1a_score()

