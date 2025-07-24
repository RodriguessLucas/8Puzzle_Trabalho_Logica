from pysat.solvers import Glucose3

#deixando os tamanhos maximos de tabuleiro, do valor usado e movimentações
contador = 1
VALOR_MAXIMO = 9
TAMANHO_MAXIMO = 3
ADJACENCIAS = {
  1: [2,4],
  2: [1,3,5],
  3: [2,6],
  4: [1,5,7],
  5: [2,4,6,8],
  6: [3,5,9],
  7: [4,8],
  8: [5,7,9],
  9: [6,8]
}

# instancia o glucose(vazio)
g = Glucose3()


# adiciona a clasula ao glucose
def addRestricoesGlucose(lista):
   for clasula in lista:
      g.add_clause(clasula)
    

def addClasulasGlucose(dicionario):
   for valor in dicionario.values():
      g.add_clause([valor])

 

# gera as clasulas e armazena em um dicionario
def gerarDictClasulaVariavel(passo):
    global contador
    auxDicionario = {}
    for k in range(VALOR_MAXIMO):
        for i in range(TAMANHO_MAXIMO):
            for j in range(TAMANHO_MAXIMO):
                auxClasula = "{}_P_{}_{}_{}".format(passo,i+1,j+1, k)
                auxDicionario.update({
                    auxClasula: contador
                })
                contador+=1
        
    return auxDicionario


# Gerar as ações que pode fazer
def gerarDictAcoes(passo):
  global contador
  auxDicionario = {}

  auxDicionario.update( {f"{passo}_A_C" : (contador+0) })
  auxDicionario.update( {f"{passo}_A_B" : (contador+1) })
  auxDicionario.update( {f"{passo}_A_D" : (contador+2) })
  auxDicionario.update( {f"{passo}_A_E" : (contador+3) })
  
  
  contador += 4

  addClasulasGlucose(auxDicionario)
  
  return auxDicionario



#  funcao para definir que cada quadradinho tem que assumir um valor ao menos
def gerarListaClasulasPeloMenosUm(dicionarioClasulas,passo):
  listaClasulas = []
  for i in range(TAMANHO_MAXIMO):
    for j in range(TAMANHO_MAXIMO):
      auxClasula = []
      for k in range(VALOR_MAXIMO):
        auxChaveEncontrar = "{}_P_{}_{}_{}".format(passo,i+1,j+1,k)
        auxValorClasula = dicionarioClasulas[auxChaveEncontrar]
        auxClasula.append(auxValorClasula)
      listaClasulas.append(auxClasula)

  addRestricoesGlucose(listaClasulas)
            
  return listaClasulas

# funcao para definir que so pode ter um valor em cada quadrado
def gerarListaClasulasSoPodeUm(clasulas):
  listaNovasClasulas = []
  tamanhoClasula = len(clasulas[0])
    
  if(tamanhoClasula <=0):
    print("Erro, lista de clasulas está vazia")
    return -1
    
  for i in range(len(clasulas)):
    for j in range(tamanhoClasula):
      for k in range(j+1,tamanhoClasula):
        var1 = clasulas[i][j] * -1
        var2 = clasulas[i][k] * -1
        listaNovasClasulas.append([var1,var2])

  addRestricoesGlucose(listaNovasClasulas)
         
  return listaNovasClasulas         
      

# funcao para definir que cada valor precisa assumir algum quadrado
def gerarListaClasulasValorDeveAssumirUm(dicionario,passo):
  listaClasulasNovas = []
  for i in range(VALOR_MAXIMO):
    auxCriarClasula = []
    for j in range(TAMANHO_MAXIMO):
      for k in range(TAMANHO_MAXIMO):
        auxChaveDic = "{}_P_{}_{}_{}".format(passo,j+1,k+1,i)
        auxObterValor = dicionario[auxChaveDic]
        auxCriarClasula.append(auxObterValor)    
    listaClasulasNovas.append(auxCriarClasula)

  addRestricoesGlucose(listaClasulasNovas)
  
  return listaClasulasNovas
      

