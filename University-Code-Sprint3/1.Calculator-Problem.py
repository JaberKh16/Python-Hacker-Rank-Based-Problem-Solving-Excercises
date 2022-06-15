#!/bin/python3

import sys

# solve-1
# def solve(opr):
#     # Complete this function
#     return eval(opr)

# if __name__ == "__main__":
#     opr = input().strip()
#     result = solve(opr)
#     print(result)
    
    
# solve-2
def solve(opr):
    if opr[1] == "+":
        return int(opr[0]) + int(opr[2])
    else:
        return int(opr[0]) - int(opr[2])
    
if __name__ == "__main__":
    opr = input().strip()
    result = solve(opr)
    print(result)
    