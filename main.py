import codecs
import time
import sys
import re
import readline
from agents.hr_interviewer import hr_ask_question
from agents.hr_evaluator import hr_evaluate, hr_evaluate_full
from agents.tech_interviewer import tech_ask_question
from agents.tech_evaluator import tech_evaluate, tech_evaluate_full
from agents.hr_coach import hr_coach
from agents.tech_coach import tech_coach

def extract_score(evaluation_text):

    match =  re.search(r"Score:\D*(\d+)", evaluation_text)
    if match:
        return int(match.group(1))
    return 0
def get_multiline_input():

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

if sys.stdin.encoding != "utf-8":
    sys.stdin.reconfigure(encoding="utf-8")

def hr(is_practice=False):
    history = []
    for i in range(3):
        # Question of the interviewer
        question = hr_ask_question(history)
        print("\nQuestion:", question)

        answer = get_multiline_input()

        if answer.strip().lower() == "quit":
            sys.exit()
        # unic feedback
        eval_text = hr_evaluate(answer)
        current_score = extract_score(eval_text)

        print("\nQuick feedback:")
        print(eval_text)
        history.append({
            "question": question,
            "answer": answer,
            "score": current_score
        })
        if  is_practice:
            #improved version
            print("\nImproved:")
            print(hr_coach(question,answer,eval_text))
        else:
            if  current_score < 3:
                print("\n" + "!" * 40)
                print("CRITICAL FAILURE: Your last answer did not meet the minimum professional standards.")
                print("The interview process is terminated immediately.")
                print("!" * 40)
                return False



    # final evaluation
    full_eval_text = hr_evaluate_full(history)
    total_score = sum(item['score'] for item in history)
    final_score = int(total_score/len(history) + 0.5)
    print("\nFinal score:", final_score)
    print("\n=== FINAL EVALUATION ===")
    print(full_eval_text)
    if  is_practice:
        return True
    else:
        if final_score >= 7:
            print("\n CONGRATULATIONS! ")
            print(f"Your final HR score is {final_score}/10. You are proceeding to the TECHNICAL ROUND.")
            print("Please wait for the Senior Architects to join the call...")

            return True

        elif 6 <= final_score < 7:
            print("\n ALMOST THERE...")
            print(f"You scored a {final_score}/10. You showed great potential and values, but the")
            print("Technical Lead requires a minimum score of 7 to move forward to the hard-skills round.")
            print("Thank you for your time, we'll keep your CV on file!")
            return False

        else:
            print("\n REJECTION")
            print(f"A final score of {final_score}/10 is not sufficient for this position.")
            print("Thank you for your interest in TechNova Solutions.")
            return False


def tech(is_practice):
    history = []
    for i in range(3):
        # Question of the interviewer
        question = tech_ask_question(history)
        print("\nQuestion:", question)

        answer = get_multiline_input()

        if answer.strip().lower() == "quit":
            sys.exit()
        # unic feedback
        eval_text = tech_evaluate(answer)
        current_score = extract_score(eval_text)

        print("\nQuick feedback:")
        print(eval_text)
        history.append({
            "question": question,
            "answer": answer,
            "score": current_score
        })
        if  is_practice:
            print("\nImproved:")
            print(tech_coach(question,answer,eval_text))
        else:
            if  current_score < 3:
                print("\n" + "!" * 40)
                print("CRITICAL FAILURE: Your last answer did not meet the minimum professional standards.")
                print("The interview process is terminated immediately.")
                print("!" * 40)
                return False



    # final evaluation
    full_eval_text = tech_evaluate_full(history)
    total_score = sum(item['score'] for item in history)
    final_score = int(total_score / len(history) + 0.5)
    print("\nFinal score:", final_score)
    print("\n=== FINAL EVALUATION ===")
    print(full_eval_text)
    if not is_practice:
        if final_score >= 8:
            print("\n CONGRATULATIONS! ")
            print(f"Your final technical score is {final_score}/10. You got the job.")
            print("We will inform you later when you can start")

            return True

        elif 6 <= final_score < 8:
            print("\n ALMOST THERE...")
            print(f"You scored a {final_score}/10. You showed great potential and values, but the")
            print("Job requires a minimum score of 8.")
            print("Thank you for your time, we'll keep your CV on file!")
            return False

        else:
            print("\n REJECTION")
            print(f"A final score of {final_score}/10 is not sufficient for this position.")
            print("Thank you for your interest in TechNova Solutions.")
            return False
    else:
        return True

def main():
    print("If you want to practice press P, if you want to simulate an interview press S.")
    letter_pressed = input()
    is_practice = letter_pressed == "P"
    hr_success = hr(is_practice)
    if hr_success:
        tech(is_practice)

if __name__ == "__main__":
    main()