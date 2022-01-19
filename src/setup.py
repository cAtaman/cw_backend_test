import os
import secrets
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# ===================================================================================
#                            INITIALISE CONSTANTS
# ===================================================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')

# ===================================================================================
#                              SETUP FLASK APP
# ===================================================================================
connex_app = connexion.App("UUID_GEN", specification_dir=BASE_DIR)
app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False  # to preserve the sort order of json objects
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# ===================================================================================
#                              INITIALISE OBJECTS
# ===================================================================================
db = SQLAlchemy(app)
ma = Marshmallow(app)

# ===================================================================================
#                               ADD SWAGGER APIs
# ===================================================================================
connex_app.add_api(os.path.join(BASE_DIR, 'spec.yaml'))
