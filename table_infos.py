from math import sqrt


TABLE_DESIGN = [0, 0, 0, 1, 2, 2, 3, 3,
                0, 4, 4, 1, 2, 2, 3, 3,
                4, 4, 1, 1, 2, 5, 5, 3,
                4, 6, 6, 1, 7, 7, 5, 5,
                8, 8, 6, 6, 7, 9, 9, 5,
                10, 8, 8, 6, 7, 11, 9, 9,
                10, 10, 8, 12, 7, 11, 11, 9,
                10, 10, 12, 12, 12, 12, 11, 11]

x = -1
table = [x, x, x, 3, x, x, 2, x,
         4, x, x, x, x, x, x, x,
         x, 2, x, x, x, x, x, x,
         x, 1, 5, x, x, 1, 5, x,
         x, 2, x, x, x, x, x, x,
         x, x, x, x, 4, x, x, 4,
         x, x, x, x, x, 3, x, x,
         x, 5, x, x, x, 5, x, x]

SIZE = int(sqrt(len(table)))


# aqui é criada uma nova tabela com novas laterais valendo -2
_SIZE = SIZE + 2
editable_table = [-2 for _ in range(_SIZE)]
new_table_design = [-2 for _ in range(_SIZE)]

for i in range(SIZE):
    editable_table.append(-2)
    new_table_design.append(-2)

    [editable_table.append(table[(i * SIZE) + j]) for j in range(SIZE)]
    [new_table_design.append(TABLE_DESIGN[(i * SIZE) + j]) for j in range(SIZE)]

    editable_table.append(-2)
    new_table_design.append(-2)

[editable_table.append(-2) for _ in range(_SIZE)]
[new_table_design.append(-2) for _ in range(_SIZE)]

table = editable_table
TABLE_DESIGN = new_table_design
SIZE = _SIZE


num_of_boxes = max(TABLE_DESIGN) + 1
BOXES_SIZE = {}
BOXES_POSITIONS = {}

for i in range(num_of_boxes):
    BOXES_SIZE[i] = TABLE_DESIGN.count(i)
    BOXES_POSITIONS[i] = []

for i in range(len(TABLE_DESIGN)):
    if TABLE_DESIGN[i] > -1:
        BOXES_POSITIONS[TABLE_DESIGN[i]].append(i)
