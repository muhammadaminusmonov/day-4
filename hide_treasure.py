row1 = ["o", "o", "o"]
row2 = ["o", "o", "o"]
row3 = ["o", "o", "o"]

the_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

choosen_position = int(input("Where do you want to put the treasure? (row, column): "))
row = choosen_position % 10 - 1
column = choosen_position // 10 - 1
the_map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")