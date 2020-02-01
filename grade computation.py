# A program that calculates Scores and assign Grades

print ('How many test did you give out?')
# It allows you to input your how many test you gave out
answer = input()
if answer == '1':
    # Allows you to input the test score
    print ('Enter the test Score: ')
    firstScore = int (input())
    secondScore = 0
    testScore = firstScore + secondScore
    print ('The Test Score is: %s' % (testScore))
elif answer == '2':
    # Allows you to input the first test score
    print ('Enter the first test Score: ')
    firstScore = int (input())
    # Allows you to input the Second test score
    print('Enter the second test Score: ')
    secondScore = int (input())
    testScore = firstScore + secondScore
    print ('The Test Score is: %s' % (testScore))
    # Allows you to input the Exam score
print ('Enter the exam Score: ')
examScore = int (input())
SumOfScores = testScore + examScore
print ('The Sum of both scores is: %s' % (SumOfScores))
# Assign Grades to Scores
if SumOfScores > 100:
    print ('Invalid Score')
elif SumOfScores >= 75:
    print ('Your grade is: A')
elif SumOfScores >= 70:
    print ('Your grade is: AB')
elif SumOfScores >= 65:
    print ('Your grade is: B')
elif SumOfScores >= 60:
    print ('Your grade is: BC')
elif SumOfScores >= 55:
    print ('Your grade is: C')
elif SumOfScores >= 50:
    print ('Your grade is: CD')
elif SumOfScores >= 45:
    print ('Your grade is: D')
elif SumOfScores >= 40:
    print ('Your grade is: E')
elif SumOfScores < 40:
    print ('Your grade is: F')
    print ('You failed the course')
    print ('Try again in another Semester')
