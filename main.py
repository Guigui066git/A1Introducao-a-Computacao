"""
Forca - Grupo 5
Autores: Felipe Lamarca (B39045), Guilherme Melo (B44397), 
Ian Araujo (B39046), Janaina Neres (B43889) e Luca Escopelli (B39339)

"""

import random
import time
import os
# importa o módulo gráfico do outro grupo
import modulo_grafico 

class funcoes(): 
    def remove_repetidos(lista):
        list_temp = []
        for i in lista:
            if i not in list_temp:
                list_temp.append(i)
        list_temp.sort()
        return list_temp
    
    def convert_str(lista, str=''):
        """ Converte lista para string, juntando os elementos da lista e a str dada em uma str .
    
        Parameters
        ----------
        lista : list
          Lista que deseja transformar em string
        
        str : string
          Uma string para preceder a lista (se não inserida retorna apenas a lista)
        Returns
        ----------
        str
          Uma string unindo todos os elementos da lista
        """
        return str.join(lista)
    
    def criar_listas(arquivos):
      """
      Cria uma lista contendo listas de palavras. Cada lista é composta por palavras de determinado tema. A função tem como input arquivos .txt organizados da seguinte forma: uma palavra por linha, sem linhas em branco.
      Parameters
      ----------
      arquivos : list
        Lista de arquivos para serem lidos.

      Returns
      ----------
      list  
        Retorna uma lista composta pelas listas lidas.
      """
      lista_ll = []
      for arquivo in arquivos:
        f = open(arquivo)
        lista_arquivo = []
        for palavra in f:
          palavra = palavra.replace("\n", "")
          lista_arquivo.append(palavra)
        lista_ll.append(lista_arquivo)
      return lista_ll
  
    def normalizar_palavra(palavra):
      """A função substitui palavras com 'acidentes gráficos', tais como acentos, tremas ou a cedilha, pela versão 'normal' da letra. Para isso, usa-se uma lista de repetições com as expressões regulares mais comuns."""
      repeticoes = ["á", "é", "í", "ó", "ú", "â", "ê", "ô", "û", "ç", "ã", "õ"]
      string_letras = ""
      palavra = palavra.lower()
      for letra in palavra:
        if letra in repeticoes:
          if letra in ["á", "â", "ã"]:
            string_letras += "a"
          elif letra in ["é","ê"]:
            string_letras += "e"
          elif letra in ["í"]:
            string_letras += "i"
          elif letra in ["ó", "ô", "õ"]:
            string_letras += "o"
          elif letra in ["ú", "û"]:
            string_letras += "u"
          elif letra in ["ç"]:
            string_letras += "c"
        else:
          string_letras += letra
      return string_letras
    def caregando():
        for i in range(1, 3):
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\t\\    Carregando    /")
          time.sleep(.5)
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\t|    Carregando.   |")
          time.sleep(.5)
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\t/    Carregando..  \\")
          time.sleep(.5)
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\t—    Carregando... —")
          time.sleep(.5)
          os.system('cls' if os.name == 'nt' else 'clear')
          
      
class variaveis():
        ll_palavras = funcoes.criar_listas(arquivos = ["palavras/corpo_humano.txt", "palavras/animais.txt", "palavras/alimentos.txt", "palavras/profissões.txt", "palavras/comunicação.txt", "palavras/esportes.txt"])   
        ward = "repetir"
        jogar_de_novo = True
        escolha_lista = ""

