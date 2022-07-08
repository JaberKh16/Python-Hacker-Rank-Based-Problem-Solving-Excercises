if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        nums = []
        nums.append(i*i) # appending each items multiplied with itself in list 
        for j in nums:
            print(j, end='\n')