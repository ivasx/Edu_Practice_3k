def rectangle(W, H = None, C = '#'):
    H = W if H is None else H
    for i in range(H):
        for j in range(W):
            print(C,end='')
        print()

if __name__ == '__main__':
    rectangle(5, C = '*')