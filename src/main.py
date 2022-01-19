import uuid
from datetime import datetime

from src.models import Uuid, UuidSchema
from src.setup import db


def generate_uuid():
    iso_dt = datetime.now().isoformat(sep=' ')
    _uuid = uuid.uuid4().hex
    dt_uuid_record = UuidSchema().load({'timestamp': iso_dt, 'uuid': _uuid})
    db.session.add(dt_uuid_record)
    db.session.commit()


def get():
    try:
        generate_uuid()
        uuid_list = UuidSchema(many=True).dump(Uuid.query.all())
    except Exception as e:
        print(e)
        return 'Something went wrong', 400
    sort_key = lambda x: datetime.fromisoformat(x[0])
    special_sort = lambda tupl: sorted(tupl, reverse=True, key=sort_key)
    uuids = dict(special_sort(map(lambda _uuid: (_uuid['timestamp'], _uuid['uuid']), uuid_list)))
    return uuids, 200

