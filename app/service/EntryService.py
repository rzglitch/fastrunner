import time
import uuid
from app.query.BoardQuery import BoardQuery
from app.query.EntryQuery import EntryQuery


class EntryService:
    @staticmethod
    def get_entry(uuid):
        entry = EntryQuery.get_entry(uuid)

        if entry is None:
            return {
                'error': True,
                'msg': 'Entry not found'
            }

        # Find board exists
        find_board = BoardQuery.get_board(entry.parent)

        if not find_board:
            return {
                'error': True,
                'msg': 'Board not found'
            }

        entry_data = {
            'board_info': find_board,
            'entry': entry.__dict__
        }

        return entry_data

    @staticmethod
    def add_entry(form):
        if not form.validate_on_submit():
            return {
                'error': True,
                'msg': 'form validation error'
            }

        # Find board exists
        find_board = BoardQuery.get_board_by_name(
            form.data.get('board_name'))

        if not find_board:
            return {
                'error': True,
                'msg': 'Board not found'
            }

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
        return {
            'error': False,
            'msg': 'success'
        }

    @staticmethod
    def update_entry(uuid, form):
        if not form.validate_on_submit():
            return {
                'error': True,
                'msg': 'form validation error'
            }

        entry = EntryQuery.get_entry(uuid)

        if entry is None:
            return {
                'error': True,
                'msg': 'Entry not found'
            }

        data = {
            'id': entry.id,
            'title': form.data.get('title'),
            'content': form.data.get('content'),
            'entry_metadata': form.data.get('entry_metadata'),
            'modified_at': time.time(),
        }
        EntryQuery.update_entry(data)
        return {
            'error': False,
            'msg': 'success'
        }

    @staticmethod
    def delete_entry(uuid):
        entry = EntryQuery.get_entry(uuid)

        if entry is None:
            return {
                'error': True,
                'msg': 'Entry not found'
            }

        EntryQuery.delete_entry(uuid)
        return {
            'error': False,
            'msg': 'success'
        }
