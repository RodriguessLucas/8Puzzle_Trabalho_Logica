from pysat.solvers import Glucose3

#deixando os tamanhos maximos de tabuleiro e do valor usado
VALOR_MAXIMO = 9
TAMANHO_MAXIMO = 3

#instancia o glucose(vazio)
g = Glucose3()


def addClasulasEmGlucose(lista):
   contador = 0
   for clasula in lista:
      contador+=1
      g.add_clause(clasula)
      

def gerarDictClasulaVariavel(passo):
    auxDicionario = {}
    contador = 1

    for k in range(VALOR_MAXIMO):
        for i in range(TAMANHO_MAXIMO):
            for j in range(TAMANHO_MAXIMO):
                auxClasula = "{}_P_{}_{}_{}".format(passo,i+1,j+1, k)
                auxDicionario.update({
                    auxClasula: contador
                })
                contador+=1
        
    return auxDicionario


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






#arrumar o de ser p ^ -p 
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
    
    addClasulasEmGlucose(listaNovasClasulas)      
    return listaNovasClasulas         
      
        

            





# funcao auxiliar

def imprimir_dicionario_linha_a_linha(meu_dicionario):
  """
  Imprime cada par de chave e valor de um dicionário em uma nova linha.

  Argumentos:
    meu_dicionario (dict): O dicionário a ser impresso.
  """
  if not isinstance(meu_dicionario, dict):
    print("Erro: O argumento fornecido não é um dicionário.")
    return

  if not meu_dicionario:
    print("O dicionário está vazio.")
    return

  print("--- Conteúdo do Dicionário ---")
  for chave, valor in meu_dicionario.items():
    # Usamos uma f-string para formatar a saída de forma clara
    print(f"Chave: {chave} | Valor: {valor}")
  print("-----------------------------")




#PARA O PASSO 1

#gera o dicionario passo1
dicionarioClasulasPassoUm = gerarDictClasulaVariavel(1)  

#imprimi
imprimir_dicionario_linha_a_linha(dicionarioClasulasPassoUm)

#gerar clasulas que para cada quadrado do 8 puzzle pode ter um valor
listaPodeTerUmValor = gerarListaClasulasPeloMenosUm(dicionarioClasulasPassoUm)

#gerar clasulas que para cada quadrado do 8 puzzle so pode ter exclusivamente um valor
listaPodeSoUmValor = gerarListaClasulasSoPodeUm(listaPodeTerUmValor)


print("----------------------------------------------------")
print("Impimindo as clasulas de so pode ter um valor")
for aa in listaPodeTerUmValor:
   print(aa)
print("----------------------------------------------------")


print("----------------------------------------------------")
print("Impimindo as clasulas de so pode ter um valor")
for aa in listaPodeSoUmValor:
   print(aa)
print("----------------------------------------------------")





# fomato do git hub para add clasula
#g.add_clause([-1, 2])
#g.add_clause([-2, 3])
#print(g.solve())
#print(g.get_model())
#True
#[-1, -2, -3]
