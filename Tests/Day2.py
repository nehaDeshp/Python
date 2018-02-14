
#Assignment 1

side1 = input("Enter Side 1")
side2 = input("Enter Side 2")
side3 = input("Enter Side 3")

if(side1 == side2 and side2 == side3):
    print("Equilateral Triangle")
elif(side1 != side2 and side2 != side3 and side3!= side1):
    print("Scalene Triangle")
else:
    print("Isoceles Triange")


#Assignment 2

original_price_list = [4.95,9.85,14.95,19.95,24.95]
discounted_price_list=[];
for i in range(len(original_price_list)-1):
    discounted_price_list.append(original_price_list[i] - (original_price_list[i] * 0.60))
for m,n in zip(original_price_list,discounted_price_list):
    print ("%0.2f,%0.2f"%(m,n))



