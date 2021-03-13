from table_infos import SIZE, BOXES_SIZE, TABLE_DESIGN, table


def print_table():
    for i in range(SIZE):
        for j in range(SIZE):
            if (j % 3) == 2:
                print(table[(i * SIZE) + j], '    ', end='')
            else:
                print(table[(i * SIZE) + j], ' ', end='')
        if (i % 3) == 2:
            print('\n')
        else:
            print()


def is_table_complete():
    for i in range(SIZE):
        for j in range(SIZE):
            if table[(i * SIZE) + j] < 0:
                return False
    return True


def is_neighborhood_clean(i, j, v):
    s = SIZE - 1
    if i == 0 and j == 0:
        # topo esquerdo
        pass
    elif i == 0 and j == s:
        # topo direito
        pass
    elif i == s and j == s:
        # fundo direito
        pass
    elif i == s and j == 0:
        # fundo esquerdo
        pass
    elif i == 0:
        # topo
        pass
    elif j == s:
        # direita
        pass
    elif i == s:
        # fundo
        pass
    elif j == 0:
        # esquerda
        pass


def is_box_clean(i, j, v):
    _i = (i // 3) * 3
    _j = (j // 3) * 3

    for r in range(_i, (_i + 3)):
        for c in range(_j, (_j + 3)):
            if table[(r * SIZE) + c] == v:
                return False
    return True


def next_position(n):
    while n < (SIZE * SIZE):
        if table[n] < 0:
            return n
        n += 1
    return -1


def set_position(n):
    print('.')
    i = n // SIZE
    j = n % SIZE

    for v in range(1, BOXES_SIZE):
        if is_neighborhood_clean(i, j, v) and is_box_clean(i, j, v):
            table[n] = v
            _next = next_position(n)
            if _next < 0:
                return True
            if set_position(_next):
                return True

    table[i][j] = -1
    return False


if __name__ == '__main__':
    set_position(next_position(0))
    print_table()
