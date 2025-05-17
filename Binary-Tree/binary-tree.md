# Binary Tree Problems

## Data structure

A *queue* of *lists*: to contain multiple types of information, such as type, distance, node etc 

## Recursion

> Decide if you need recursion: if your function breaks an input apart to get to a solution

2 cases:
1. A base/terminating case which ends the recursive calls
1. A recursive case which calls the function again on a subset of the original input or sometimes a new set of inputs.

Code example:
```
void test(int value) {
    if (value == 0) return;
    
    test(--value);
}

int main() {
    test(3);
    return 0;
}
```

The call stack looks like....


```
Stack: Empty...
Stack: Main (main method is added onto the stack)
Stack: Main
       test(3) (test is added onto the stack)
Stack: Main
       test(3)
       test(2)
Stack: Main
       test(3)
       test(2)
       test(1)
Stack: Main
       test(3)
       test(2)
       test(1)
       test(0)

// Notice at this point we return (when value == 0)

Stack: Main
       test(3)
       test(2)
       test(1)
       test(0) // POP!
Stack: Main
       test(3)
       test(2)
       test(1) // POP!
Stack: Main
       test(3)
       test(2) // POP!
Stack: Main
       test(3) (test is added onto the stack) // POP!
Stack: Main...
```

Recursion is nothing but a fancy way of adding method calls onto the call stack. The callstack is just a stack. Like the datastructure or a stack of books. The call stack tracks method calls. <u>A method call gets added onto the stack, executed, and then popped off the stack after returning...</u> with recursion a method is added onto the stack, executed, and then a method is added onto the stack, etc. [Reference](https://www.reddit.com/r/learnprogramming/comments/kax4jf/comment/gfd90fg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
