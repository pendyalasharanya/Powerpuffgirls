"""
chatbot.py - Uses Groq (free, no quota issues) as the LLM.
"""
import os
from groq import Groq
from colleges_config import HYDERABAD_COLLEGES, GENERAL_INFO
from scraper import get_college_content

_CLIENT = None

def init_groq():
    """Initialize the Groq client using the API key from environment."""
    global _CLIENT  # pylint: disable=global-statement
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return False
    _CLIENT = Groq(api_key=api_key)
    return True


def build_context(question):
    """Build context from college database relevant to the question."""
    q = question.lower()
    relevant = []

    for name, data in HYDERABAD_COLLEGES.items():
        name_lower = name.lower()
        full_lower = data["full_name"].lower()
        name_match = name_lower in q
        tag_match = any(t in q for t in data["tags"])
        word_match = any(w in q for w in full_lower.split() if len(w) > 3)
        if name_match or tag_match or word_match:
            relevant.append((name, data))

    if not relevant:
        keywords = [
            "engineering", "law", "business", "mba",
            "btech", "arts", "science", "medical"
        ]
        for kw in keywords:
            if kw in q:
                for name, data in HYDERABAD_COLLEGES.items():
                    if kw in " ".join(data["tags"]) and (name, data) not in relevant:
                        relevant.append((name, data))
                        if len(relevant) >= 4:
                            break
                break

    if not relevant:
        relevant = list(HYDERABAD_COLLEGES.items())[:5]

    context_parts = [GENERAL_INFO]
    colleges_used = []

    for name, data in relevant[:2]:
        scraped = get_college_content(name, data["url"])
        part = (
            f"\nCOLLEGE: {data['full_name']} ({name})\n"
            f"Location: {data['location']}\n"
            f"Type: {data['type']} | Established: {data['established']}\n"
            f"Affiliation: {data['affiliation']}\n"
            f"Phone: {data['phone']} | Email: {data['email']}\n"
            f"Website: {data['url']}\n"
            f"Description: {data['description']}\n"
            f"Tags: {', '.join(data['tags'])}\n"
        )
        if scraped:
            part += f"Website Content: {scraped[:1000]}\n"
        context_parts.append(part)
        colleges_used.append(name)

    return "\n\n".join(context_parts), colleges_used


def ask(question, history):
    """Ask a question and return the answer and colleges referenced."""
    global _CLIENT  # pylint: disable=global-statement
    if _CLIENT is None and not init_groq():
        return "⚠️ GROQ_API_KEY not found. Please set it in your .env file.", []

    context, colleges = build_context(question)

    history_text = ""
    for h in history[-2:]:
        history_text += f"User: {h['user']}\nAssistant: {h['assistant']}\n\n"

    prompt = (
    "You are CampusGuide AI, an expert educational counselor for Hyderabad colleges.\n\n"

    "Answer confidently and naturally.\n"
    "Use the college information provided in the database.\n"
    "Do not repeatedly say 'information is not available in the database'.\n"
    "If some details are missing, provide a helpful overview based on the college profile.\n"
    "Only recommend visiting the official website when very specific information is requested.\n"
    "Keep answers student-friendly, informative and professional.\n"
    "Use bullet points whenever appropriate.\n"
    "Mention courses, facilities, placements and admissions whenever relevant.\n\n"

    f"COLLEGE DATABASE:\n{context}\n\n"
    f"CONVERSATION HISTORY:\n{history_text}\n"
    f"USER QUESTION: {question}\n\nANSWER:"
)

    try:
        chat = _CLIENT.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        return chat.choices[0].message.content, colleges
    except (ValueError, RuntimeError) as e:
        return f"Error: {str(e)}", []


SUGGESTED_QUESTIONS = [
    "What are the top engineering colleges in Hyderabad?",
    "How do I apply to JNTU Hyderabad?",
    "What is EAMCET and how does it work?",
    "Tell me about IIIT Hyderabad admissions",
    "Which colleges offer MBA in Hyderabad?",
    "What are the fees at CBIT?",
    "Tell me about NIT Warangal placements",
    "What courses does Osmania University offer?",
    "Tell me about ISB Hyderabad PGP program",
    "Which is the best college for CSE in Hyderabad?",
]
