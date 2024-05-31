from sqlalchemy.sql.expression import select, insert, update, delete

from app.models import db, Entry


class EntryQuery:
    @staticmethod
    def get_entry(entry_id):
        query = db.session.scalars(
            select(Entry).
            filter_by(id=entry_id).
            limit(1)
        ).first()
        db.session.close()
        return query

    @staticmethod
    def add_entry(data):
        db.session.execute(
            insert(Entry),
            [
                {
                    'uuid': data['uuid'],
                    'parent': data['parent'],
                    'title': data['title'],
                    'content': data['content'],
                    'entry_metadata': data['entry_metadata'],
                    'user_id': data['user_id'],
                    'created_at': data['created_at'],
                    'modified_at': data['modified_at'],
                }
            ],
        )
        db.session.commit()
        db.session.close()

    @staticmethod
    def update_entry(data):
        db.session.execute(
            update(Entry), [data],
        )
        db.session.commit()
        db.session.close()

    @staticmethod
    def delete_entry_by_id(id):
        db.session.execute(
            delete(Entry).
            where(id=id)
        )
        db.session.commit()
        db.session.close()
