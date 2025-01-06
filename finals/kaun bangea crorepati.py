# create a program capable of displaying questions to the user like KBC
# use list data type to store questions and their correct answers 
# display the final amount the person is taking home after playing the game 



questions = ["How many continents are there?", "What is the capital of India?", "NG mei kaun se course padhaya jaata hai?"]
options = [["1.Four", "2.Nine", "3.Seven", "4.Eight"], 
           ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"], 
           ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
answers=[3,4,1]

def play_game():

    print("Welcome to Kaun Banega Crorepati")
    print("Here are the rules:")
    print('1)For every correct answer you get $10,000.')
    print('2)If you provide any one answer wrong you loose , and game ends with winning amount. ')
    
    total_prize=0
    for i in range(len(questions)):
        print(f"\nQuestion {i+1}: {questions[i]}")
        print("Options are:")
        for option in options[i]:
            print(option)
        user_answer=int(input("Enter your choice(1/2/3/4):"))
        if (user_answer)==answers[i]:
            total_prize+=10000
            print("Correct Answer! You've won $10,000")
        else:
            print("Wrong Answer! Game Over.")
            break
    
    print(f"Thank you for playing! You can take home ${total_prize}")


            

play_game()



