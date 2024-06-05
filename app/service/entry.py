import time
import uuid
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
    def add_entry(form):
        if form.validate_on_submit():
            # Find board exists
            find_board = BoardQuery.get_board_by_name(
                form.data.get('board_name'))

            if find_board:
                gen_uuid = str(uuid.uuid4())
                data = {
                    'uuid': gen_uuid,
                    'parent': find_board.id,
                    'title': form.data.get('title'),
                    'content': form.data.get('content'),
                    'entry_metadata': form.data.get('entry_metadata'),
                    'user_id': 0,
                    'created_at': time.time(),
                    'modified_at': time.time(),
                }
                EntryQuery.add_entry(data)
                return True

        return False

    @staticmethod
    def update_entry(data):
        EntryQuery.update_entry(data)
        return True

    @staticmethod
    def delete_entry_by_id(id):
        EntryQuery.delete_entry_by_id(id)
        return True
