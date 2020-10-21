def hanoi(n, f, h, t):
    print('{}n={}, f={}, h={}, t={}'.format(' '*(4-n), n, f, h, t))
    if n == 0: return
    else:
        hanoi(n-1, f, t, h)
        print('{}Move from {} to {}'.format(' '*(4-n), f, t))
        hanoi(n-1, h, f, t)

hanoi(4, 'A', 'B', 'C')