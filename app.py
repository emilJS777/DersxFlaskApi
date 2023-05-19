from src import app
from flask_sslify import SSLify

sslify = SSLify(app)
if __name__ == '__main__':
    app.run()
