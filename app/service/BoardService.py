import uuid
from app.query.BoardQuery import BoardQuery


class BoardService:
    @staticmethod
    def add_board(form):
        if not form.validate_on_submit():
            return {
                'error': True,
                'msg': 'form validation error'
            }

        # Find board exists
        find_board = BoardQuery.get_board_by_name(
            form.data.get('name'))

        if find_board:
            return {
                'error': True,
                'msg': 'Board already exists'
            }

        gen_uuid = str(uuid.uuid4())
        BoardQuery.add_board(gen_uuid, form)
        return {
            'error': False,
            'msg': 'success'
        }

    @staticmethod
    def get_entry_list(name, entry_offset, search=None):
        # Search
        if search:
            return

        # Find board exists
        find_board = BoardQuery.get_board_by_name(name)

        if not find_board:
            return {
                'error': True,
                'msg': 'Board not found'
            }

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
