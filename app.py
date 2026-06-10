import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="CampusGuide Hyderabad",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
.stApp { background: #F0EFFF !important; }
.block-container { padding: 1.5rem 2rem !important; max-width: 1300px; }

.header-box {
    background: linear-gradient(135deg, #5B4FCF 0%, #8B5CF6 100%);
    border-radius: 18px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    color: white;
}
.header-box h1 { color: white !important; font-size: 1.9rem; font-weight: 800; margin: 0 0 0.3rem; }
.header-box p  { color: rgba(255,255,255,0.85) !important; margin: 0; font-size: 0.95rem; }

.stat-box {
    background: white;
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #E0DEFF;
    box-shadow: 0 2px 12px rgba(91,79,207,0.08);
}
.stat-num   { font-size: 1.7rem; font-weight: 800; color: #5B4FCF; }
.stat-label { font-size: 0.75rem; color: #888; font-weight: 500; margin-top: 2px; }

.chat-box {
    background: white;
    border-radius: 16px;
    border: 1px solid #E0DEFF;
    padding: 1.2rem 1.4rem;
    min-height: 400px;
    max-height: 500px;
    overflow-y: auto;
    box-shadow: 0 2px 16px rgba(91,79,207,0.08);
    margin-bottom: 0.8rem;
}
.msg-user { display: flex; justify-content: flex-end; margin-bottom: 1rem; }
.msg-bot  { display: flex; justify-content: flex-start; margin-bottom: 1rem; gap: 10px; }
.bubble-user {
    background: #5B4FCF; color: white !important;
    padding: 0.75rem 1.1rem; border-radius: 18px 18px 4px 18px;
    max-width: 72%; font-size: 0.88rem; line-height: 1.6;
    box-shadow: 0 2px 8px rgba(91,79,207,0.25);
}
.bubble-bot {
    background: white; color: #1a1a2e !important;
    padding: 0.75rem 1.1rem; border-radius: 18px 18px 18px 4px;
    max-width: 72%; font-size: 0.88rem; line-height: 1.6;
    border: 1px solid #E0DEFF;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.bot-avatar {
    width: 36px; height: 36px; background: #EEF0FF;
    border-radius: 10px; display: flex; align-items: center;
    justify-content: center; font-size: 1.1rem; flex-shrink: 0; margin-top: 2px;
}
.college-tag {
    display: inline-block; background: #EEF0FF; color: #5B4FCF !important;
    font-size: 0.68rem; font-weight: 600; padding: 2px 9px;
    border-radius: 20px; margin-right: 4px; margin-top: 5px;
    border: 1px solid rgba(91,79,207,0.2);
}
.welcome-msg { text-align: center; padding: 2rem 1rem; }
.welcome-msg .emoji { font-size: 3rem; }
.welcome-msg h3 { color: #5B4FCF !important; font-weight: 700; margin: 0.5rem 0 0.3rem; }
.welcome-msg p  { color: #888 !important; font-size: 0.85rem; }

.coll-card {
    background: white; border-radius: 12px;
    border: 1px solid #E0DEFF; border-left: 4px solid #5B4FCF;
    padding: 0.8rem 1rem; margin-bottom: 0.6rem;
    box-shadow: 0 1px 8px rgba(91,79,207,0.07);
}
.coll-name { font-weight: 700; font-size: 0.83rem; color: #1a1a2e; }
.coll-meta { font-size: 0.72rem; color: #888; margin-top: 2px; }

.stTextInput input {
    border-radius: 12px !important; border: 2px solid #E0DEFF !important;
    padding: 0.7rem 1rem !important; font-size: 0.9rem !important;
}
.stTextInput input:focus { border-color: #5B4FCF !important; }
.stButton > button {
    border-radius: 12px !important; font-weight: 600 !important;
    font-size: 0.85rem !important;
}
</style>
""", unsafe_allow_html=True)

from chatbot import ask, init_groq as init_gemini, SUGGESTED_QUESTIONS
from colleges_config import HYDERABAD_COLLEGES

# Init Gemini once on startup
init_gemini()

# Session state
if "messages"     not in st.session_state: st.session_state.messages = []
if "query_count"  not in st.session_state: st.session_state.query_count = 0
if "colleges_seen" not in st.session_state: st.session_state.colleges_seen = set()
if "pending_q"    not in st.session_state: st.session_state.pending_q = None

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:0.5rem 0 1.2rem">
        <div style="font-size:2.5rem">🎓</div>
        <div style="font-weight:800;font-size:1.2rem;color:#5B4FCF">CampusGuide</div>
        <div style="font-size:0.72rem;color:#888;margin-top:2px">Hyderabad Colleges AI</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Session Stats")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-num">{st.session_state.query_count}</div>
            <div class="stat-label">Queries</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-num">{len(st.session_state.colleges_seen)}</div>
            <div class="stat-label">Colleges</div></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🏛️ Colleges Database")
    for name, data in HYDERABAD_COLLEGES.items():
        with st.expander(name):
            st.markdown(f"**{data['full_name']}**  \n📍 {data['location']}  \n🏷️ {data['type']}  \n🔗 [{data['url']}]({data['url']})")

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.query_count = 0
        st.session_state.colleges_seen = set()
        st.rerun()

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-box">
    <h1>🎓 CampusGuide Hyderabad</h1>
    <p>AI-powered information assistant for 15+ Hyderabad colleges — admissions, fees, placements, clubs & more</p>
</div>""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)
for col, (num, label) in zip([s1,s2,s3,s4], [
    ("15+","Colleges"), ("JNTU/OU/Central","Affiliations"),
    ("B.Tech→PhD","Programs"), ("Gemini AI","Powered By")]):
    with col:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── MAIN LAYOUT ───────────────────────────────────────────────────────────────
left, right = st.columns([2, 1])

with left:
    st.markdown("### 💬 Chat")

    html = '<div class="chat-box">'
    if not st.session_state.messages:
        html += """<div class="welcome-msg">
            <div class="emoji">👋</div>
            <h3>Hi! I'm CampusGuide AI</h3>
            <p>Ask me anything about colleges in Hyderabad —<br>
            admissions, fees, placements, hostel, clubs and more!</p>
        </div>"""
    else:
        for m in st.session_state.messages:
            if m["role"] == "user":
                html += f'<div class="msg-user"><div class="bubble-user">{m["content"]}</div></div>'
            else:
                tags = "".join([f'<span class="college-tag">🏛 {c}</span>'
                                for c in m.get("colleges", [])[:3]])
                body = m["content"].replace("\n", "<br>")
                html += f'''<div class="msg-bot">
                    <div class="bot-avatar">🤖</div>
                    <div class="bubble-bot">{body}<br><div style="margin-top:6px">{tags}</div></div>
                </div>'''
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    ic, bc = st.columns([5, 1])
    with ic:
        user_input = st.text_input("", placeholder="e.g. What are B.Tech fees at CBIT?",
                                   label_visibility="collapsed", key="input")
    with bc:
        send = st.button("Send ➤", use_container_width=True)

    st.markdown("**💡 Try asking:**")
    r1, r2, r3 = st.columns(3)
    for i, q in enumerate(SUGGESTED_QUESTIONS[:6]):
        col = [r1, r2, r3][i % 3]
        with col:
            label = q[:38] + "…" if len(q) > 38 else q
            if st.button(label, key=f"chip_{i}", use_container_width=True):
                st.session_state.pending_q = q
                st.rerun()

with right:
    st.markdown("### 🏛️ Featured Colleges")
    for name, data in list(HYDERABAD_COLLEGES.items())[:7]:
        tags = "".join([f'<span class="college-tag">{t}</span>' for t in data["tags"][:2]])
        st.markdown(f"""<div class="coll-card">
            <div class="coll-name">{data['full_name']}</div>
            <div class="coll-meta">📍 {data['location']} · Est. {data['established']}</div>
            <div style="margin-top:4px">{tags}</div>
        </div>""", unsafe_allow_html=True)

# ── HANDLE INPUT ──────────────────────────────────────────────────────────────
def handle(question):
    if not question.strip():
        return

    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.query_count += 1

    history = []
    msgs = st.session_state.messages
    for i in range(0, len(msgs) - 1, 2):
        if msgs[i]["role"] == "user" and i+1 < len(msgs) and msgs[i+1]["role"] == "assistant":
            history.append({"user": msgs[i]["content"], "assistant": msgs[i+1]["content"]})

    with st.spinner("🔍 Searching college database..."):
        answer, colleges = ask(question, history)

    for c in colleges:
        st.session_state.colleges_seen.add(c)

    st.session_state.messages.append({
        "role": "assistant", "content": answer, "colleges": colleges
    })
    st.rerun()

if st.session_state.pending_q:
    q = st.session_state.pending_q
    st.session_state.pending_q = None
    handle(q)
elif send and user_input:
    handle(user_input)

st.markdown("---")
st.markdown("""<div style="text-align:center;color:#aaa;font-size:0.75rem">
🎓 CampusGuide Hyderabad · Powered by Google Gemini · Data from official college websites
</div>""", unsafe_allow_html=True)
