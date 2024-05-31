from sqlalchemy.sql.expression import select, insert

from app.models import db
from app.models import Board, Entry


class BoardQuery:
    @staticmethod
    def add_board(uuid, form):
        db.session.execute(
            insert(Board),
            [
                {
                    'uuid': uuid,
                    'name': form.data.get('name'),
                    'display_name': form.data.get('display_name'),
                    'description': form.data.get('description'),
                }
            ],
        )
        db.session.commit()
        db.session.close()

    @staticmethod
    def get_board_by_name(name):
        query = db.session.scalars(
            select(Board).
            filter_by(name=name).
            limit(1)
        ).first()
        db.session.close()
        return query

    @staticmethod
    def get_board_entries(board_id, entry_offset, entry_limit):
        query = db.session.execute(
            select(Entry).
            where(
                Entry.parent == board_id
                and Entry.status is True
                and Entry.id >= entry_offset
            ).
            order_by(Entry.id.desc()).
            limit(entry_limit)
        ).scalars().all()
        db.session.close()
        return query
