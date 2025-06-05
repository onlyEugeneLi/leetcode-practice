class SmallestInfiniteSet:

    def __init__(self):
        self.smallest_number = 1 # It's like a pointer against virtual inifite list of positive integers
        self.infinite_set = set() # Imagine this empty set contains all positive integers, but we don't have to actually assign values to it

    def popSmallest(self) -> int:
        # Not emtpy
        if self.infinite_set:
            smallest_num = min(self.infinite_set) # Don't update the virutal samllest number, just get the actual 
            self.infinite_set.remove(smallest_num)
            return smallest_num
        # Empty set: we have all positive integers in the set
        else:
            self.smallest_number += 1 # If smallest integer popped out, it will be replaced by next smallest integer
            return self.smallest_number - 1 # Return the original smallest number

    def addBack(self, num: int) -> None:
        if self.smallest_number > num:
            # Set can filter out duplicates, so if larger, just add it 
            self.infinite_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)