from src.setup import db, ma


class Uuid(db.Model):
    __tablename__ = 'UUIDS'
    __table_args__ = {'extend_existing': True}
    id = db.Column('ID', db.Integer, primary_key=True)
    timestamp = db.Column('TIMESTAMP', db.Text, nullable=False)
    uuid = db.Column('UUID', db.Text, nullable=False)


class UuidSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Uuid
        load_instance = True
        sqla_session = db.session


db.create_all()
