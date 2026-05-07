from core.llm import call_llm
from core.prompts.hr_prompts import HR_INTERVIEWER_PROMPT

def hr_ask_question(history):
    is_first_question = len(history) == 0
    context = ""
    for entry in history:
        context += f"Q{entry['question']}\nA: {entry['answer']}\n"

    instruction = "This is the start of the interview. Introduce yourself." if is_first_question else "Continue the interview without repeating topics."
    user_prompt =f"{instruction}\n\nHistory so far:\n{context}\n\nAsk the next question:"

    return call_llm(HR_INTERVIEWER_PROMPT, user_prompt)
