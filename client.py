import socket
import sys
import threading
import traceback

class Client:
    def __init__(self, host='localhost', port=5000, name='client'):
        self.__s = socket.socket()
        self.__s.settimeout(0.5)
        self.__s.bind((host, port))
        self.__s_UDP = socket.socket(type=socket.SOCK_DGRAM)
        self.__s_UDP.bind((host, port))
        self.__name = name
        print('Écoute sur {}:{}'.format(host, port))
        
    def run(self):
        handlers = {
            '/exit': self._exit,
            '/quit': self._quit,
            '/join': self._join,
            '/send': self._send,
            '/list': self._list,
            '/info': self._info,
            '/private': self._private
        }
        self.__running = True
        self.__address = None

        while self.__running:
            line = sys.stdin.readline().rstrip() + ' '
            command = line[:line.index(' ')]
            param = line[line.index(' ')+1:].rstrip()
            if command in handlers:
                try:
                    handlers[command]() if param == '' else handlers[command](param)
                except:
                    print("Erreur lors de l'exécution de la commande.")
            else:
                print('Commande inconnue:', command)
    
    def _exit(self):
        self.__running = False
        self.__address = None
        self.__s.close()
    
    def _quit(self):
        self.__s.send("Client déconnecté".encode())
        self.__address = None
    
    def _join(self, param):
        if self.__name=='client':
            self.__name = input("Choisir un nom d'utilisateur: ")
        tokens = param.split(' ')
        if len(tokens) == 2:
            try:
                self.__address = (tokens[0], int(tokens[1]))
                self.__s.connect(self.__address)
                print('Connecté à {}:{}'.format(*self.__address))
            except OSError:
                print("Erreur lors de l'envoi du message.")
    
    def _send(self, param):
        if self.__address is not None:
            try:
                message = param.encode()
                totalsent = 0
                while totalsent < len(message):
                    sent = self.__s.sendto(message[totalsent:], self.__address)
                    totalsent += sent
            except OSError:
                print('Erreur lors de la réception du message.')
    
    def _receive(self):
        while self.__running:
            try:
                data, address = self.__s.recvfrom(1024)
                print(data.decode())
            except s.timeout:
                pass
            except OSError:
                return

    def _list(self):
        self.__s.send('/list'.encode())

    def _info(self):
        self.__s.send('/info'.encode())

    def _private(self, x):
        y = x.split("/")
        try:
            msg = y[2].encode()
            totalsent = 0
            while totalsent < len(msg):
                sent = self.__s_UDP.sendto(msg[totalsent:], (y[0], int(y[1])))
                totalsent += sent
        except OSError:
            print('Erreur lors de la réception du message.')

    def _rcvprivate(self):
        while s.__running:
            try:
                x = self.__s_UDP.recv(1024).decode()
                print(x)
            except s.timeout:
                traceback.print_exc()
            except OSError:
                traceback.print_exc()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        Client(sys.argv[1], int(sys.argv[2])).run()
    else:
        Client().run()
