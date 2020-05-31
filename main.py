from viridi.app import _app as app
from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run()