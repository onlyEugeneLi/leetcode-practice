from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: 
                node.children[c] = TrieNode()
            node = node.children[c]
            # Save matched product names 
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c]
            # Go to the end of prefix to check the matched word list
        return node.words
            
class Solution_trie:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        # Populate the trie
        for word in products: 
            trie.add_word(word)

        ans, prefix = [], ''

        for char in searchWord:
            prefix += char 
            ans.append(trie.find_word_by_prefix(prefix))
        return ans    
    
class Solution_binary_search:
    # Reference: https://authorslog.com/@dare2solve/1268-search-suggestions-system-yv5CR0BuC8
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        result = []
        left, right = 0, len(products) - 1

        # Sort the products
        products.sort()
        # Narrow down the left and right pointers so that all products between them start with this prefix
        for i in range(len(searchWord)):
            c = searchWord[i]
            matched = []

            while left <= right and (len(products[left]) <= i or products[left][i] < c):
                '''
                Skips products that are:
                    - Too short to match the prefix (len(products[left]) <= i)
                    - Or whose character at position i is less than the current character c (i.e., not matching the prefix)
                '''
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] > c):
                '''
                skips products that:
                    - Are too short
                    - Or whose character at position i is greater than c (i.e., also not matching the prefix)
                '''
                right -= 1

            '''
            All products between left and right (inclusive) match the current prefix

            Take up to 3 of them
            '''
            for j in range(3):
                if left + j <= right:
                    matched.append(products[left + j])
            result.append(matched)

        return result