import time
import threading

def timed_input(prompt, timeout):
    """Get input with timeout. Returns None if timeout exceeded."""
    answer = [None]

    def input_thread():
        answer[0] = input(prompt)

    thread = threading.Thread(target=input_thread)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        return None
    return answer[0]

def run_quiz(questions, time_per_question=15):
    score = 0
    total = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"  {idx}. {option}")

        print(f"You have {time_per_question} seconds to answer.")
        start_time = time.time()

        answer = timed_input("Your answer (number): ", time_per_question)

        if answer is None:
            print("\n⏰ Time's up! You didn't answer in time.")
            print(f"The correct answer is: '{q['answer']}'.")
            continue

        try:
            answer = int(answer)
            if not (1 <= answer <= len(q['options'])):
                print(f"Invalid choice. Must be between 1 and {len(q['options'])}. Counting as wrong.")
                print(f"The correct answer is: '{q['answer']}'.")
                continue
        except ValueError:
            print("Invalid input. Counting as wrong.")
            print(f"The correct answer is: '{q['answer']}'.")
            continue

        chosen = q['options'][answer - 1]
        if chosen.lower() == q['answer'].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! You chose '{chosen}'. The correct answer is: '{q['answer']}'.")

        elapsed = time.time() - start_time
        print(f"Answered in {elapsed:.1f} seconds.")

    percentage = (score / total) * 100
    print(f"\nQuiz complete! You scored {score} out of {total} ({percentage:.2f}%).")

    save = input("Do you want to save your results? (y/n): ").strip().lower()
    if save == 'y':
        with open("quiz_results.txt", "a") as f:
            f.write(f"Score: {score}/{total} ({percentage:.2f}%)\n")
        print("Results saved to quiz_results.txt")

if __name__ == "__main__":
    sample_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "2"],
            "answer": "4"
        },
        {
            "question": "Which language is this program written in?",
            "options": ["Java", "C++", "Python", "Ruby"],
            "answer": "Python"
        }
    ]

    run_quiz(sample_questions)