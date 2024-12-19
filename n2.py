def print_pattern(N):
    for i in range(N):
    
        row = ['+'] * N
        row[i] = '=' 
        print("".join(row))  

N = 5
print_pattern(N)