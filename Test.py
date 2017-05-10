

dict = {"test":[1,2,3]}
key = dict["test"]

print key

TEMPQUESTION = {"Test":[["IncorrectA", False], ["IncorrectB", False], ["CorrectC", True], ["IncorrectD", False]]}

choice = 1

for answer in TEMPQUESTION:
    if TEMPQUESTION[answer][choice][1] == True:
        print "correct"
    else:
        print "incorrect"




Question|AnswerA|AnswerB|AnswerC|AnwserD