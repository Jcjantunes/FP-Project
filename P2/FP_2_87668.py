#87668 Joao Antunes

#contrutores
def faz_pos(l,c): 
    if type(l) != int or type(c) != int or l<0 or c<0:             #restricao dos argumentos
        raise ValueError ('faz_pos: argumentos errados')
    else:
        t=(l,c)
    return t

#seletores
def linha_pos(p):
    return p[0]                #devolve a posicao da linha do tuplo

def coluna_pos(p):
    return p[1]                #devolve a posicao da coluna do tuplo

#reconhecedores
def e_pos(arg):
    if len(arg) != 2 or type(arg) != tuple:  # verifica se arg tem 2 elementos e se e um tuplo
        return False
    return True

#testes
def pos_iguais(p1,p2):
    if p1 == p2:
        return True
    return False

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Tipo Chave
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
#Construtores
def gera_chave_linhas (l, mgc):                      
    lst = []
    lst1=[]

    if len (l) != 25 or type (mgc) != str or type(l) != tuple:             #restricao dos argumentos de gera_chave_linhas
        raise ValueError ( 'gera_chave_linhas: argumentos errados')
    
    s=''
    for o in l:                                                            # criacao da string com os elementos de l
        s=s+str(o)
    
    if s != s.upper():
        raise ValueError ('gera_chave_linhas: argumentos errados')         #restricao de l em que todos os seus elementos tem de ser letras maiusculas 
    
    for a in l:                                                            #restricao onde verifica se l tem letras repetidas 
        if a not in lst1:
            lst1= lst1 + [a]
        else:
            raise ValueError ( 'gera_chave_linhas: argumentos errados')
    
    for i in mgc:                                                          #criacao da "primeira" parte da chave onde inclui os elementos de mgc nao repetidos     
        if i != ' ':
            if i not in l:
                raise ValueError ('gera_chave_linhas: argumentos errados')                  
            elif i not in lst:
                lst = lst + [i]
                                
    for j in l:                                                           #atualizacao de lst onde se inclui os elementos da chave nao iguais aos elementos da "primeira" parte
        if j not in lst:                                                  #da chave
            lst = lst + [j]
                
    t = lst [0:5]
    k = lst [5:10]
    d = lst [10:15]
    f = lst [15:20]
    g = lst [20:25]
    chave = [t, k, d, f, g]         
    return chave

#--------------------------------------------------
#                 Chave espiral -------------------> nesta espiral criei um algoritmo onde associei 2 quadrados, um externo e um interno onde este inclui o centro onde associei
#--------------------------------------------------  que as posicoes da espiral,e a posicao final iriam ser associadas as posicoes "normais" de uma lista final
#--------------------------------------------------
#|  0 -  0 |  1 -  1 |  2 -  2 |  3 -  3 |  4 - 4 |
#--------------------------------------------------
#|  5 - 15 |  6 - <0>|  7 - <1>|  8 - <2>|  9 - 5 |
#--------------------------------------------------
#| 10 - 14 | 11 - <7>| 12 - 24 | 13 - <3>| 14 - 6 |
#--------------------------------------------------
#| 15 - 13 | 16 - <6>| 17 - <5>| 18 - <4>| 19 - 7 |
#--------------------------------------------------
#| 20 - 12 | 21 - 11 | 22 - 10 | 23 -  9 | 24 - 8 |
#--------------------------------------------------
def BuildLstPos(dic, pos, ln, s):     #funcao auxiliar que devolve uma lista com os elementos do dicionario
    
    lst  = list(dic.keys())
    if (s == 'r'):
        kLst = lst[pos::]             #invercao da lista 
        if (pos > 0):
            kLst = kLst + lst[0:pos]
    else:
        p = ln * (-1) + pos
        kLst = lst[p::-1]             # limitar desde posicao ate inicio (reverse)
        lAux = lst[pos+1::]           # retirar os elementos invertidos
        kLst = kLst + lAux[::-1]      # inverter o resto dos elementos
    
    lst = []
    for i in kLst:
        lst =  lst + [dic[i]]     #contrucao da lista com elementos da chave do dicionario (sao formados em gera_chave_espiral)
        
    return lst    

def getPositions(dic_ext, dic_int, p, s):                             
    lstPos = BuildLstPos(dic_ext, p, len(dic_ext), s)                  # ordenar posicoes do quadrado externo conforme ponto de incio
    lstPos = lstPos + BuildLstPos(dic_int, int(p/2), len(dic_int), s)  # ordenar posicoes do quadrado interno conforme ponto de incio
    return lstPos
    
