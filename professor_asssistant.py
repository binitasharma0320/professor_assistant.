import random

def read_question_bank(file_path):
    """
    Reads the question bank and returns a list of (question, answer) pairs.
    Each question is followed by its answer in the next line.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("The file path you entered cannot be found. Please try again.")
        return None

    # Clean and remove empty lines
    cleaned = [line.strip() for line in lines if line.strip() != ""]

    qa_pairs = []

    # Pair question and answer lines
    i = 0
    while i < len(cleaned) - 1:
        question = cleaned[i]
        answer = cleaned[i + 1]
        qa_pairs.append((question, answer))
        i += 2

    return qa_pairs


def create_exam(qa_pairs, num_requested, output_file):
    """
    Selects num_requested random question-answer pairs
    and writes them to output_file.
    """
    selected = random.sample(qa_pairs, num_requested)

    with open(output_file, "w", encoding="utf-8") as f:
        for q, a in selected:
            f.write(q + "\n")
            f.write(a + "\n\n")


def professor_assistant():
    # Welcome message
    print("Welcome to Professor Assistant version 1.0.")

    # Ask professor name
    name = input("Please Enter Your Name: ").strip()
    print(f"Hello Professor {name}, I am here to help you create exams from a question bank.")

    # Main loop
    while True:
        choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit)? ").strip().lower()

        if choice == "no":
            print(f"Thank you Professor {name}. Have a good day!")
            break

        elif choice == "yes":
            # Step 1: ask for question bank path
            path = input("Please Enter the Path to the Question Bank: ").strip()
            qa_pairs = read_question_bank(path)

            # If file path invalid, return to loop
            if qa_pairs is None:
                continue

            print("Yes, the path you provided contains questions and answers.")

            # Step 2: ask how many pairs to include
            while True:
                try:
                    num = int(input("How many question-answer pairs do you want to include in your exam? "))
                    if num <= 0:
                        print("Please enter a positive number.")
                    elif num > len(qa_pairs):
                        print(f"The question bank only contains {len(qa_pairs)} pairs. Please enter a smaller number.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")

            # Step 3: ask where to save the exam
            output_file = input("Where do you want to save your exam? ").strip()

            # Step 4: create the exam
            create_exam(qa_pairs, num, output_file)

            print(f"Congratulations Professor {name}. Your exam has been created and saved in {output_file}.")

        else:
            print("Invalid choice. Please type Yes or No.")


# Run the program
professor_assistant()
