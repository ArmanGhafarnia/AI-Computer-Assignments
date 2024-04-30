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
    for i in range(0,first_population_number):
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
        first_population.append(val)



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



first_population = list()
first_population_number = 12
var_numbers = 0
p_numbers = 0
paranteses = list()


read()
creat_answer()
xlist = []
ylist = []
templist = list()
for i in range(2000):
    xlist.append(i)
    
    templist = list()
      
    print([first_population[i].fitness for i in range(first_population_number) ])
    
    first_population.sort(key = lambda e:e.fitness)
    
    print([first_population[i].fitness for i in range(first_population_number) ])
         
    for j in range(6):
        u = first_population[len(first_population) - j -1 ]
        templist.append(u)
        
        

    print([templist[i].fitness for i in range(6) ])  
    first_population.clear()
    first_population.extend(templist)
    
    
    for j in range(3):
        crossoverlist = list()
        for k in range(2):
            rand = random.randint(0, len(templist)-1) 
            crossoverlist.append(templist[rand])

        cros1 = answer(crossoverlist[0].value, 0)
        cros2 = answer(crossoverlist[1].value, 0)
        crossoverpoint = random.randint(5, 95)        
        for k in range(crossoverpoint,100):
            temp = cros1.value[k]
            cros1.value[k] = cros2.value[k]
            cros2.value[k] = temp
        
        rand = random.randint(0, 99)
        
        
        cros1.value[rand] = not cros1.value[rand]
        cros2.value[rand] = not cros2.value[rand]
        

            
        cros1.fitness = solver(cros1.value)
        cros2.fitness = solver(cros2.value)
        first_population.append(cros1)
        
        print([first_population[i].fitness for i in range(len(first_population)) ])

        first_population.append(cros2)
        
        print([first_population[i].fitness for i in range(len(first_population)) ])
    
    
    print("===================================") 

    best_pop = []
    for l in range(len(first_population)):
        fit = solver(first_population[l].value)
        best_pop.append(fit)
    
    ylist.append(max(best_pop))

    
matplotlib.pyplot.scatter(xlist,ylist)
matplotlib.pyplot.show()












    
