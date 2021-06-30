#Your Code Here
# Solve 4*ABCD == DCBA
def nested_nest():

    for A in range(1, 9):
        for B in range(0, 9):
            for C in range(0, 9):
                for D in range(1, 9):
                    if 4*( 1000 * A + 100 * B + 10 * C + D) == \
                        (A + 10 * B + 100 * C + 1000 * D):
                        print("a=", A, "b=", B, "c=", C, "d=", D)
    return
    
nested_nest()