# solve-1
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 ==0) and (year % 100 == 0):
        leap = True
    elif (year % 4 == 0) and (year % 100 !=0):
        leap = False
    return leap

year = int(input())
print(is_leap(year))

# solve-2
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))