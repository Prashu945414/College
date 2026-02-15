import time 

start_time = time.time()

score = 0

q1 = { "Q.": "Who is president of U.S.?",
      "Options": ["A.Donald Trump","B.George Washington","C.Nelson Mandela"],
      "answer": "A"}

q2 = {"Q.": "What is largest Forest ?",
      "Options": ["A.Sahara", "B.Amazon","C.Mangrove"],
      "answer": "B"
}

Quiz = [q1,q2]

for q in Quiz:
    print(q["Q."])
    for option in q["Options"]:
        print(option)
    user = input("Enter answer ")

    if user == q["answer"]:
    
        print("Correct Answer")
        score+=10
    else:
    
        print("Incorrect Answer ")
        
stop_time = time.time()

Time_Taken = stop_time - start_time

print("Your final score is ", score )

print("time taken: ", Time_Taken) 