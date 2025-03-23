from collections import defaultdict, Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # Generate a count dict automatically
        occur_table = Counter(tuple(row) for row in grid)
        count = 0

        # *: unpacks the 2D list to 3 lists (3 rows)
        # zip: collate all elements at the same index -> column
        for column in zip(*grid):
            count += occur_table[column]
        return count