from core.llm import call_llm
from core.prompts.hr_prompts import HR_COACH_PROMPT

def hr_coach(last_question, last_answer, last_feedback):
    context = f"""
    Last Question: {last_question}
    Last Answer: {last_answer}
    Last Feedback: {last_feedback}
    """
    return call_llm(HR_COACH_PROMPT, context)