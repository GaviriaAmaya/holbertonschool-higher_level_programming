#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    for y in range(x):
        try:
            print(my_list[y], end="")
            z += 1
        except IndexError:
                print()
                return(z)
    print()
    return(z)
