LABORATOIRE 3: Chat avec python.
Réalisé par EL BAKKOURY Yassine et EL HADDADI Yassine.
Série 6a Binôme 3.
Réalisé le 15/03/2018.

Le dossier se compose de 3 fichiers: le README, un fichier serveur et un fichier client.
Pour pouvoir faire du peer-to-peer il suffit simplement de lancer deux clients que l'un se connecte sur l'IP et le port du correspondant. Deux méthodes sont disponibles:
/join Ip Port
ou 
/private IP/Port/Message

La deuxième méthode permet de ne pas avoir à quitter le serveur sur lequel nous sommes connectés si nous étions préalablement en communication client/serveur.
Et donc la communication client/serveur se lance simplement par /join ServeurHôte Port .
On peut essayer cela en lançant d'abord le serveur qui va se connecter sur localhost 5500, et ensuite lancer le client, taper[ /join localhost 5500 ] pour se connecter sur le serveur.

Pour communiquer: 
/send message
pour recevoir les messages l'un en dessous de l'autre sur la fenêtre du serveur

/send /list 
pour obtenir la liste des IP+Port (clients) sur la fenêtre du serveur.

/send /info
pour obtenir certaines informations.