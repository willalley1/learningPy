import math as m

radius = float(input("enter radius of circle: \n")) 

tau = m.tau # pi * 2

pi = m.pi # ~3.14

inf = m.inf # Infinite

circ = f"{tau * radius}\n{radius *(pi*2)}" 

area = f"{pi * (radius * radius)}"

print("\nSpace is %s\n" %inf)

print(f'\nPi is: {pi}\n')

print(f'\nThe radius of your circle is {radius},\n the circumfrence is {circ:.6},\n and the area is {area:.6}\n') # notice {area:.6} says i want to show 6 places of the area including the decimal

# print(tau, print(circ, print(pi))) # Uhmmm Errr.... Not sure if this could ever be useful

weight = float(input("\nWhats your weight in pounds?: \n"))

height = float(input(f"\nYou weight {weight:.6} pounds,\nWhats your height in inches?:\n"))

bmi = 703 * weight / (height**2)

print("\nYou weigh %s pounds, You're %s inches tall, and your BMI is %s\n" %(weight, height, bmi)) 
