from src import app
from OpenSSL import SSL

ssl_context = SSL.Context(SSL.SSLv23_METHOD)
ssl_context.use_privatekey_file('/etc/ssl/certs/privkey.pem')
ssl_context.use_certificate_chain_file('/etc/ssl/certs/fullchain.pem')

if __name__ == '__main__':
    app.run(ssl_context=ssl_context, port=5000)
