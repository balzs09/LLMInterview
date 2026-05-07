from core.llm import call_llm
from core.prompts.tech_prompts import  HYBRID_EVALUATOR_PROMPT, TECH_SUMMARY_PROMPT

def tech_evaluate(answer):
    return call_llm(HYBRID_EVALUATOR_PROMPT, answer)

def tech_evaluate_full(history):
    combined = ""

    for i, item in enumerate(history):
        combined += f"Technical Round {i+1}:\n"
        combined += f"Q{i+1}: {item['question']}\n"
        combined += f"A{i+1}: {item['answer']}\n\n"
        combined += f"Partial Technical Score given: {item['score']}/10\n\n"
    return call_llm(TECH_SUMMARY_PROMPT, combined)