def gera_chave_espiral(l, mgc, s, pos):
    lst1=[]

    for a in l:                                                       # restricao onde verifica se os elementos de l sao repetidos 
        if a not in lst1:
            lst1 = lst1 + [a]
        else:
            raise ValueError ( 'gera_chave_espiral: argumentos errados')    
    
    if len (l)!= 25 or type (l) != tuple or type (mgc) != str or len (pos) != 2 or type (pos) != tuple or (s != 'c' and s != 'r'): # restricao que verifica as carateristicas dos
        raise ValueError ('gera_chave_espiral: argumentos errados')                                                                #argumentos

    s1=''
    for o in l:                                    # criacao da string com os elementos de l
        s1 = s1 + str(o)
       
    if s1 != s1.upper():                           # se a string de l nao for igual a transformacao das letras em maiusculas ira dar erro
        raise ValueError ('gera_chave_espiral: argumentos errados') 
    
    for i in mgc:                                                          #restricao onde verifica se os elementos de mgc estao em l    
        if i != ' ':
            if i not in l:
                raise ValueError ('gera_chave_espiral: argumentos errados')                
    
    
    pos_ini = { (0,0):0, (0,4):4, (4,4):8, (4,0):12 }                      #as posiveis posicoes onde a espiral pode comecar (coordenadas do canto : indice na espiral desse 
                                                                           #desse canto, confere-se no desenho da matriz em cima)
    if pos not in pos_ini:                 #restricao que verifica se o pos introduzido na funcao e igual a algum dos cantos da matriz 5 x 5
        raise ValueError ('gera_chave_espiral: argumentos errados')
    
    dic_ext = {0:0, 1:1, 2:2, 3:3, 4:4, 5:9, 6:14, 7:19, 8:24, 9:23, 10:22, 11:21, 12:20, 13:15, 14:10, 15:5} #{indices da lista final:indices da lista em espiral do quadrado externo}
    dic_int = {0:6, 1:7, 2:8, 3:13, 4:18, 5:17, 6:16, 7:11} # {indices da lista final:indices da lista em espiral do quadrado interno}

    ultima_posicao = 12 # a posicao final e sempre 12 na lista espiral
    
    lstPos = []        
    p = pos_ini[pos]   #indice na matriz da espiral onde comeca a disposicao da mgc
    
    lstPos = getPositions(dic_ext, dic_int, p, s)   
    lstPos = lstPos + [ultima_posicao]          # incluir ultima posicao
    
    idx = 0 
    d_final = {}
    for c in mgc:                               # criacao do dicionario com a "primeira" parte com os elementos nao repetidos de mgc
        if c not in d_final.values() and c != ' ':
            d_final[lstPos[idx]] = c
            idx = idx + 1
    for k in l:                                 #actualizacao do dicionario com a "segunda" parte com os elementos nao repetidos de l e que nao estao em d_final
        if k not in d_final.values():
            d_final[lstPos[idx]] = k
            idx = idx + 1
            
    lsta = []    
    lsta = list(d_final.values())               #tranformar o dicionario em lista
    
    t = lsta [0:5]
    k = lsta [5:10]
    d = lsta [10:15]
    f = lsta [15:20]
    g = lsta [20:25]
    
    chave = [t, k, d, f, g]      
            
    return chave             

#seletores

def ref_chave(c, p):    
    return c[linha_pos(p)][coluna_pos(p)] #recurso a linha_pos , coluna_pos para devolver o caracter na posicao introduzida

#modificador
def muda_chave(c, p, l):
    c[linha_pos(p)][coluna_pos(p)] = l #recurso a linha_pos, coluna_pos para substituir o caracter na posicao selecionada pelo l 
    return c

#reconhecedores
def e_chave(arg): 
    s=''
    if len(arg) != 5:               #verificacao se existem 5 linhas na chave
        return False
    for i in arg:
        if len (i) != 5:           #verificacao se existem 5 elementos em cada linha
            return False
        
    for o in range(len(arg)):      #contrucao de uma string com os elementos de arg
        for j in range (len(arg[o])):
            s=s+str(arg[o][j])
            
    if s != s.upper():             #verificacao se os elementos da string sao todos letras maiusculas
        return False  
    
    return True

#tranformador
def expand(x):                   # funcao auxiliar que adiciona os espacos entre os elementos da string
    s=''
    for i in x:
        s= s + i + ' '
    return s + '\n'

