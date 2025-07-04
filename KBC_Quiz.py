questions = [
    "1. What is the powerhouse of the cell?",
    "2. Who developed the theory of general relativity?",
    "3. What is the value of Pi up to 3 decimal places?",
    "4. In which year did World War II end?",
    "5. What is the largest internal organ in the human body?",
    "6. What programming language is primarily used for iOS app development?",
    "7. What is the hardest natural substance on Earth?",
    "8. Who painted the ceiling of the Sistine Chapel?",
    "9. What is the smallest prime number?",
    "10. Which element has the atomic number 1?",
    "11. What is the capital city of Canada?",
    "12. Who is the author of 'Brave New World'?",
    "13. Which gas makes up most of the Earth's atmosphere?",
    "14. In which organ of the human body would you find the hippocampus?",
    "15. Which planet has the most moons?",
    "16. What is the longest river in the world?",
    "17. Who composed the Four Seasons?",
    "18. What is the derivative of sin(x)?",
    "19. What year did the Berlin Wall fall?",
    "20. What is the main language spoken in Brazil?"
]

options = [
    "A) Nucleus\nB) Mitochondria\nC) Ribosome\nD) Chloroplast",
    "A) Isaac Newton\nB) Nikola Tesla\nC) Albert Einstein\nD) Galileo Galilei",
    "A) 3.124\nB) 3.141\nC) 3.142\nD) 3.154",
    "A) 1942\nB) 1945\nC) 1939\nD) 1950",
    "A) Brain\nB) Heart\nC) Liver\nD) Lungs",
    "A) Java\nB) Python\nC) Swift\nD) Kotlin",
    "A) Steel\nB) Quartz\nC) Diamond\nD) Obsidian",
    "A) Leonardo da Vinci\nB) Michelangelo\nC) Raphael\nD) Donatello",
    "A) 0\nB) 1\nC) 2\nD) 3",
    "A) Helium\nB) Hydrogen\nC) Oxygen\nD) Carbon",
    "A) Toronto\nB) Vancouver\nC) Ottawa\nD) Montreal",
    "A) George Orwell\nB) J.D. Salinger\nC) Aldous Huxley\nD) Ray Bradbury",
    "A) Oxygen\nB) Nitrogen\nC) Carbon Dioxide\nD) Hydrogen",
    "A) Brain\nB) Liver\nC) Kidney\nD) Lungs",
    "A) Earth\nB) Jupiter\nC) Saturn\nD) Neptune",
    "A) Nile\nB) Amazon\nC) Yangtze\nD) Mississippi",
    "A) Bach\nB) Beethoven\nC) Mozart\nD) Vivaldi",
    "A) cos(x)\nB) -cos(x)\nC) -sin(x)\nD) tan(x)",
    "A) 1985\nB) 1989\nC) 1991\nD) 1993",
    "A) Portuguese\nB) Spanish\nC) French\nD) Italian"
]

answers = [
    "b",  # Mitochondria
    "c",  # Einstein
    "c",  # 3.142
    "b",  # 1945
    "c",  # Liver
    "c",  # Swift
    "c",  # Diamond
    "b",  # Michelangelo
    "c",  # 2
    "b",  # Hydrogen
    "c",  # Ottawa
    "c",  # Aldous Huxley
    "b",  # Nitrogen
    "a",  # Brain
    "b",  # Jupiter
    "a",  # Nile
    "d",  # Vivaldi
    "a",  # cos(x)
    "b",  # 1989
    "a"   # Portuguese
]

def quiz():
    pts = 0
    print("Welcome to the quiz! Type 'quit' anytime to exit.\n")
    for i in range(len(questions)):
        while True:
            print(questions[i])
            print(options[i])
            ans = input("Your answer: ").strip().lower()

            if ans in ['quit', 'exit']:
                print(f"Quiz ended. You won {pts} points. Goodbye!")
                return

            if ans not in ['a', 'b', 'c', 'd']:
                print("Invalid input! Please answer with A, B, C, or D.\n")
                # retry the same question without ending
                continue  

            if ans == answers[i]:
                pts = 1000 * pow(2, i)
                print(f"Correct! Your current points: {pts}\n")
                break  # next question

            else:
                # wrong answer with valid input ends the quiz
                if pts == 0:
                    print("You didn’t win anything this time. Just kidding! Give it another try!")
                else:
                    print(f"Wrong answer. You won {pts} points so far!")
                return  # end quiz here

    print(f"Congratulations! You completed the quiz with {pts} points!")

quiz()