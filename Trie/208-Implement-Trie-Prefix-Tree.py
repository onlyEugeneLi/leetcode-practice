class Trie:
    
    class Node:
        def __init__(self):
            self.nodes = [None] * 26 # All 26 letters
            self.is_end = False # Flag -- is there a complete word?

    def __init__(self) -> None:
        self.root = self.Node()

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word:
            index = ord(char) - ord('a')

            ''' Check if character already exists in the root '''
            if current_node.nodes[index] is None:
                current_node.nodes[index] = self.Node()
            
            ''' Move to children '''
            current_node = current_node.nodes[index]
        
        # At the end of a word, set the flag 'is_end' to true
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            index = ord(char) - ord('a')
            current_node = current_node.nodes[index]
            ''' not a node now, can't use index and attribute '''
            if current_node is None:
                return False
            
        return current_node.is_end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            current_node = current_node.nodes[index]
            ''' not a node now, can't use index and attribute '''
            if current_node is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)