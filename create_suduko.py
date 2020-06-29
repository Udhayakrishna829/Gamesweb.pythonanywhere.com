def create_sudoku():
    base = 3
    side = base*base
    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    from random import sample
    def shuffle(s): return sample(s,len(s))
    base = 3
    side = base * base
    rBase = range(base)
    rows = rs = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = cs = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    bc = [[nums[pattern(r, c)] for c in cs] for r in rs]
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0
    return [board,bc]
