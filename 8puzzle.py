from pysat.solvers import Glucose3

#deixando os tamanhos maximos de tabuleiro, do valor usado e movimentações
contador = 0
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
    auxDicionario = {}

    global contador

    for k in range(VALOR_MAXIMO):
        for i in range(TAMANHO_MAXIMO):
            for j in range(TAMANHO_MAXIMO):
                auxClasula = "{}_P_{}_{}_{}".format(passo,i+1,j+1, k)
                auxDicionario.update({
                    auxClasula: contador
                })
                contador+=1
        
    return auxDicionario

#  funcao para definir que cada quadradinho tem que assumir um valor ao menos
def gerarListaClasulasPeloMenosUm(dicionarioClasulas):
   listaClasulas = []
   for i in range(TAMANHO_MAXIMO):
        for j in range(TAMANHO_MAXIMO):
           auxClasula = []
           for k in range(VALOR_MAXIMO):
                auxChaveEncontrar = "1_P_{}_{}_{}".format(i+1,j+1,k)
                auxValorClasula = dicionarioClasulas[auxChaveEncontrar]
                auxClasula.append(auxValorClasula)
           listaClasulas.append(auxClasula)
            
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
  
  return listaClasulasNovas
      

# funcao para definir que cada valor so pode assumir um quadrado apenas
def gerarListaClasulasSoPodeUmTabuleiro(clasulas):
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
         
  return listaNovasClasulas     
            




            





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
  for chave, valor in dicionario.items():
    # Usamos uma f-string para formatar a saída de forma clara
    print(f"Chave: {chave} | Valor: {valor}")
  print("-----------------------------")


def imprimirRestricoes(lista, texto):
  print("----------------------------------------------------")
  print(texto)
  for aa in lista:
    print(aa)
  print("----------------------------------------------------")








#PARA O PASSO 1

# gera o dicionario passo1
dicionarioClasulasPassoUm = gerarDictClasulaVariavel(1)  

# gerar clasulas que para cada quadrado do 8 puzzle deve assumir um valor
listaPodeTerUmValor = gerarListaClasulasPeloMenosUm(dicionarioClasulasPassoUm)

# gerar clasulas que para cada quadrado do 8 puzzle so pode ter exclusivamente um valor
listaPodeSoUmValor = gerarListaClasulasSoPodeUm(listaPodeTerUmValor)


# gera clasulas para que no tabuleiro, um valor deva assumir a posicao em algum quadrado
listaCadaValorAssumeEmTabuleiro = gerarListaClasulasValorDeveAssumirUm(dicionarioClasulasPassoUm,1)

# gera clasula para que no tabuleiro so exista valoroes unicos
# (nao repetir o valor 2  em 2 ou mais quadrados por exemplo)
listaSoPodeUmValorTabuleiro = gerarListaClasulasSoPodeUmTabuleiro(listaCadaValorAssumeEmTabuleiro)




# prints de cada função para verificar
imprimirDicionarioLinhaLinha(dicionarioClasulasPassoUm)

imprimirRestricoes(listaPodeTerUmValor,"Impimindo as clasulas de pode ter um valor")
imprimirRestricoes(listaPodeSoUmValor,"Impimindo as clasulas de so pode ter um valor")
imprimirRestricoes(listaCadaValorAssumeEmTabuleiro, "Impimindo as clasulas que cada valor assume um quadrado em tabuleiro")
imprimirRestricoes(listaSoPodeUmValorTabuleiro,"Impimindo as clasulas que cada valor assume apenas um quadrado em tabuleiro")



# fomato do git hub para add clasula
#g.add_clause([-1, 2])
#g.add_clause([-2, 3])
#print(g.solve())
#print(g.get_model())
#True
#[-1, -2, -3]
