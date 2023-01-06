import random
num_questions = 10
points = 0
for i in range(num_questions):
    num1 = random.randint(1, 50)
    num2 = random.randint(1,50)
    answer = int(input("What is {} * {} ". format(num1, num2)))
    if (answer == num1 * num2 ) :
        points+=1
        print("correct!")
    else:
        print("not correct")