class jogo():
    def jogar():  
        """Inicia um laço de repetição responsável por todos os processos do jogo."""
        while variaveis.ward == "repetir":
          variaveis.escolha_lista = input("Por favor, escolha um tema para o jogo digitando o número correspondente: \n\n 0. Corpo humano \n 1. Animais \n 2. Alimentos \n 3. Profissões \n 4. Comunicação \n 5. Esportes\n \n R: ")
          if variaveis.escolha_lista == "0":
            print("\nVocê escolheu: corpo humano.\nAguarde o início do jogo!")
            variaveis.ward = "não repetir"
          elif variaveis.escolha_lista == "1":
            print("\nVocê escolheu: Animal. \nAguarde o início do jogo!")
            variaveis.ward = "não repetir"
          elif variaveis.escolha_lista == "2":
            print("\nVocê escolheu: Alimento. \nAguarde o início do jogo!")
            variaveis.ward = "não repetir"
          elif variaveis.escolha_lista == "3":
            print("\nVocê escolheu: Profissão. \nAguarde o início do jogo!")
            variaveis.ward = "não repetir"
          elif variaveis.escolha_lista == "4":
            print("\nVocê escolheu: Comunicação. \nAguarde o início do jogo!")
            variaveis.ward = "não repetir"
          elif variaveis.escolha_lista == "5":
            print("\nVocê escolheu: Esportes. \nAguarde o início do jogo!")
            variaveis.ward = "não repetir"
          else:
            os.system('cls' if os.name=='nt' else 'clear')
            print("\nEntrada inválida! Você está digitando um número válido?")
            variaveis.ward = "repetir"
        variaveis.ward = "repetir"
        # depois de 3 segundos, inicia-se a tela de carregamento
        time.sleep(3)
        
        # cria-se uma tela de carregamento com símbolo 'carregando'. Isso dura alguns segundos antes do início do jogo

        funcoes.caregando()
        # A partir daqui, inicia-se o jogo propriamente dito. É escolhida uma palavra aleatória da lista
        # de listas, mais especificamente uma palavra dentro da sublista cujas palavras estão relacionadas ao tema que o usuário optou no início do programa. Em seguida, a palavra é "normalizada" através da função criada. A palavra 'maçã' torna-se 'maca'.
        variaveis.escolha_lista = int(variaveis.escolha_lista)
        palavra_secreta = random.choice(variaveis.ll_palavras[variaveis.escolha_lista])
        palavra_normalizada = funcoes.normalizar_palavra(palavra_secreta)
        
        # cria-se duas listas vazias: uma que receberá as letras corretas digitadas, ou seja, aquelas que estejam dentro da palavra sorteada; e uma que receberá as listas incorretas, que não estão contidas na palavra sorteada.
        letras_corretas =[]
        letras_erradas = []
        
        
        # o grupo mostra na imagem da forca um componente de LETRAS USADAS. Para contemplar isso, criamos a string tentativas, que receberá cada letra que o usuário digitar.
        tentativas = ""
        
        # palavra, que corresponde aos underlines a serem 'descobertos' pelo usuário, recebe um underline para cada letra da palavra secreta, isto é, 1 underline multiplicado pelo len da palavra secreta.
        palavra = "_ "*len(palavra_secreta)
        
        # Explicação geral: caso o usuário digite mais de uma letra, o programa informa que a entrada é inválida e repete o imput, para que o usuário tente mais uma vez. Além disso a depender do len da lista de letras erradas, a condicional utiliza uma função específica do módulo gráfico, correspondente ao estado do 'boneco enforcado' no jogo.
        ward_erro = False
        
        #lê o número de erros já cometidos e chama a função do boneco equivalente. 
        while True:
          os.system('cls' if os.name == 'nt' else 'clear')
          if len(letras_erradas) == 0:
           modulo_grafico.boneco0(palavra,tentativas)
          elif len(letras_erradas) == 1:
            modulo_grafico.boneco1(palavra,tentativas)
          elif len(letras_erradas) == 2:
            modulo_grafico.boneco2(palavra,tentativas)
          elif len(letras_erradas) == 3:
            modulo_grafico.boneco3(palavra,tentativas)
          elif len(letras_erradas) == 4:
            modulo_grafico.boneco4(palavra,tentativas)
          elif len(letras_erradas) == 5:
            modulo_grafico.boneco5(palavra,tentativas)
        
          if ward_erro:
            print("\nDigite uma única letra!")
          letras_digitadas = input("\nTente uma letra: ") 
          letras_digitadas = funcoes.normalizar_palavra(letras_digitadas) 
          
          #confere se o usuário digitou apenas uma letra. Caso contrário, solicita que o usuário insira uma entrada novamente.
          if len(letras_digitadas) != 1:
            ward_erro= True
            continue
          else:
            ward_erro= False

          #confere se o usuário digitou uma letra realmente
          if letras_digitadas not in "abcdefghijklmnopqrstuvwxyz":
            ward_erro = True
            continue
          else:
            ward_erro = False
        
          #adiciona a tentativa à lista de letras(corretas ou erradas) para que essas listas possam ser usadas depois para contagem de erro
          if letras_digitadas in palavra_normalizada:
            letras_corretas += letras_digitadas
          else:
            letras_erradas += letras_digitadas
          letras_corretas = funcoes.remove_repetidos(letras_corretas)
          letras_erradas = funcoes.remove_repetidos(letras_erradas)
          
          # Com seis erros o usuário perde e é apresentado o boneco completo e enforcado
          if len(letras_erradas) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            modulo_grafico.boneco6(palavra, tentativas)
            print(f"\nInfelizmente você perdeu! \nA palavra era {palavra_secreta}")
            variaveis.jogar_de_novo = input("Pressione enter para jogar de novo ou insira qualquer outra entrada para sair:\n")
            if variaveis.jogar_de_novo == "":
                variaveis.jogar_de_novo = True
            else:
                variaveis.jogar_de_novo = False
            break
        
          #confere se a letra já foi digitada e, caso não tenha sido, a inclui na lista de letras já tentadas
          if letras_digitadas not in tentativas:
            tentativas = tentativas + " " + letras_digitadas
        
        
          #transforma a palavra a ser descoberta em uma lsita para que possa ser modificada dentro do jogo
          palavra_lista = []
          for letra in palavra:
            palavra_lista.append(letra)
        
          #inicia os dois contadores que serão utilizados no loop e em seguida  
          contador_palavra = -1
          contador_palavra2 = -2
          for letra in palavra_normalizada:
            contador_palavra += 1
            contador_palavra2 += 2
            if letras_digitadas == letra:
              palavra_lista[contador_palavra2] = palavra_secreta[contador_palavra]
          palavra = funcoes.convert_str(palavra_lista, "")
        
          # O verificador começa com True e o for caminha por toda a palavra. Caso a lista de letras corretas não esteja completamente preenchida com as letras da palavra normalizada, então significa que o jogador ainda não ganhou o jogo e o verificador se torna False. Se todas as letras da palavra normalizada estiverem dentro da lista de letras corretas, o verificador se mantem True e o usuário finalmente ganhou a partida de forca.
          verificador = True
          for letra2 in palavra_normalizada:
            if letra2 not in letras_corretas:
              verificador = False
          if verificador:
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(letras_erradas) == 0:
              modulo_grafico.boneco0(palavra,tentativas)
            elif len(letras_erradas) == 1:
              modulo_grafico.boneco1(palavra,tentativas)
            elif len(letras_erradas) == 2:
              modulo_grafico.boneco2(palavra,tentativas)
            elif len(letras_erradas) == 3:
              modulo_grafico.boneco3(palavra,tentativas)
            elif len(letras_erradas) == 4:
              modulo_grafico.boneco4(palavra,tentativas)
            elif len(letras_erradas) == 5:
              modulo_grafico.boneco5(palavra,tentativas)
            print("\nParabéns, você ganhou!")
            print(f"A palavra era: {palavra_secreta}")
            variaveis.jogar_de_novo = input("Pressione enter para jogar de novo ou insira qualquer outra entrada para sair:\n")
            
            if variaveis.jogar_de_novo == "":
                variaveis.jogar_de_novo = True
            else:
                variaveis.jogar_de_novo = False
            break

# a função traz a apresentação do jogo desenvolvida pelo grupo
modulo_grafico.apresentacao()
time.sleep(3)
os.system('cls' if os.name=='nt' else 'clear')
while variaveis.jogar_de_novo == True:
    # definimos uma duração de 3 segundos para a tela de apresentação
    jogo.jogar()
    #a estrutura de repetição a seguir trabalha com uma entrada do usuário, que escolherá qual o tema de sua preferência para as palavras do jogo. Se o usuário digitar um número correspondente a qualquer um dos temas, isto é, qualquer número de 0 a 5, o programa inicia. Do contrário, o programa pede que o usuário insira um número válido.
    os.system('cls' if os.name=='nt' else 'clear')
print("Obrigado por jogar")
