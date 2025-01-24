def sierpinski(n):
    triangle = ["*"]
    for i in range(n):
        new_row = []
        for row in triangle:
            spaces = " " * len(row)
            new_row.append(row + " " + row)
            triangle = [row + spaces + row for row in triangle]
        triangle += new_row
    return "\n".join(triangle)

print(sierpinski(5))