def string_chave (c):                 
    s=''
    for i in c:                 #formacao da string com os elementos da chave introduzida
        for j in i:
            s=s+str(j)
    t = s [0:5]
    k = s [5:10]
    d = s [10:15]
    f = s [15:20]
    g = s [20:25]
    
    return  expand(t) + expand(k) + expand(d) + expand(f) +expand(g)
    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Funcoes a desenvolver
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
def digramas(mens):
    s=''
    s1=''
    for i in mens:                    #formacao da string com os elementos de mens sem os espacos
        if i != ' ':
            s= s + i
    for j in range (len(s)-1):        #adicionar o X caso os elementos seguidos sejam iguais
        if s[j]==s[j+1]:
            s1= s1 + s[j] + 'X'
        else:
            s1 = s1 + s[j]
    s1 = s1 + s[len(s)-1]
    if len(s1)%2 !=0:                 #caso o comprimento da string seja impar adicionar um X no final
        s1= s1 + 'X'
    return s1
                  
def figura (digrm,chave):
    t=()
    for i in range (len(chave)):
        for j in range (len(chave[i])):
            if chave[i][j] == digrm[0]:          #obter a posicao do primeiro elemento do digrm
                pos1 = faz_pos(i,j)
            if chave[i][j] == digrm[1]:
                pos2 = faz_pos(i,j)              #obter a posicao do segundo elemento do digrm
    
    if linha_pos(pos1)==linha_pos(pos2):         # caso a linha de pos1 seja igual a linha de pos 2 a figura ira ser l
        fig = 'l'
   
    elif coluna_pos(pos1)==coluna_pos(pos2):    #caso a coluna se pos1 seja igual a coluna de pos 2 a figura sera c     
        fig = 'c'

    else:                                       # caso contrario ira ser r
        fig = 'r'
    t = (fig,pos1,pos2)
    return t

def codifica_l(pos1, pos2, inc):                   
    if inc == 1:                                     #encriptar
        if coluna_pos(pos1) == 0 or 1 or 2 or 3:     #adiciona sempre 1 a coluna de pos1 e pos 2 e a linha mantem dado que nao varia
            c1 = coluna_pos(pos1) + 1
            pos1_cod = (linha_pos(pos1),c1)

        if coluna_pos(pos2) == 0 or 1 or 2 or 3:     
            c2 = coluna_pos(pos2) + 1
            pos2_cod = (linha_pos(pos2),c2)
            
        if coluna_pos(pos1) == 4:                   #caso a coluna de pos 1 e de pos 2 seja igual a 4 a coluna tera de ter o valor de 0 e l nao varia
            c1 = coluna_pos(pos1) -4
            pos1_cod = (linha_pos(pos1), c1)
        
        if coluna_pos(pos2) == 4:
            c2 = coluna_pos(pos2)-4
            pos2_cod = (linha_pos(pos1),c2)
    
        return pos1_cod, pos2_cod
    
    if inc == -1:                                   #desincriptar
        if coluna_pos(pos1) ==  1 or 2 or 3 or 4:   #subtrair sempre 1 as colunas de pos 1 e pos 2 o valor de l nao varia
            c1 = coluna_pos(pos1) - 1
            pos1_cod = (linha_pos(pos1),c1)
        
        if coluna_pos(pos2) == 1 or 2 or 3 or 4:
            c2 = coluna_pos(pos2) - 1
            pos2_cod = (linha_pos(pos2),c2)
                    
        if coluna_pos(pos1) == 0:                   # caso as colunas de pos 1 e pos 2 sejam 0 tera de se adicionar 4 a coluna de pos1 e pos 2, o valor de l nao altera
            c1 = coluna_pos(pos1) + 4
            pos1_cod = (linha_pos(pos1), c1)
                
        if coluna_pos(pos2) == 0:
            c2 = coluna_pos(pos2)+ 4
            pos2_cod = (linha_pos(pos1),c2)
            
        return pos1_cod, pos2_cod        

