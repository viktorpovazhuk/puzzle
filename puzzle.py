"""Validate puzzle start board"""

def validate_board(board: list) -> bool:
    """
    Check if the board is ready for a game.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "3      **", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "3   1  **", "  2  ****"])
    False
    """
    return check_rows(board) and check_cols(board) and check_block(board)


def check_rows(board: list) -> bool:
    """
    Check if board has unique numbers in rows.

    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "311    **", "  2  ****"])
    False
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "31     **", "  2  ****"])
    True
    """
    for row in board:
        clear_row = row.replace(" ", "").replace("*", "")
        if len(clear_row) != len(set(clear_row)):
            return False
    return True


def check_cols(board: list) -> bool:
    """
    Check if board has unique numbers in columns.

    >>> check_cols(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "3  1   **", "  2  ****"])
    False
    >>> check_cols(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "3      **", "  2  ****"])
    True
    """
    for i in range(len(board[0])):
        col = []
        for row in board:
            if row[i] != " " and row[i] != "*":
                col.append(row[i])
        if len(col) != len(set(col)):
            return False
    return True


def check_block(board: list) -> bool:
    """
    Check if board has unique numbers in color bloks.

    >>> check_block(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "36     **", "  2  ****"])
    False
    >>> check_block(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
    "     9 5 ", " 6  83  *", "3      **", "  2  ****"])
    True
    """
    for i in range(len(board) - 5 + 1):
        corn = (len(board) - 1 - i, i)
        uniq_nums = []
        for col in range(5):
            cur_num = board[corn[0]][corn[1] + col]
            if cur_num == " ":
                continue
            if cur_num in uniq_nums:
                return False
            else:
                uniq_nums.append(cur_num)
        for row in range(4, 0, -1):
            cur_num = board[corn[0] - row][corn[1]]
            if cur_num == " ":
                continue
            if cur_num in uniq_nums:
                return False
            else:
                uniq_nums.append(cur_num)
        # print(uniq_nums)
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    board = ["**** ****", "***1 ****", "**  3****", "* 4 1****",
             "     9 5 ", " 6  83  *", "3      **", "  2  ****"]
    print(validate_board(board))
