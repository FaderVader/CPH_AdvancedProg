import random


weekdays = [ 
        "Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday" 
        ]


choices = [
        [ "A"],
        [ "A"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"]
        ]

def choose_random_candidate():
    return [ random.choices(choice) for choice in choices ]

def check_candidate(candidate):
    """ checks that a candidate week assigment is valid
    """
    for i in range(len(candidate) - 1):
        if candidate[i] == candidate[i + 1]:
            return False
    return True

candidate = choose_random_candidate()

for i in range(100):
    if check_candidate(candidate): break
    candidate = choose_random_candidate()


for day, choice in zip(weekdays, candidate):
    print(day, choice)
