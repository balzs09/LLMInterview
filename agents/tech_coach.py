from core.llm import call_llm
from core.prompts.tech_prompts import TECH_COACH_PROMPT

def tech_coach(last_question, last_answer, last_feedback):
    context = f"""
    Last Question: {last_question}
    Last Answer: {last_answer}
    Last Feedback: {last_feedback}
    """
    return call_llm(TECH_COACH_PROMPT, context)