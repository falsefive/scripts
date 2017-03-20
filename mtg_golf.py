w = ['W','U','B','R','G']

def is_ally(c):
    return w.index(c[1]) - w.index(c[0]) == 1 or w.index(c[1]) - w.index(c[0]) == 4
