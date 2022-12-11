import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        print("get connection from : ", self.client_address)

        while True:
            # 接收客户端发来的数据
            self.data = self.request.recv(1024).decode()
            if self.data == 'exit':
                break
            self.request.sendall(self.data.upper().encode())  # 回答
        self.request.close()


server = socketserver.ThreadingTCPServer(('', 5009), MyTCPHandler)
server.serve_forever()
