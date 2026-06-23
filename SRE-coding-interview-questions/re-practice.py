import re
class StringList(list):
    def __init__(self, text: str, delimiter: str = ', ') -> None:
        super().__init__(text.split(delimiter))

    def has_match(self, pattern: str) -> bool:
        return any(re.search(pattern, item) for item in self)
    

class LargeStringList():
    def __init__(self, text: str, delimiter: str = ', ') -> None:
        self._raw = text
        self._delimiter = delimiter
    
    def __iter__(self):
        for item in self._raw.split(self._delimiter):
            yield item
    
    def has_match(self, pattern: str) -> bool:
        return any(re.match(pattern, item) for item in self)

if __name__ == '__main__':
    str1 = 'football, car, basketball, bar'
    test = StringList(str1)
    pattern_1 = '.*ar'
    pattern_2 = r'\bfood'
    assert test.has_match(pattern_1), "Expected output: true"
    assert not test.has_match(pattern_2), "Expected output: false"
    print("All test cases passed!")
