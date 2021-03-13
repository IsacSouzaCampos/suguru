import table_infos


def print_table():
    for i in range(SIZE):
        for j in range(SIZE):
            if (j % 3) == 2:
                print(table[i][j], '    ', end='')
            else:
                print(table[i][j], ' ', end='')
        if (i % 3) == 2:
            print('\n')
        else:
            print()


def is_table_complete():
    for i in range(SIZE):
        for j in range(SIZE):
            if table[i][j] < 0:
                return False
    return True


def is_row_column_clean(i, j, v):
    for p in range(SIZE):
        if table[i][p] == v and p != j:
            return False
        if table[p][j] == v and p != i:
            return False
    return True


def is_box_clean(i, j, v):
    _i = (i // 3) * 3
    _j = (j // 3) * 3

    for r in range(_i, (_i + 3)):
        for c in range(_j, (_j + 3)):
            if table[r][c] == v:
                return False
    return True


def next_position(n):
    while n < (SIZE * SIZE):
        i = n // SIZE
        j = n % SIZE
        if table[i][j] < 0:
            return n
        n += 1
    return -1


def set_position(n):
    print('.')
    i = n // SIZE
    j = n % SIZE

    for v in range(1, ):
        if is_row_column_clean(i, j, v) and is_box_clean(i, j, v):
            table[i][j] = v
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
