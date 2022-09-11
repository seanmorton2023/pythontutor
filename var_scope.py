
pressure = 103.9

def adjust(t):
    #what's local, what's global?
    temperature = t * 1.43 / pressure
    return temperature

def celsius(temp2):
    temperature = 1.8 * (temp2 - 32)
    return temperature

t_i = 199.5
adjust(t_i)

#what's the expected output?
print(str(pressure))
print(str(t))
print(str(temperature))

#---question 2---#

temperature = celsius(t_i)
print(temperature)


#----question 3---#

t = 1
temp2 = celsius(adjust(t_i))
print(temp2)


