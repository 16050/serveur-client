LABORATOIRE 3: Chat avec python.
R�alis� par EL BAKKOURY Yassine et EL HADDADI Yassine.
S�rie 6a Bin�me 3.
R�alis� le 15/03/2018.

Le dossier se compose de 3 fichiers: le README, un fichier serveur et un fichier client.
Pour pouvoir faire du peer-to-peer il suffit simplement de lancer deux clients que l'un se connecte sur l'IP et le port du correspondant. Deux m�thodes sont disponibles:
/join Ip Port
ou 
/private IP/Port/Message

La deuxi�me m�thode permet de ne pas avoir � quitter le serveur sur lequel nous sommes connect�s si nous �tions pr�alablement en communication client/serveur.
Et donc la communication client/serveur se lance simplement par /join ServeurH�te Port .
On peut essayer cela en lan�ant d'abord le serveur qui va se connecter sur localhost 5500, et ensuite lancer le client, taper[ /join localhost 5500 ] pour se connecter sur le serveur.

Pour communiquer: 
/send message
pour recevoir les messages l'un en dessous de l'autre sur la fen�tre du serveur

/send /list 
pour obtenir la liste des IP+Port (clients) sur la fen�tre du serveur.

/send /info
pour obtenir certaines informations.