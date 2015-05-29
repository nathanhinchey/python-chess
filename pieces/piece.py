class Piece:
    def __init__(self, options):
        self.color = options['color']
        self.board = options['board']
        self.pos = options['pos']

        board.add_piece(self, pos)

    def render():
        symbols[color]

    def valid_moves():
        _valid_moves = []
        for to_pos in moves():
            if !move_into_check(to_pos):
                _valid_moves.push(to_pos)

    def move_into_check():
        test_board = board.dup()
        test_board.move_piece(pos, to_pos)
        test_board.in_check?(self.color)
