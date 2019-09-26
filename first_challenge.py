#%%
def problem1(st):
    j = 0
    for i in range(len(st)):
        j = i+j
        count = 0
        for j in range(len(st)):
            if st[i] == st[j]: count += 1

        if count > len(st)/2: return st[i]
    return -1

problem1([2,3,2,1,3,3,2,2,2])


#%%
def convertRoman2Number(input):
    nums = {'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1}
    sum = 0
    for i in range(len(input)):
        value = nums[input[i]]
        
        # verifica se estar no final e se o da frente é maior que o de tras
        if i+1 < len(input) and nums[input[i+1]] > value:
            sum -= value
        else: sum += value
            
           
    return sum
      
convertRoman2Number("IX")

#%%

def problema3(numero, limMultiplicacao, modulo):
    lista = list(str(numero))[::-1]
    print(lista[0])
    lim = 2
    Multiplicacaosoma = 0
    for i in range(1,len(lista)):
        if lim > limMultiplicacao:
            lim = 2
        Multiplicacaosoma += int(lista[i])*lim
        lim+=1

    if Multiplicacaosoma*10 % modulo == int(lista[0]):
        return 1
    return 0

numero = 2615338
limMult = 5
modulo = 11
print("Saida P3 = ", end='')
if problema3(numero,limMult,modulo):
    print("Digito Valido")
else:
    print("Digito invalido")


# def main():
#     # Teste básico do problema 1
#     vetorP1 = [2,1,7,2,2,8,2]
#     print("Saida P1 =", problema1(vetorP1))

# 	# Teste básico do problema 2
#     stringP2 = "MCMLXXXV"
#     print("Saida P2 =", problema2(stringP2))

# 	# Teste básico do problema 3
#     numero = 2615338
#     limMult = 5
#     modulo = 11
#     print("Saida P3 = ", end='')
#     if problema3(numero,limMult,modulo):
#         print("Digito Valido")
#     else:
#         print("Digito invalido")



#%%
