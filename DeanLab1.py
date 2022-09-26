name =input("What is your name? ")
print ('Hello World')
##########################
print ("Hello",name,"!")
a = 38.4
b = a* 1.8 + 32
print (str(a) + " Celcius")
print (str(b) + " Farenheit")
##########################
batted = 1014
notout = 162
runs = 48426
inningscomp = batted - notout
battingaverage = runs/inningscomp
print("Boycott had a batting average of", battingaverage, "!")
##########################
total=input("How many people in your class: ")
group=int(total) // 24
remainder=int(total) % 24
print("The amount of full groups is " + str(group))
print("The amount of students left over is " + str(remainder))