'''
    Golf scores record the number of strokes used to get the ball in the hole.
    The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5).
    Each score's name is based on the actual strokes taken compared to par:
        "Eagle": number of strokes is two less than par
        "Birdie": number of strokes is one less than par
        "Par": number of strokes equals par
        "Bogey": number of strokes is one more than par
    Given two integers that represent par and the number of strokes used, write a program
    that prints the appropriate score name.
    Print "Error" if par is not 3, 4, or 5.
'''

par = int(input("Enter par: "))
strokes = int(input("Enter strokes: "))
score_name = ''

if par in range(3, 6):
    if strokes == par:
        score_name = "Par"
    elif (par - strokes) == 2:
        score_name = "Eagle"
    elif (par - strokes) == 1:
        score_name = "Birdie"
    elif (par - strokes) == -1:
        score_name = "Bogey"
else:
    score_name = "Error"

print(score_name)