def codifica_c (pos1,pos2,inc):
    if inc == 1:                                 #para encriptar
        if linha_pos(pos1) == 0 or 1 or 2 or 3:  # adicionar 1 ao valor as linhas de pos 1 e pos2 e os valores da coluna nao variam
            l1 = linha_pos(pos1) + 1
            pos1_cod = (l1,coluna_pos(pos1))
        
        if linha_pos(pos2) == 0 or 1 or 2 or 3:
            l2 = linha_pos(pos2) + 1
            pos2_cod = (l2,coluna_pos(pos2))
            
        if linha_pos(pos1) == 4:                #caso o valor das linhas de pos 1 e pos 2 seja 4  tera de se subtrair 4 ,as colunas nao alteram
            l1 = linha_pos(pos1) - 4
            pos1_cod = (l1,coluna_pos(pos1))
            
        if linha_pos(pos2) == 4:
            l2 = linha_pos(pos2) - 4
            pos2_cod = (l2,coluna_pos(pos2))
            
        return pos1_cod,pos2_cod
           
    if inc == -1:                                #desencriptar
        if linha_pos(pos1) ==  1 or 2 or 3 or 4: # subtrair 1 ao valor das linhas de pos 1 e pos 2 , os valores das colunas nao se alteram
            l1 = linha_pos(pos1) - 1
            pos1_cod = (l1, coluna_pos(pos1))
                   
        if linha_pos(pos2) == 1 or 2 or 3 or 4:
            l2 = linha_pos(pos2) - 1
            pos2_cod = (l2, coluna_pos(pos2))
                               
        if linha_pos(pos1) == 0:                  #caso o valor das linhas de pos1 e pos 2 seja 0 soma 4 valores, os valores da coluna nao alteram
            l1 = linha_pos(pos1) + 4
            pos1_cod = (l1, coluna_pos(pos1))
                           
        if linha_pos(pos2) == 0:
            l2 = linha_pos(pos2) + 4
            pos2_cod = (l2,coluna_pos(pos2))
                       
        return pos1_cod, pos2_cod   
    
def codifica_r(pos1,pos2):                   
    d=linha_pos(pos2) - linha_pos (pos1)       #diferenca entre a linha de pos2 e pos1
    h=coluna_pos(pos2) - coluna_pos (pos1)     #diferenca entre a coluna de pos 2 e pos 1
    
    pos1_cod = (linha_pos(pos2)-d,coluna_pos(pos2)) # pos1 ira ser igual a subtracao da linha de pos 2 com a diferenca entre a linha de pos2 e pos1, a coluna mantem 
    pos2_cod = (linha_pos(pos2),coluna_pos(pos2)-h) # pos2 ira ser igual a subtracao da coluna de pos 2 com a difrenca entre a coluna de pos2 e pos1 , a linha mantem
    
    return pos1_cod , pos2_cod

def codifica_digrama(digrm,chave,inc):
    s=''
    for i in range(len(chave)):         #obter a posicao do primeiro elemento de digrm
        for j in range(len(chave[i])):
            if digrm[0] == chave[i][j]:
                pos_d0=(i,j)
    for k in range(len(chave)):        #obter a posicao do segunfo elemento de digrm
        for c in range(len(chave[k])):
            if digrm[1] == chave[k][c]:
                pos_d1=(k,c)
       
    if linha_pos(pos_d0) == linha_pos(pos_d1): # se a linha de pos_d0 for igual a linha de pos_d1 recorre a funcao codifica_l
        r = codifica_l(pos_d0, pos_d1, inc)
        ch1 = chave[r[0][0]][r[0][1]]
        ch2 = chave[r[1][0]][r[1][1]]
        s = str(ch1)+str(ch2)                 # formacao da string com os caracters correspondentes as posicoes da chave introduzida
        return s
        
    elif coluna_pos(pos_d0) == coluna_pos(pos_d1): # se a coluna de pos_d0 for igual a coluna de pos_d1 recorre a funcao codifica_c
        r = codifica_c(pos_d0,pos_d1,inc)
        ch1 = chave[r[0][0]][r[0][1]]
        ch2 = chave[r[1][0]][r[1][1]]
        s = str(ch1)+str(ch2)                     #formacao da string com os caracteres correspondentes as posicoes da chave introduzida
        return s
    
    else:
        r = codifica_r(pos_d0,pos_d1)            # caso nao tenha linhas e colunas colunas recorre a funcao codifica_r
        ch1 = chave[r[0][0]][r[0][1]]
        ch2 = chave[r[1][0]][r[1][1]]
        s = str(ch1)+str(ch2)                   #formacao da string com os caracteres correspondentes as posicoes da chave introduzida
        return s  
    
def codifica(mens,chave,inc):
    s=''
    c = digramas(mens)                          #recurso a digramas para encriptar mens
    if inc == -1:
        for k in range (0,len(mens),2):                     #percorre os indices de mens de 2 em 2
            s = s + codifica_digrama(mens[k:k+2],chave,inc) #criacao da string com a desincriptacao de mens 
        return s        
    else:
        for k in range (0,len(c),2):            #percorre os indices de c de 2 em 2
            s = s + codifica_digrama(c[k:k+2],chave,inc) #criacao da string com a encriptacao de c
        return s



