def rectangle(W, H = None, C = '#'):
    H = W if H is None else H
    for i in range(W):
        for j in range(H):
            print(C,end='')
        print()

if __name__ == '__main__':
    rectangle(5, C = '*')