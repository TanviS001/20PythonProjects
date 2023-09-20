quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question3": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("correct")
        score = score + 1
        print("Your score is: ", score)
        print(" ")
        print(" ")
    else:
        print("Wrong!")
        print("Corrct answer is: ", value['answer'])
        print("your score is : ", score)
        print(" ")
        print(" ")

print("You got ", str(score), "out of 7")
print("Your percentage is : ", score/7*100, "%")
