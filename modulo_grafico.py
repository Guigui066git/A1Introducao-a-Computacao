"""
Created on Wed Apr 14 13:57:23 2021

Autores:
    Edilton Brandão
    Caio lanna
    Anderson Lima
    Pedro portela
    Leonardo Lima
"""
# ===============================VARIÁVEIS A DEFINIR===========================
'''letras_digitadas = palavra secreta com as letras que já foram descobertas e as que faltam descobrir
   exemplo: a_ac_xi
   letras_usadas = lista com todas as letras que já foram digitadas'''
# =============================================================================




def apresentacao():
    ''' Essa função aprsenta o título de apresetação do jogo'''
    
    print("      __     ________      ________     ________  \n     |  |   /   __   \   /   ______|   /   __   \ \n     |  |   |  |  |  |   |  |  ____    |  |  |  | \n __  |  |   |  |  |  |   |  | |__  |   |  |  |  | \n|  |_|  |   |  |__|  |   |  |___|  |   |  |__|  | \n\_______/   \________/   \_________/   \________/\n")
    print("  _______      ________ \n |   __  \    |   __   | \n |  |  |  |   |  |__|  | \n |  |  |  |   |   __   | \n |  |__|  /   |  |  |  |\n |_______/    |__|  |__| \n")   
    print(" _______     ________      _______       ________      ________ \n|   ____|   /   __   \    |   __  \     /   _____|    |   __   | \n|  |___     |  |  |  |    |  |__|  |    |  |          |  |__|  | \n|   ___|    |  |  |  |    |      _|     |  |          |   __   | \n|  |        |  |__|  |    |  |\  \      |  |_____     |  |  |  | \n|__|        \________/    |__| \__\     \________|    |__|  |__|\n")



'''A seguir está definida as funções que desenha cada boneco'''

# =============================================================================
def boneco6 (letras_digitadas, letras_usadas):

    for i in range(0, 18):
        print("=", end="")
    print(" ")

    print("||  /            |")
    ("|| /             |")
    print("||/              |")

    print("||              (_)")
    print("||               |")
    print("||              /|\\")
    print("||             / | \\")
    print("||               |")
    print("||              / \\")
    print("||            _/   \_")

    for i in range(0, 4):
        print("||")
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")
    
    
    
    
    
    
def boneco5 (letras_digitadas, letras_usadas): 
    
    for i in range(0, 18):
         print("=", end="")
    print("")

    print("||  /            |")
    print("|| /             |")
    print("||/              |")

    print("||              (_)")
    print("||               |")
    print("||              /|\\")
    print("||             / | \\")
    print("||               |")
    print("||                \\")
    print("||                 \\_")

    for i in range(0, 4):
        print("||")
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")
    
    
    
    
    
def boneco4 (letras_digitadas, letras_usadas):   
    for i in range(0, 18):
        print("=", end="")
    print("")

    print("||  /            |")
    print("|| /             |")
    print("||/              |")

    print("||              (_)")
    print("||               |")
    print("||              /|\\")
    print("||             / | \\")
    print("||               |")
    print("||                ")
    print("||                 ")

    for i in range(0, 4):
        print("||")
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")    
    
    
    
    
    
def boneco3 (letras_digitadas, letras_usadas):
    for i in range(0, 18):
        print("=", end="")
    print("")

    print("||  /            |")
    print("|| /             |")
    print("||/              |")

    print("||              (_)")
    print("||               |")
    print("||              /|")
    print("||             / | ")
    print("||               |")
    print("||                ")
    print("||                 ")

    for i in range(0, 4):
        print("||")     
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")
    
    
    
    
    
def boneco2 (letras_digitadas, letras_usadas):   
    for i in range(0, 18):
        print("=", end="")        
    print("")

    print("||  /            |")
    print("|| /             |")
    print("||/              |")

    print("||              (_)")
    print("||               |")
    print("||               |")
    print("||               | ")
    print("||               |")
    print("||                ")
    print("||                 ")

    for i in range(0, 4):
        print("||")     
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")
    
    
    
    
    
    
def boneco1 (letras_digitadas, letras_usadas):   
    for i in range(0, 18):
        print("=", end="")        
    print("")

    print("||  /            |")
    print("|| /             |")
    print("||/              |")

    print("||              (_)")
    print("||                ")
    print("||                ")
    print("||                ")
    print("||               ")
    print("||                ")
    print("||                 ")

    for i in range(0, 4):
        print("||")     
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")







def boneco0 (letras_digitadas, letras_usadas):  
    for i in range(0, 18):
        print("=", end="")
    print("")

    print("||  /            |")
    print("|| /             |")
    print("||/              |")

    print("||              ")
    print("||                ")
    print("||                ")
    print("||                ")
    print("||               ")
    print("||                ")
    print("||                 ")

    for i in range(0, 4):
        print("||")         
    print(f"|| {letras_digitadas}           LETRAS USADAS:  {letras_usadas}")
    
# =============================================================================

   
    
