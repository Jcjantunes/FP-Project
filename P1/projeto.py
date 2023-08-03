#87668 Joao Antunes
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Primeiro Projeto 
''''''''''''''''''
Versao Simplificada 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def gera_chave1 ( letras ):   # Criacao do tuplo de tuplos
    t = letras [0:5]
    l = letras [5:10]
    d = letras [10:15]
    f = letras [15:20]
    g = letras [20:25]
    chave = (t, l, d, f, g) 
    return chave 

def obtem_codigo1 (car , chave):
    s = ''
    for i in range(len(chave)):           #Percorrer as linhas de chave
        for j in range (len (chave[i])):  #Percorrer as colunas de chave
            if chave[i][j] == car:        #Verificar se o caracter e igual a algum dos caracteres do tuplo
                s = str(i) + str(j)        
    return s                              #Devolve a string com a posicao do caracter

def codifica1 ( cad , chave ):
    s = ''
    for i in range(len (cad)):                 #Percorre os elementos de cad um a um
        s = s + obtem_codigo1 (cad[i], chave ) #Formacao da string com as posicoes dos varios elementos de cad
    return s                                   #Devolve as posicoes dos elementos de cad

def obtem_car1 (cod, chave):              
    k = ''
    for i in range ( len (chave)):           #Percorre as linhas de chave
        for j in range ( len ( chave[i])):   #Percorre as colunas de chave
            if cod == str(i) + str ( j ):    #Verifica se cod pertence a chave
                k = chave [i][j]
    return k                                 #Devolve o caracter correspondente a posicao da linha e da coluna da chave

def descodifica1 (cad_codificada, chave):
    s=''
    for i in range (0, len (cad_codificada), 2):                              #Percorre os elementos de cad_codificada de 2 em 2 elementos      
        s = s + obtem_car1 (cad_codificada [i] + cad_codificada [i+1], chave) 
    return s                                                                  #Devolve os caracteres correspondentes a posicao das linhas e das colunas de chave

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Versao Final

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nt = numero de tuplos necessarios
ln = comprimento de chaves
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def getNumLinhas (letras):       #Calcula o numero de tuplos necessarios
    from math import sqrt        
    ln = len ( letras )
    nt = sqrt (ln)               #Caso o quadrado perfeito seja o proprio comprimento de letras               
    while round(nt) != nt:       #Entra no ciclo caso o arredondamento de nt seja diferente igual ao valor exato de nt                   
        ln = ln+1                                        
        nt =  sqrt (ln)          #Actualizacao do valor de nt                     
        
    return round(nt)                             
    
def obter_tuplos(numLinhas, numColunas, letras): #Devolve os tuplos de acordo com o numero de linhas e o numero de colunas
    k = numColunas
    t =()
    for i in range(numLinhas):                   #Percorre todos os elementos do numLinhas
        j = k * i                                #Para cada posicao do numLinhas calcula a primeira posicao de cada tuplo formado
        t1 = (letras[j:numColunas + j])          #Restricao da posicao inicial e final dos tuplos
        t = t + (t1,)  
    return t                                     

def gera_chave2 ( letras ):
    numLinhas =  getNumLinhas(letras)
    resto = len ( letras ) % numLinhas                       #Calcula o numero de elementos no ultimo tuplo        
    if resto == 0:                                           #Isolamento do caso em que o comprimento de letras seja divisivel pelo numero de linhas dando um valor nao certo 
        numColunas = numLinhas                                       #Neste caso o numero de linhas tera de ser igual ao numero de colunas 
    else:        
        numColunas = round((len ( letras ) - resto )/ (numLinhas-1)) #Calculo de quantos elementos existem em cada tuplo com excecao do ultimo
    return obter_tuplos(numLinhas, numColunas, letras)    

def obtem_codigo2 ( car, chave):
    
    s = obtem_codigo1 (car , chave)           #Recurso a funcao obtem_codigo1
    if s == '':
        s = 'XX'                              #Caso car nao pertenca a chave entao s sera igual a XX
    return s

def codifica2( cad, chave):                   
    s = ''
    for i in range(len (cad)):                 #Percorre todas as posicoes de cad
        s = s + obtem_codigo2 (cad[i], chave ) #Recurso a funcao obtem_codigo2
    return s  

def obtem_car2 ( cod, chave ):
    s = obtem_car1 (cod, chave)                #Recurso a funcao obtem_car1
    if cod == 'XX':                            
        s = '?'                                #Caso os cod seja igual a XX o caracter correspondente sera ?
    return s

def descodifica2 ( cad_codificada , chave ):
    s=''
    for i in range (0, len (cad_codificada), 2):                              #Percorre todas as posicoes de cad_codificada de 2 em 2    
        s = s + obtem_car2 (cad_codificada [i] + cad_codificada [i+1], chave) #Recurso a funcao obtem-car2 para devolver os caracteres correspondentes a cad_codificada
    return s      