from sqlalchemy.sql.expression import select

from app.models import db, Board, Entry


class BoardQuery:
    @staticmethod
    def get_board_by_name(name):
        return db.session.scalars(
            select(Board).
            filter_by(name=name).
            limit(1)
        ).first()

    @staticmethod
    def get_board_entries(id, entry_offset, entry_limit):
        db.session.execute(
            select(Entry).
            where(
                Entry.parent == id
                and Entry.status is True
                and Entry.id >= entry_offset
            ).
            order_by(Entry.id.desc()).
            limit(entry_limit)
        ).scalars().all()
