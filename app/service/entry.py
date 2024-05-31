from app.query.board import BoardQuery
from app.query.entry import EntryQuery


class EntryService:
    @staticmethod
    def get_entry(id):
        list_entries = EntryQuery.get_entry(id)

        # Find board exists
        find_board = BoardQuery.get_board_by_name(list_entries.parent)

        if find_board:
            entry_data = {
                'board_info': find_board,
                'entry': list_entries
            }

            return entry_data

        return {
            'error': True,
            'msg': 'Board not found'
        }

    @staticmethod
    def add_entry(data):
        # Find board exists
        find_board = BoardQuery.get_board_by_name(data)

        if find_board:
            EntryQuery.add_entry(data)

        return {
            'error': True,
            'msg': 'Board not found'
        }

    @staticmethod
    def update_entry(data):
        EntryQuery.update_entry(data)
        return True

    @staticmethod
    def delete_entry_by_id(id):
        EntryQuery.delete_entry_by_id(id)
        return True
