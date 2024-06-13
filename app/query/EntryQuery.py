from sqlalchemy.sql.expression import select, insert, update, delete

from app.models import db, Entry


class EntryQuery:
    @staticmethod
    def get_entry(uuid):
        query = db.session.scalars(
            select(Entry).
            filter_by(uuid=uuid).
            limit(1)
        ).first()
        db.session.close()
        return query

    @staticmethod
    def add_entry(data):
        query = db.session.execute(
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
        return query

    @staticmethod
    def update_entry(data):
        db.session.execute(
            update(Entry), [
                {
                    'id': data['id'],
                    'title': data['title'],
                    'content': data['content'],
                    'entry_metadata': data['entry_metadata'],
                    'modified_at': data['modified_at'],
                }
            ],
        )
        db.session.commit()
        db.session.close()

    @staticmethod
    def delete_entry(uuid):
        db.session.execute(
            delete(Entry).
            where(Entry.uuid == uuid)
        )
        db.session.commit()
        db.session.close()
