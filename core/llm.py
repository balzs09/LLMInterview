
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq()


def call_llm(system_prompt, user_prompt):
    try:

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            temperature=1.0,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop= None
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Hiba történt az LLM hívásakor: {e}"