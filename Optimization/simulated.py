import random
import math
import matplotlib.pyplot 

class answer :
    def __init__(self,value,fitness):
        self.value = value
        self.fitness = fitness

   



def read ():
    read_f = open("input.cnf", "r")
    text = read_f.read()
    list_row = text.split("\n")
    detail_line = list_row[3].split(" ")
    global var_numbers
    var_numbers = int(detail_line[2])
    global p_numbers
    p_numbers = int(detail_line[3])
    first_line = 4
    last_line = p_numbers + first_line 
    global paranteses
    for i in range(first_line , last_line):  
        in_parantes = list()
        temp = list_row[i].split("  ")
        for j in range(0 , 3):
            in_parantes.append(int(temp[j]))

        paranteses.append(in_parantes)   
    



def creat_answer():
    global first_population
    x = list()
    for j in range(0 , var_numbers):
            temp = random.randint(1,10)
            print(temp)
            if temp < 5 :
                x.append(False)
            if temp >= 5 : 
                x.append(True)
    fit = solver(x)
    val = answer(x, fit) 
    first_population = val



def solver(member):
    fitness_score = 0
    for i in paranteses : 
        f = -1;
        for j in i:
            if j > 0: 
                if member[j-1] == True and f == -1:
                    fitness_score += 1
                    f = 1;
            if j < 0: 
                if  member[-j-1] == False and f== -1:
                    fitness_score += 1
                    f=1;        
    return fitness_score


first_population = 0;   #object
var_numbers = 0
p_numbers = 0
paranteses = list()


read()
T = 9
creat_answer()
xlist = []
ylist = []
for i in range(50000):
    xlist.append(i)
    value_temp = first_population.value

    

    r = random.randint(0, var_numbers -1)  
    r2 = random.randint(0, var_numbers-1)
    value_temp[r] = not value_temp[r]
    value_temp[r2] = not value_temp[r2]
    

    new_fitness = solver(value_temp)

    if(i%100==0):
        print(first_population.fitness)
    
    if new_fitness > first_population.fitness :
        
        first_population = answer(value_temp, new_fitness)
    else:
       
        r2 = random.uniform(0, 1)
        
        
        x = (first_population.fitness - new_fitness)

        check = math.exp(-(x)/T)
        
        if r2 < check :
            first_population = answer(value_temp, new_fitness)
    
    ylist.append(first_population.fitness)

    T = T * 0.97


matplotlib.pyplot.scatter(xlist,ylist)
matplotlib.pyplot.show()












    
