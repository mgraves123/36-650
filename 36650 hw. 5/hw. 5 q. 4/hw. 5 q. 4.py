#https://www.w3schools.com/python/python_while_loops.asp

def num_tri(rows):
    count = 1
    row = 0
    if isinstance(rows, int)==False or rows < 0:
        return print("Invalid Input")
    for row in range(rows):
        for _ in range(row+1):
            print(count, end=' ')
            count = count + 1
        print()

num_tri(6)

