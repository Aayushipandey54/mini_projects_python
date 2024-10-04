class Question :

    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:

    def __init__(self):

        self.questions=[]

    def add_question(self,question):

        self.questions.append(question)

    def take_quiz(self):

        print("\nPlease answer the following questions: \n")

        self.score = 0 # reset score for new quiz

        for question in self.questions:

            user_answer = input(question.prompt)

            if user_answer.lower() == question.answer.lower():

                self.score += 1

        print(f"\nYour score : {self.score}/{len(self.questions)}")

        self.display_results()

    def display_results(self):

        if self.score == len(self.questions):
            
            print("\nCongratulations! You have passed the quiz.\n")

        elif self.score >= len(self.questions)/2:
                
                print("\nYou have passed the quiz.\n")

        else:
                
                print("\nYou have failed the quiz.\n")

def main():
     
    quiz = Quiz()

    question = [
         
        Question("what is the capital of France?\n(a) Paris\n(b) Madrid\n(c) Rome\n\n","a"),
        Question("what is capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Kolkata\n\n","a"),
        Question("what is 100+47+98?\n(a) 145\n(b) 245\n(c) 245\n\n","b"),
        Question("what is integer in python?\n(a) 1.0\n(b) 1\n(c) 1.0\n\n","b"),
        Question("what is the language use in web development?\n(a) Python\n(b) Java\n(c) HTML\n\n","c"),
        Question("what is language use in machine learning?\n(a) Python\n(b) Java\n(c) HTML\n\n","a"),
        Question("what is the Gradient Descent?\n(a) Optimization Algorithm\n(b) Machine Learning Algorithm\n(c) Deep Learning Algorithm\n\n","a"),
        Question("what is deep learning stand for?\n(a) Machine Learning\n(b) Artificial Intelligence\n(c) Neural Network\n\n","c"),
        Question("what is DBMS stand for?\n(a) Database Management System\n(b) Data Management System\n(c) Data Base Management System\n\n","a"),
     ]

    for question in question :
             
            quiz.add_question(question)
    
    while True:

        print("/n----Exam Prepration App----\n")

        print("1. Take Quiz\n")

        print("2.add a new question\n") 

        print("3. Exit\n")

        choice = input("select an option (1-3): ")

        if choice == "1":
                 
                quiz.take_quiz()

        elif choice == "2":
             
             prompt = input("enter the question :")

             answer = input("enter the answer :")

             quiz.add_question(Question(prompt,answer))

             print("\nQuestion added successfully.\n")

        elif choice == "3":
                 
                 print("\nThank you for using the Exam Prepration App.\n")
                 break

        else:          
                 print("\nInvalid choice. Please select a valid option.\n")  

if __name__ == "__main__":
         
        main()


