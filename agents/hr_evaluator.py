from core.llm import call_llm
from core.prompts.hr_prompts import HR_EVALUATOR_PROMPT, HR_SUMMARY_PROMPT

def hr_evaluate(answer):
    return call_llm(HR_EVALUATOR_PROMPT, answer)

def hr_evaluate_full(history):
    combined = ""

    for i, item in enumerate(history):
        combined += f"Round {i + 1}:\n"
        combined += f"Q{i+1}: {item['question']}\n"
        combined += f"A{i+1}: {item['answer']}\n\n"
        combined += f"Partial Score given: {item['score']}/10\n\n"
    return call_llm(HR_SUMMARY_PROMPT, combined)