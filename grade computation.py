# A program that calculates Scores and assign Grades

print ('How many test did you give out?')
# It allows you to input your how many test you gave out
Answer = input()
if Answer == '1':
    # Allows you to input the test score
    print ('Enter the test Score: ')
    firstScore = int (input())
    secondScore = 0
    TestScore = firstScore + secondScore
    print ('The Test Score is: %s' % (TestScore))
elif Answer == '2':
    # Allows you to input the first test score
    print ('Enter the first test Score: ')
    firstScore = int (input())
    # Allows you to input the Second test score
    print('Enter the second test Score: ')
    secondScore = int (input())
    TestScore = firstScore + secondScore
    print ('The Test Score is: %s' % (TestScore))
    # Allows you to input the Exam score
print ('Enter the exam Score: ')
ExamScore = int (input())
Sum = TestScore + ExamScore
print ('The Sum of both scores is: %s' % (Sum))
# Assign Grades to Scores
if Sum > 100:
    print ('Invalid Score')
elif Sum >= 75:
    print ('Your grade is: A')
elif Sum >= 70:
    print ('Your grade is: AB')
elif Sum >= 65:
    print ('Your grade is: B')
elif Sum >= 60:
    print ('Your grade is: BC')
elif Sum >= 55:
    print ('Your grade is: C')
elif Sum >= 50:
    print ('Your grade is: CD')
elif Sum >= 45:
    print ('Your grade is: D')
elif Sum >= 40:
    print ('Your grade is: E')
elif Sum < 40:
    print ('Your grade is: F')
    print ('You failed the course')
    print ('Try again in another Semester')