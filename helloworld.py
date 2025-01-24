import math

def draw_spiral(size):
    for i in range(size):
        for j in range(size):
            if math.isclose(math.fmod(i + j, 2), 0, abs_tol=0.3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

draw_spiral(5)