# funcao para definir que cada valor so pode assumir um quadrado apenas
def gerarListaClasulasValorUnicoPorTabuleiro(clasulas):
  listaNovasClasulas = []
  tamanhoClasula = len(clasulas[0])

  if(tamanhoClasula <= 0):
    print("Erro, lista de clasulas está vazia")
    return -1
  
  for i in range(len(clasulas)):
        for j in range(tamanhoClasula):
            for k in range(j+1,tamanhoClasula):
                var1 = clasulas[i][j] * -1
                var2 = clasulas[i][k] * -1
                listaNovasClasulas.append([var1,var2])

  addRestricoesGlucose(listaNovasClasulas)
         
  return listaNovasClasulas     
            

# falta o método de gerar as movimentacoes (todas as possibilidades)


            





# funcao auxiliar, apenas representativo

def imprimirDicionarioLinhaLinha(dicionario, texto):

  if not isinstance(dicionario, dict):
    print("Erro: O argumento fornecido não é um dicionário.")
    return

  if not dicionario:
    print("O dicionário está vazio.")
    return

  print("--- Conteúdo do Dicionário ---")
  print(f"--- {texto} ---")
  auxContador = 1
  for chave, valor in dicionario.items():
    print(f"Chave: {chave} | Valor: {valor}", end =" -- ")
    if(auxContador % 5 == 0):
      print("\n")
      auxContador = 0
    auxContador +=1
  print("\n-----------------------------")


def imprimirRestricoes(lista, texto):
  print("----------------------------------------------------")
  print(texto)

  if(len(lista) <= 10):
    for aa in lista:
      print(aa)
  else:
    auxContador = 1
    for aa in lista:
      print(aa, end=" ")
      if(auxContador % 5 == 0):
        print("\n")
        auxContador = 0
      auxContador +=1

  
  print("\n----------------------------------------------------")





def main():
  dictClasulas = {}
  listaRestricoes = []

  #dar uma organizada melhor nisso

  for i in range(1,3):
    # gera o dicionario passo1
    dictClasulasPosicoes = gerarDictClasulaVariavel(i)
    dictClasulas = {*dictClasulas, * dictClasulasPosicoes}

    # gera o dicionario dass acoes passo1
    dictClasulasAcoes = gerarDictAcoes(i)
    dictClasulas = {*dictClasulas, *dictClasulasAcoes}

    #gerar clasulas que para cada quadrado do 8 puzzle deve assumir um valor
    listaPodeTerUmValor = gerarListaClasulasPeloMenosUm(dictClasulasPosicoes,i)
    listaRestricoes = [*listaRestricoes, *listaPodeTerUmValor]

    # gerar clasulas que para cada quadrado do 8 puzzle so pode ter exclusivamente um valor
    listaPodeSoUmValor = gerarListaClasulasSoPodeUm(listaPodeTerUmValor)
    listaRestricoes = [*listaRestricoes, *listaPodeSoUmValor]


    # gera clasulas para que no tabuleiro, um valor deva assumir a posicao em algum quadrado
    listaCadaValorAssumeEmTabuleiro = gerarListaClasulasValorDeveAssumirUm(dicionario=dictClasulasPosicoes,passo = i)
    listaRestricoes = [*listaRestricoes, *listaCadaValorAssumeEmTabuleiro]

    # gera clasula para que no tabuleiro so exista valoroes unicos
    # (nao repetir o valor 2  em 2 ou mais quadrados por exemplo)
    listaSoPodeUmValorTabuleiro = gerarListaClasulasValorUnicoPorTabuleiro(listaCadaValorAssumeEmTabuleiro)
    listaRestricoes = [*listaRestricoes, *listaSoPodeUmValorTabuleiro]



    # prints de cada função para verificar
    imprimirDicionarioLinhaLinha(dictClasulasPosicoes,"Dicionario das clasulas")
    imprimirDicionarioLinhaLinha(dictClasulasAcoes,"Dicionario das ações")

    imprimirRestricoes(listaPodeTerUmValor,"Impimindo as clasulas de pode ter um valor")
    imprimirRestricoes(listaPodeSoUmValor,"Impimindo as clasulas de so pode ter um valor")
    imprimirRestricoes(listaCadaValorAssumeEmTabuleiro, "Impimindo as clasulas que cada valor assume um quadrado em tabuleiro")
    imprimirRestricoes(listaSoPodeUmValorTabuleiro,"Impimindo as clasulas que cada valor assume apenas um quadrado em tabuleiro")

    


main()





# fomato do git hub para add clasula
#g.add_clause([-1, 2])
#g.add_clause([-2, 3])
#print(g.solve())
#print(g.get_model())
#True
#[-1, -2, -3]
