## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]

mean = sum(distribution)/len(distribution)

summ = 0
for i in distribution:
    summ += i
    mean_2 = summ/len(distribution)
    
center = False

equal_distances = True

## 3. The Mean as a Balance Point ##

import numpy as np
from numpy.random import randint, seed

valores_inf_1 = []
valores_sup_1 =[]
equal_distances = 0

# 1º, criar um for loop 5000x, e a cada uma destas 5000 iterações criar uma serie de valores completamente aleatórios, q podem assumir o valor minimo de 0 e o valor máximo de 1000, não exedendo o tamanho de 10 unidades. Criar também uma variável média, que é cálculada para cada uma destas séries de 10  unidades:
for i in range(5000):
    np.random.seed(i)
    a = np.random.randint(low=0,high=1000, size=10)
    #print(a)
    mean = sum(a)/len(a)
# 2º, em cada iteração destas 5000 iterações, vamos fazer um for loop para cada uma daquelas listas de 10 valores aleatórios apuradas à pco. E para cada um dos seus valores, se esse valor for inferior à média, vamos calcular a diferença da média dessa serie, para esse mesmo valor, arredondar para 1 casa decimal, e dp vamos adicionar esse valor apurado à lista criada acima - valores_inf_1:    
    for value in a:
        if value < mean:
            #print(round(mean - value, 1))
            distancias_inf = round(mean - value, 1)
            valores_inf_1.append(distancias_inf)
# 3º, em cada iteração destas 5000 iterações, vamos fazer um for loop para cada uma daquelas listas de 10 valores aleatórios apuradas à pco. E para cada um dos seus valores, se esse valor for superior à média, vamos calcular a diferença desse valor, para a média dessa mesma serie, arredondar para 1 casa decimal, e dp vamos adicionar esse valor apurado à lista criada acima - valores_sup_1:             
    for value in a:
        if value > mean:
            #print(round(value - mean, 1))
            distancias_sup = round(value - mean, 1)
            valores_sup_1.append(distancias_sup)
# 4º, ainda em cada uma das 5000 iterações vamos verificar se a soma dos valores que pertencem à lista - valores_inf_1, é igual à soma d todos os valores pertencentes à lista - valores_sup_1. E se assim for, por cada igualdade acrescentamos o valor 1 À lista - equal_distances. Isto é para verificar se a média se situa ao meio das somas das diferenças para esse mesmo valor, para a média, quer as diferenças dos valores que se situam abaixo da média, quer as diferenças dos valores que se situam acima da média:
    if round(sum(valores_inf_1),1) == round(sum(valores_sup_1),1):
        equal_distances += 1
                    

    

# Sacar todos os valores abaixo da média usando uma list comprehension:
valores_inf = [value for value in a if value < mean]

# Sacar todos os valores abaixo da média usando uma list comprehension:
valores_sup = [value for value in a if value > mean]

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False 

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def mean(lista):
    soma = 0
    for i in lista:
        soma += i
        média = soma/len(lista)
    return média

mean_1 = mean(distribution_1)
mean_2 = mean(distribution_2)
mean_3 = mean(distribution_3)

## 6. Introducing the Data ##

houses = pd.read_csv('AmesHousing_1.txt', sep='\t')

houses.head()

one = True
two = False
three = True

## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])

pandas_mean = houses['SalePrice'].mean()

means_are_equal = function_mean == pandas_mean

## 8. Estimating the Population Mean ##

parameter = houses['SalePrice'].mean()
sample_size = 5

sample_sizes = []
sampling_errors = []

for i in range(101):
    sample = houses['SalePrice'].sample(sample_size , random_state = i)
    statistic = sample.mean()
    sampling_error = parameter - statistic
    sampling_errors.append(sampling_error)
    sample_sizes.append(sample_size)
    sample_size += 29
    
import matplotlib.pyplot as plt
plt.scatter(sample_sizes, sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')


##########################################################################
amostra_n = 5
amostra = []
erros = []

for i in range(101):
    amostras = houses['SalePrice'].sample(amostra_n, random_state=i)
    estatistica = amostras.mean()
    erro = parameter - estatistica
    erros.append(erro)
    amostra.append(amostra_n)
    amostra_n +=29
    
    
    
    

## 9. Estimates from Low-Sized Samples ##

import matplotlib.pyplot as plt

amostra_mean_lst = []

for i in range(10000):
    amostra = houses['SalePrice'].sample(100, random_state=i)
    amostra_mean = amostra.mean()
    amostra_mean_lst.append(amostra_mean)
 
print(len(amostra_mean_lst))


plt.hist(amostra_mean_lst)
plt.axvline(houses['SalePrice'].mean())

plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0, 500000)

plt.show()

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]

population_mean = sum(population)/len(population)

samples = []
for i in population:
    sample = random.sample(population, 2)
    sample_means = sum(sample)/len(sample)
    samples.append(sample_means)

sample_samples = sum(samples)/len(samples)

unbiased = sample_samples == population_mean