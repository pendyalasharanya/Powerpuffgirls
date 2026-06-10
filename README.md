# 🎓 CampusGuide Hyderabad

> An AI-Powered College Information Assistant for Hyderabad Students

CampusGuide Hyderabad is an intelligent chatbot that helps students explore colleges in Hyderabad through natural language conversations. Instead of browsing multiple websites, students can simply ask questions about admissions, courses, fees, placements, facilities, eligibility criteria, campus life, and more.

🌐 **Live Demo:** https://powerpuffgirls-8eidqrtu3jvpead88exr9d.streamlit.app

---

## 🚀 Problem Statement

Students often spend hours searching through multiple college websites to gather information about admissions, courses, fee structures, placements, hostel facilities, and eligibility criteria.

Information is scattered across different websites, making comparison and decision-making difficult.

CampusGuide Hyderabad solves this problem by providing a single AI-powered platform that answers college-related queries instantly.

---

## ✨ Key Features

### 🤖 AI-Powered Conversations
- Natural language question answering
- Context-aware responses
- Student-friendly explanations

### 🏛️ Hyderabad College Database
- Information about 30+ colleges and universities
- Engineering, Management, Law, Science and Degree colleges
- Admissions and eligibility details

### 📚 Academic Information
- Courses offered
- Departments and specializations
- Affiliation details
- Program information

### 💼 Career & Placement Insights
- Placement-related information
- Industry-focused programs
- Emerging technology specializations

### 🌐 Smart Information Retrieval
- College database matching
- Website content extraction
- Context-based responses

### 📱 Modern User Interface
- Responsive Streamlit UI
- Interactive chat interface
- College explorer sidebar
- Session statistics

---

## 🏛️ Colleges Covered

### Universities
- JNTU Hyderabad
- Osmania University
- University of Hyderabad
- Mahindra University
- Anurag University
- Woxsen University
- ICFAI University
- KL University Hyderabad

### Engineering Colleges
- CBIT
- GNITS
- GRIET
- CVR College of Engineering
- VNR VJIET
- MGIT
- MJCET
- KMIT
- SNIST
- IARE
- CMRCET
- CMRTC
- Vardhaman College of Engineering
- ACE Engineering College
- TKR College of Engineering
- BVRIT
- BVRIT Women's College
- Lords Institute of Engineering and Technology
- Guru Nanak Institutions
- Malla Reddy Engineering College

### Specialized Institutions
- IIIT Hyderabad
- NALSAR University
- ISB Hyderabad
- NIT Warangal
- St. Ann's College
- Methodist College
- Stanley College
- Aurora University

---

## 🛠️ Tech Stack

### Frontend
- Streamlit
- HTML/CSS
- Custom UI Components

### Backend
- Python

### AI & LLM
- Groq API
- Llama 3.3 70B Versatile

### Data Collection
- BeautifulSoup
- Requests
- LXML

### Configuration
- Python Dotenv

### Deployment
- Streamlit Community Cloud

---

## 📂 Project Structure

```text
campus_chatbot/
│
├── app.py
├── chatbot.py
├── scraper.py
├── colleges_config.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/pendyalasharanya/Powerpuffgirls.git
cd Powerpuffgirls
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application is deployed on Streamlit Community Cloud.

### Live Application

🔗 https://powerpuffgirls-8eidqrtu3jvpead88exr9d.streamlit.app

---

## 🎯 Sample Questions

Try asking:

- What courses are offered in GNITS?
- Tell me about CBIT placements.
- What is the admission process for JNTUH?
- Which college is best for CSE in Hyderabad?
- Tell me about Mahindra University.
- What are the fees at GRIET?
- Compare GNITS and CBIT.

---

## 👥 Team

### Powerpuffgirls

- Vyshnavi Pittala
- Team Members

---

## 🔮 Future Enhancements

- College comparison feature
- Scholarship recommendations
- Placement analytics dashboard
- Admission deadline alerts
- Multi-city college database
- Voice-based interaction
- Personalized college recommendations

---

## 📜 License

This project was developed for educational and hackathon purposes.

---

⭐ If you found this project useful, consider giving the repository a star.