import socketserver
from os.path import commonprefix
words = {'how are you?': 'Fine,thank you.',
         'how old are you?': '10',
         'what is your name?': 'xiaoluo',
         'where do you work?': 'Lavatory',
         'whats your favourite?': 'majsoul',
         'areYouManAWoman?': 'man',
         'whatDoYouLikeToEat?': 'cake',
         'bye': 'Bye'}


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        print("get connection from : ", self.client_address)

        while True:
            # 接收客户端发来的数据
            self.data = self.request.recv(1024).decode()
            if not self.data:
                break
            if self.data == 'exit':
                break
            m = 0
            key = ''
            for k in words.keys():
                self.data = ' '.join(self.data.split())  # 删除多余的空白字符
                # 与某个“键”非常接近，就直接返回
                if len(commonprefix([k, self.data])) > len(k)*0.7:
                    key = k
                    break  # 跳出for,表示找到对应的问题
                # 选择一个重合度较高的“键”
                length = len(set(self.data.split()) & set(k.split()))
                if length > m:
                    m = length
                    key = k
            self.request.sendall(words.get(key, 'Sorry.').encode())  # 回答
        self.request.close()


server = socketserver.ThreadingTCPServer(('', 5007), MyTCPHandler)
server.serve_forever()
