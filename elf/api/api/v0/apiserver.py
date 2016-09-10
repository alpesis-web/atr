"""API Server"""

from apiserver.apiserver import api_server

if __name__ == '__main__':

    server = api_server()
    server.run(host=server.config['HOST'], port=server.config['PORT'])
