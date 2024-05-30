from sqlalchemy import Column, String, Integer, Text, BigInteger, \
    Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Board(db.Model):
    __tablename__ = 'board'

    id = Column(BigInteger().with_variant(Integer, 'sqlite'),
                primary_key=True)
    uuid = Column(String(36), index=True, unique=True, nullable=False)
    name = Column(String(64), index=True, nullable=False)
    display_name = Column(String(64), index=True, nullable=False)
    description = Column(String(191), nullable=False)


class Entry(db.Model):
    __tablename__ = 'entry'

    id = Column(BigInteger().with_variant(Integer, 'sqlite'),
                primary_key=True)
    uuid = Column(String(36), index=True, unique=True, nullable=False)
    parent = Column(BigInteger().with_variant(Integer, 'sqlite'),
                    index=True, nullable=False)
    title = Column(String(64), index=True, nullable=False)
    content = Column(Text(), nullable=False)
    entry_metadata = Column(Text(), nullable=False)
    user_id = Column(BigInteger().with_variant(Integer, 'sqlite'),
                     index=True, default=0, nullable=False)
    hits = Column(BigInteger().with_variant(Integer, 'sqlite'),
                  index=True, default=0, nullable=False)
    likes = Column(BigInteger().with_variant(Integer, 'sqlite'),
                   index=True, default=0, nullable=False)
    created_at = Column(BigInteger().with_variant(Integer, 'sqlite'),
                        index=True, nullable=False)
    modified_at = Column(BigInteger().with_variant(Integer, 'sqlite'),
                         index=True, nullable=False)
    # current unused for privacy
    deleted = Column(Boolean, index=True, default=False)


class User(db.Model):
    __tablename__ = 'user'

    id = Column(BigInteger().with_variant(Integer, 'sqlite'),
                primary_key=True)
    uuid = Column(String(36), index=True, unique=True, nullable=False)
    username = Column(String(64), index=True, nullable=False)
    password = Column(String(191), nullable=False)
    display_name = Column(String(64), index=True, nullable=False)
    group = Column(BigInteger().with_variant(Integer, 'sqlite'),
                   index=True, nullable=False)
