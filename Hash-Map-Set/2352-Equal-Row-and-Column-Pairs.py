from collections import defaultdict, Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        occur_table = defaultdict(int)
        count = 0
        # Counting occurence of each row
        # Use Tuple as key of dict
        for row in grid:
            occur_table[tuple(row)] += 1

        # *: unpacks the 2D list to 3 lists (3 rows)
        # zip: collate all elements at the same index -> column
        for column in zip(*grid):
            count += occur_table[column]
        return count