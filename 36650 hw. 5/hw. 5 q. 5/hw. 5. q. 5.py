def num_stars(rows):
    spaces = rows-1
    row = 0
    if isinstance(rows, int)==False or rows < 0:
        return print("Invalid Input")
    for row in range(rows):
        print(' '*spaces, end=' ')
        spaces = spaces - 1
        for _ in range(row+1):
            print('*', end=' ')
        print()

print(num_stars(4))