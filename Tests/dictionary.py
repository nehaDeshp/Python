dictionary = {

    "John" : [50,40,57,78],
    "Amy" : [60,46,67,76],
    "Ellen" : [57,90,92,100],
    "Reggie" : [10,4,5,4],
    "Pennie" : [80,90,47,68],
}

print(dictionary)

sum=0
#Average score of all students
for name,score in dictionary.items():
    for i in range(len(score)):
        sum=sum+score[i]
print("The average of all students is : ",sum/len(dictionary))
sum=0
#Students whose score is more than 100
print("----------------------------------------")
for name,score in dictionary.items():
    for i in range(len(score)):
        sum=sum+score[i]
    if(sum > 100):
        print("Students who scored more than 100 : ",name, ":", sum)
    sum=0;