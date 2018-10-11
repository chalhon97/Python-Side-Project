#This program averages test scores for each student and the total class


#Get the number of students
num_students=int(input("How many students are there : "))

    #validate number of students
while num_students <0:
    print ("ERROR: The amount of students cannot be negative")
    num_students=int(input("Enter the correctnumber of students: "))


#Get the number of test scores per student
num_test_scores=int(input("How many test scores per student? : "))

    #validate number of tests
while num_test_scores <0:
    print ("ERROR: The amount of test scores cannot be negative")
    num_test_scores=int(input("Enter the correct number of test scores: "))
    
#Initialize accumulator for all test scores
total_all = 0.0

#Determine Each Students Average Test Score
for student in range(num_students):
    #Initialize an accumlator for test scores.
    total=0.0
    #Get a students test scores.
    print("Student number", student + 1)
    print ("----------------")
    for test_num in range(num_test_scores):
        print("Test number", test_num + 1, end="")
        score= float(input(": "))
        #Add the score to the accumulator
        total += score
        total_all += score

    #Calculate the average test score for this student
    average = total / num_test_scores

    #Display the average
    print("The average for student number", student +1,
              "is: ", average, "\n")
    
print("----------------")
print("Overall Class Average = ", total_all/num_students)
print()

