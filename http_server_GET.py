from http.server import BaseHTTPRequestHandler
from urllib import parse
import os
import mimetypes

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        # message_parts = [
        #     'CLIENT VALUES:',
        #     'client_address={} ({})'.format(
        #         self.client_address,
        #         self.address_string()),
        #     'command={}'.format(self.command),
        #     'path={}'.format(self.path),
        #     'real path={}'.format(parsed_path.path),
        #     'query={}'.format(parsed_path.query),
        #     'request_version={}'.format(self.request_version),
        #     '',
        #     'SERVER VALUES:',
        #     'server_version={}'.format(self.server_version),
        #     'sys_version={}'.format(self.sys_version),
        #     'protocol_version={}'.format(self.protocol_version),
        #     '',
        #     'HEADERS RECEIVED:',
        # ]
        # for name, value in sorted(self.headers.items()):
        #     message_parts.append(
        #         '{}={}'.format(name, value.rstrip())
        #     )
        # message_parts.append('')
        # message = '\r\n'.join(message_parts)
        requestPath = parsed_path.path
        print("-url->",requestPath)
        if requestPath == '/': 
            requestPath = "index.html"
        if requestPath.find (".html") == len(requestPath)-5:
            fullPath = "source/html/"+requestPath
            # print(fullPath)
            if os.path.exists(fullPath) == True:
                self.send_response(200)
                self.send_header('Content-Type','text/html; charset=utf-8')
                self.end_headers()
                f=open(fullPath,'r')
                fData=f.read()
                self.wfile.write(fData.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-Type','text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write("Page not found.".encode('utf-8'))
        elif requestPath.find ("/image/") != -1:
            fullPath = "source/"+requestPath
            print(fullPath)
            if os.path.exists(fullPath) == True:
                print(mimetypes.guess_type(fullPath)[0])
                self.send_response(200)
                self.send_header('Content-Type',mimetypes.guess_type(fullPath)[0])
                self.end_headers()
                f=open(fullPath,'rb')
                fData=f.read()
                self.wfile.write(fData)
            else:
                self.send_response(404)
                self.send_header('Content-Type','text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write("Page not found.".encode('utf-8'))
        # self.send_response(200)
        # self.send_header('Content-Type','text/html; charset=utf-8')
        # self.end_headers()
        # # f=open('HTML1.html','r')
        # # fData=f.read()
        # self.wfile.write("fData".encode('utf-8'))
        # self.send_header('Content-Type','image/jpeg')
        # self.end_headers()
        # f=open('ceE3LtadPGMrY.jpg','rb')
        # fData=f.read()
        # self.wfile.write(fData)
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()