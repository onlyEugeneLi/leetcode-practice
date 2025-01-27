'''
Link to problem: https://www.hackerrank.com/challenges/array-left-rotation/problem
'''

def rotateLeft(d, arr):
    # # Self attempt: brute force
    # res = [0] * len(arr)
    # print(f"Input -- {arr}")
    # for i in range(len(arr)):
    #     res[i - d] = arr[i]
    # print(f"Rotated -- {res}")
    # return res

    # Solution
    arr[:] = arr[d:] + arr[:d]
    return arr

d = 2 
# d = 4
arr = [1, 2, 3, 4, 5]
result = rotateLeft(d, arr)

print(result)