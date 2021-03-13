from table_infos import SIZE, _SIZE, BOXES_SIZE, BOXES_POSITIONS, TABLE_DESIGN, table


def print_table():
    for i in range(1, _SIZE - 1):  # 1, _SIZE - 1
        for j in range(1, _SIZE - 1):
            if table[(i * _SIZE) + j] >= 0:
                print('', table[(i * _SIZE) + j], '    ', end='')
            else:
                print(table[(i * _SIZE) + j], '    ', end='')
        print()


def is_table_complete():
    for i in range(SIZE):
        for j in range(SIZE):
            if table[(i * SIZE) + j] < 0:
                return False
    return True


def is_neighborhood_clean(i, j, v):
    for _i in range((i - 1), (i + 2)):
        for _j in range((j - 1), (j + 2)):
            # print(i, j, '-', _i, _j)
            if table[(_i * _SIZE) + _j] == v:
                return False
    return True


def is_box_clean(n, v):
    for i in BOXES_POSITIONS[TABLE_DESIGN[n]]:
        # print(i, end=' ')
        if table[i] == v:
            return False
    return True


def next_position(n):
    while n < (_SIZE * _SIZE):
        if table[n] == -1:
            return n
        n += 1
    return -1


def set_position(n):
    print('.')
    i = (n // _SIZE)
    j = (n % _SIZE)

    # print(n, TABLE_DESIGN[n])
    # print_table()
    # print('*'*40)

    for v in range(1, BOXES_SIZE[TABLE_DESIGN[n]] + 1):
        if is_neighborhood_clean(i, j, v) and is_box_clean(n, v):
            table[n] = v
            _next = next_position(n)
            if _next < 0:
                return True
            if set_position(_next):
                return True

    # print('settou pra -1', (i * SIZE) + j, n)
    table[n] = -1
    return False


if __name__ == '__main__':
    set_position(next_position(0))
    print_table()
