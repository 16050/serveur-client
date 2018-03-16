import socket
import traceback
import threading
import sys

address = ('localhost', 5500)
users = {}

class Server:
    def __init__(self):
        self.__s = socket.socket()
        try:
            self.__s.bind(address)
        except socket.error:
            print('Erreur de liaison {}'.format(socket.error))
        self.__s.listen(5)

    def run(self):
        print("Bienvenue sur le chat du binôme 3 série 6a.")
        print("L'écoute se fait sur {}.".format(address))
        print("Le client peut maintenant communiquer.")
        while True:
            client, add = self.__s.accept()
            y = ThreadClient(client,add)
            y.start()

    def exit(self):
        self.__s.close()

class ThreadClient(threading.Thread):
    def __init__(self,connexion,add):
        threading.Thread.__init__(self)
        self.connexion = connexion
        self.add = add
        self.commands = {'/info':self._info, '/list':self._list}

    def run(self):
        users[self.add] = [self.connexion,'','active']
        while True:
            try:
                data = self.connexion.recv(1024).decode()
                if data[0] == "/":
                    x = data.rstrip() + ' '
                    commande = x[:x.index(' ')]
                    param = x[x.index(' ')+1:].rstrip()
                    params = [param, self.add]
                    if commande in self.commands:
                        try:
                            self.commands[commande](self.connexion) if param == '' else self.commands[commande](params)
                        except Exception as e:
                            print("Erreur durant l'éxécution de la commande.")
                            print(e)
                            traceback.print_exc()
                    else:
                        print('Commande {} introuvable.'.format(commande))
                elif not data:
                    break
                else:
                    msg = "{}> {}".format(users[self.add][1], data)
                    print(msg)
                    for user in users:
                             if user != self.add:
                                users[user][0].send(msg.encode())
            except:
                print("Client coupé ou utilisateur injoignable.")
                print("Votre correspondant nous vous aime peut-être plus et s'en est allé.")
                print("Relancez le client et le serveur et tchattez avec vous-même, vous-même vous aime.")
                break

    def _info(self,client):
        self.connexion.send('/info'.encode())
        print("Pour avoir la liste, tapez sur le client [/send /liste] et regardez sur le serveur IP+Port du client.")
        print("Pour lancer une discussion privée /private IP/port/Message ")

    def _list(self,client):
        u=''
        for i in users:
            u += "{} [{}] \n".format(users[i][1], i)
        print("Utilisateurs actifs: "+ u)

if __name__=='__main__':
    try:
        Server().run()
    except:
        print("Serveur coupé ou injoignable.")


        
