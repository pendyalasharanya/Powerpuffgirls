# 🎓 CampusGuide Hyderabad — AI Campus Info Chatbot

An AI-powered chatbot for answering questions about colleges in Hyderabad, Telangana. Built for the Capabl Track A project.

---

## 🏛️ Colleges Covered

| College | Location | Type |
|--------|----------|------|
| JNTU Hyderabad | Kukatpally | University |
| Osmania University | Amberpet | University |
| CBIT | Gandipet | Engineering |
| IIIT Hyderabad | Gachibowli | Deemed University |
| NIT Warangal | Warangal | NIT |
| ISB Hyderabad | Gachibowli | Business School |
| NALSAR University | Shameerpet | Law University |
| University of Hyderabad | Gachibowli | Central University |
| VNR VJIET | Bachupally | Engineering |
| Vasavi College | Ibrahimbagh | Engineering |
| Nizam College | Basheerbagh | Arts & Science |
| MVSR Engineering | Nadergul | Engineering |
| Muffakham Jah | Banjara Hills | Engineering |
| VJIT | Bachupally | Engineering |
| St. Francis College | Begumpet | Women's College |

---

## ⚙️ Tech Stack

- **Frontend:** Streamlit with custom CSS
- **Backend:** Python + LangChain
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2` (free, no API needed)
- **Vector DB:** FAISS (local)
- **LLM:** OpenAI GPT-3.5-turbo
- **Scraping:** BeautifulSoup + requests
- **Data:** Scraped live from official college websites

---

## 🚀 Setup Instructions

### Step 1 — Clone & enter folder
```bash
git clone <your-repo>
cd campus_chatbot
```

### Step 2 — Create virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Configure API key
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenAI API key:
OPENAI_API_KEY=sk-your-key-here
```

Get your OpenAI API key from: https://platform.openai.com/api-keys

### Step 5 — Run the app
```bash
streamlit run app.py
```

The app opens at **http://localhost:8501**

---

## 📖 Usage Guide

1. **Open the app** at http://localhost:8501
2. **Enter your OpenAI API key** in the sidebar (if not in .env)
3. **Click "Load KB"** — this scrapes all college websites and builds the vector database
   - First time takes ~2-3 minutes (scraping 15+ websites)
   - Subsequent loads are instant (uses cache)
4. **Ask questions!** Examples:
   - *"What are the B.Tech fees at CBIT Hyderabad?"*
   - *"How do I apply to JNTU Hyderabad?"*
   - *"Tell me about placements at Vasavi College"*
   - *"Which college is best for CSE in Hyderabad?"*
   - *"What is EAMCET and how does it work?"*

---

## 📁 Project Structure

```
campus_chatbot/
├── app.py                  # Main Streamlit UI
├── chatbot.py              # RAG chatbot with LangChain
├── knowledge_base.py       # Vector store builder (FAISS)
├── scraper.py              # BeautifulSoup web scraper
├── colleges_config.py      # College URLs and metadata
├── requirements.txt        # Python dependencies
├── .env.example            # Environment template
├── .env                    # Your API keys (don't commit!)
└── data/
    ├── cache/              # Scraped content cache (JSON)
    └── vector_db/          # FAISS index files
```

---

## 🔄 Rebuild Knowledge Base

If college websites update:
- Click **"🔄 Rebuild"** in the sidebar — re-scrapes all websites
- Or delete the `data/` folder and click **"▶ Load KB"**

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| `OpenAI API error` | Check your API key in `.env` |
| Scraping fails for a college | That college's website may be down; cached data is used |
| Slow first load | Normal — scraping 15 websites takes ~2-3 min |
| `FAISS index not found` | Click "Load KB" or "Rebuild" in sidebar |

---

## 📦 Deployment (Streamlit Cloud)

1. Push code to GitHub (don't commit `.env` — it's in `.gitignore`)
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Add `OPENAI_API_KEY` in Streamlit Cloud → App settings → Secrets
5. Deploy!

---

## 🎯 Assessment Checklist (Track A)

- [x] GitHub repo with project structure
- [x] Python + LangChain + Streamlit + BeautifulSoup + FAISS
- [x] Document processing (web content extraction)
- [x] Web scraping for college websites
- [x] Campus info categorization (location, fees, admissions, clubs)
- [x] Streamlit chatbot interface
- [x] Deployable on Streamlit Cloud
- [x] Multi-source information retrieval
- [x] Conversation memory (last 6 exchanges)
- [x] Contact info, location, and facility details

---

Built as part of **Capabl Interactive Campus Info Chatbot Project — Track A**
