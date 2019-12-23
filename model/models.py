from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, TEXT, INTEGER, DATETIME

Base = declarative_base()


def _create_session_class(db_path):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine(db_path + "?check_same_thread=False")
    global Session
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)


def open_session(db_path):
    from sqlalchemy.orm import scoped_session
    global Session
    if Session is None:
        _create_session_class(db_path)

    return scoped_session(Session)


class FileInfoBase(object):
    path = Column(TEXT, primary_key=True)
    size = Column(INTEGER)
    date_created = Column(DATETIME)
    date_modified = Column(DATETIME)
    date_taken = Column(DATETIME)
    camera = Column(TEXT)
    width = Column(INTEGER)
    height = Column(INTEGER)
    bit_dept = Column(INTEGER)
    horizontal_resolution = Column(TEXT)
    vertical_resolution = Column(TEXT)


class FileInfo(Base, FileInfoBase):
    """
    A table for existing files and their data
    """
    __tablename__ = "file_info"


class FileInfoDumpster(Base, FileInfoBase):
    """
    A table for deleted files
    """
    __tablename__ = "file_info"
