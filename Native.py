#for list apel fruit in form of list
apel = [100, 200, 150, 100, 120, 80, 90, 160, 110, 170]

weight_total = 0 #variable to keep weight total of all apel

for i in range(len(apel)):
    weight_total = weight_total + apel[i] #calculate all apel weight
    
avg_apel = weight_total / len(apel)
print(avg_apel)

#Median Example
import math
def bubblesort(elements):
    for n in range (len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
    return elements

def calc_median(elements):
    elements = bubblesort(elements)
    len_element = len(elements)
    if len_element % 2 is 0:
        center = math.floor(len_element/2)
        return (elements[center-1] + elements[center]) / 2
    else:
        return elements[math.cell(len_element/2)-1]
    
apel = [100, 200, 150, 100, 120, 80, 90, 160, 110, 170]
median = calc_median(apel)
print(median)