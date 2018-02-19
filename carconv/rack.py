from board import Board


class Rack:

    def __init__(self, host, rack_address, boards):
        """

        :param host:
        :param rack_address:
        :param boards:
        """
        self.__rack_address = rack_address
        self.__boards = {}
        for board_name in boards:
            board_address = boards[board_name]
            self.__boards[board_name] = Board(host, board_address)

    def get_board(self, name):
        return self.__boards[name]

    def stop(self):
        for name, board in self.__boards.iteritems():
            board.stop()
