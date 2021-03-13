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

SIZE = sqrt(len(table))


num_of_boxes = max(TABLE_DESIGN) + 1
BOXES_SIZE = {}

for i in range(num_of_boxes):
    BOXES_SIZE[i] = TABLE_DESIGN.count(i)
