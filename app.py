from src import app

if __name__ == '__main__':
    app.run(ssl_context=('/etc/letsencrypt/live/skillx.am/cert.pem', '/etc/letsencrypt/live/skillx.am/privkey.pem'))
