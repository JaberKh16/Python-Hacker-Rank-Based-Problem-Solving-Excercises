if __name__ == '__main__':
    a = int(input()) # read integer a
    b = int(input()) # read integer b
    
    def integer_div(a, b):
        print(f'{a//b}', end="\n")
    def float_div(a, b):
        print(f'{a/b}', end="\n")
        
    integer_div(a, b)
    float_div(a, b)