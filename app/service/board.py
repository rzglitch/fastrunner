from app.query.board import BoardQuery


class BoardService:
    @staticmethod
    def get_entry_list(name, entry_offset, search=None):
        # Search
        if search:
            return

        # Find board exists
        find_board = BoardQuery.get_board_by_name(name)

        if find_board:
            entry_limit = 20

            # Get list by board id
            list_entries = BoardQuery.get_board_entries(
                find_board.id,
                entry_offset,
                entry_limit
            )

            board_data = {
                'board_info': find_board,
                'board_list': list_entries
            }

            return board_data

        return None
