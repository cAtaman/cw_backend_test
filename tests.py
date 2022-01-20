from datetime import datetime

import pytest
import tempfile
from flask_sqlalchemy import SQLAlchemy

from src import setup, main


@pytest.fixture(scope="function")
def mock_objs():
    mock_app = setup.create_app(db_path=tempfile.mkstemp()[1])
    mock_db = SQLAlchemy(mock_app.app)

    class Uuid(mock_db.Model):
        __tablename__ = 'UUIDS'
        __table_args__ = {'extend_existing': True}
        id = mock_db.Column('ID', mock_db.Integer, primary_key=True)
        timestamp = mock_db.Column('TIMESTAMP', mock_db.Text, nullable=False)
        uuid = mock_db.Column('UUID', mock_db.Text, nullable=False)

    mock_db.create_all()
    return mock_db, Uuid


def test_main_generate_uuid(mock_objs, monkeypatch):
    mock_db, Uuid = mock_objs
    monkeypatch.setattr(main, "db", mock_db)
    init = Uuid.query.all()
    # first call
    main.generate_uuid()
    first = Uuid.query.all()
    # call again
    main.generate_uuid()
    second = Uuid.query.all()
    # make sure only one record is generated per call
    assert len(init) == 0
    assert len(first) == 1
    assert len(second) == 2

    # check the values of the object created
    test_uuid = second[0]
    assert len(test_uuid.uuid) == 32
    assert datetime.now() > datetime.fromisoformat(test_uuid.timestamp)


def test_main_get(mock_objs, monkeypatch):
    # patch the func
    mock_db, Uuid = mock_objs
    monkeypatch.setattr(main, "db", mock_db)
    monkeypatch.setattr(main, "Uuid", Uuid)

    # make three calls to generate 3 uuids
    main.get()
    main.get()
    uuids, status = main.get()
    assert len(Uuid.query.all()) == 3

    # make sure the most recent is at the top of the list
    dts = [datetime.fromisoformat(key) for key in uuids]
    assert dts[0] > dts[1] > dts[2]
