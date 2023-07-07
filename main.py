from random import randint
from colorama import Fore, Style
import time
import os
import platform
from packge.slow_print import slowprint
import requests
import json

class NumeroDasorte:
    def __init__(self) -> None:
      pass

    def api_lote(self):

        response = requests.get('https://api.guidi.dev.br/loteria/megasena/ultimo')
        json_data = json.loads(response.text)
        last_result = (json_data['dezenasSorteadasOrdemSorteio'])
        slowprint(f'Ultimo resultado da mega-sena{last_result}')
    
    def  checkPlatform(self):
        system_platform = platform.system()

        if system_platform == 'Windows':
            os.system('cls'),
        
        else:
            os.system('clear')

    def initialScreen(self):
        
        print(Fore.GREEN + Style.BRIGHT + '███╗   ██╗██╗   ██╗███╗   ███╗██████╗  ██████╗     ██████╗  █████╗     ███████╗ ██████╗ ██████╗ ████████╗███████╗')
        print(Fore.YELLOW + Style.BRIGHT +'████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝')
        print(Fore.RED + Style.BRIGHT +'██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝██║   ██║    ██║  ██║███████║    ███████╗██║   ██║██████╔╝   ██║   █████╗  ')
        print(Fore.BLUE + Style.BRIGHT+' ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║    ██║  ██║██╔══██║    ╚════██║██║   ██║██╔══██╗   ██║   ██╔══╝  ')
        print(Fore.CYAN + Style.BRIGHT +'██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝    ██████╔╝██║  ██║    ███████║╚██████╔╝██║  ██║   ██║   ███████╗')
        print(Fore.MAGENTA + Style.BRIGHT +'╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝' + Style.RESET_ALL)
        print('                                                  by.Rafael Guedes                                                ') 
        print('                                                 github.com/guedes2142                                                ')                                                                                                             

    def timeToLuck(self):
        t = 3
        print(Fore.CYAN + 'Seu número será gerado em ......' + Style.RESET_ALL)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    def randNumbers(self):
        self.checkPlatform()
        while True:

            for i in range(10,30):

                x = randint(0,49)
                y = randint(50,100)
                z = randint(0,30)
                n = randint(20,29)
                j = randint(0,19)
                k = randint(0,100)

            res = x , y , z, n , j, k 
            res = str(res)
            self.api_lote()
            slowprint(Fore.GREEN + Style.BRIGHT + f'Seu número da sorte é = {res}' + Style.RESET_ALL ) 
            slowprint(Fore.BLUE + 'Deseja continuar e gerar um novo número da sorte?' +Style.RESET_ALL)

            user_choice = input(Fore.YELLOW + 'S/n:  ' + Style.RESET_ALL).lower()
            if user_choice.startswith('s'):
               self.checkPlatform()
               self.timeToLuck()
            else:
                self.checkPlatform()
                slowprint('Obrigado por usar meu app, by.Rafael Guedes 🧡')
                time.sleep(2)
                exit()
               
start = NumeroDasorte()
start.checkPlatform()
start.initialScreen()
start.timeToLuck()
start.randNumbers()


