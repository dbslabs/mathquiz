import random

def math_quiz_game():
    score = 0
    questions_asked = 0
    
    print("=========================================")
    print("      📐 WELCOME TO THE MATH QUIZ! 📐    ")
    print("=========================================")
    print("Answer the questions. Type 'quit' to exit.\n")
    
    while True:
        # 1. Randomly generate two numbers and an operation
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-"])
        
        # Calculate the correct answer behind the scenes
        if operation == "+":
            correct_answer = num1 + num2
        else:
            # Prevent negative numbers for beginners by making sure num1 is bigger
            if num1 < num2:
                num1, num2 = num2, num1  # Swap them
            correct_answer = num1 - num2
            
        # 2. Present the question to the user
        print(f"Question: What is {num1} {operation} {num2}?")
        user_input = input("Your answer: ").strip().lower()
        
        # 3. Check if the user wants to quit
        if user_input == "quit":
            print("\n=========================================")
            print("                GAME OVER                ")
            print("=========================================")
            if questions_asked > 0:
                percentage = round((score / questions_asked) * 100)
                print(f"Final Score: {score}/{questions_asked} ({percentage}%)")
            else:
                print("You didn't answer any questions!")
            print("Thanks for playing! 👋")
            break
            
        # 4. Validate input to make sure it's an integer
        try:
            user_answer = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please type a number or 'quit'.\n")
            continue  # Skip the rest of the loop and give them a new question
            
        # 5. Check if the answer is correct
        questions_asked += 1
        if user_answer == correct_answer:
            print("🎉 Correct! Great job!")
            score += 1
        else:
            print(f"😢 Incorrect. The correct answer was {correct_answer}.")
            
        # Print current progress
        print(f"Current Score: {score}/{questions_asked}\n")
        print("-" * 30)

# Run the quiz
if __name__ == "__main__":
    math_quiz_game()
