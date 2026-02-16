# 📌 TalentScout Hiring Assistant 🤖

An AI-powered interview chatbot designed for hiring teams to automatically collect candidate details and generate tailored technical questions based on a candidate’s tech stack. Built with Streamlit and a Large Language Model API for an intelligent conversational screening experience.

---

## 🧠 Project Overview

TalentScout Hiring Assistant is a smart AI chatbot that performs initial candidate screening for technical recruitment.

The chatbot:

- Collects structured candidate information
- Maintains conversation context
- Generates technical questions based on declared skills
- Simulates a recruiter-style interview flow

This reduces manual recruiter effort while ensuring consistent candidate evaluation.

---

## ⚙️ Features

✔ Interactive conversational UI  
✔ Candidate information collection  
✔ Tech-stack based question generation  
✔ Context-aware dialogue  
✔ Exit keyword support  
✔ GDPR-aware in-memory data handling  
✔ Clean Streamlit interface  
✔ Cloud deployment ready  

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sk-moin/Hiring-Assistant-Chatbot.git
cd Hiring-Assistant-Chatbot
```

### 2. Create environment

Using Conda:
conda create -n venv python=3.11
conda activate venv

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add API key

Create a .env file:

OPENROUTER_API_KEY=your_key_here

### 5. Run the chatbot:

streamlit run app.py

### 6. Open browser:

http://localhost:8501

## Flow

Chatbot greets candidate

Collects profile details

Asks tech stack

Generates 3–5 tailored technical questions

Ends conversation politely

User can type:

exit / quit / bye

to end anytime.


## 🧰 Technical Details

Language: Python

UI Framework: Streamlit

LLM Backend: OpenRouter API

Session Memory: Streamlit session_state

Prompt Engine: Structured LLM prompting

Data Handling: In-memory simulation (privacy safe)


## ✍ Prompt Design

Prompts were engineered to:

Gather structured candidate information

Generate only 3–5 technical questions

Avoid unnecessary text

Maintain interviewer tone

Handle diverse tech stacks

Example:

You are a technical interviewer.
Generate ONLY 3–5 concise interview questions about:
{tech_stack}
Return numbered questions only.

This ensures predictable, recruiter-ready outputs.

## ☁️ Cloud Deployment (AWS CodePipeline → Elastic Beanstalk)

This project supports automated cloud deployment using AWS CI/CD tools.

Every time code is pushed to GitHub, AWS automatically builds and deploys the chatbot.

### Deployment Steps

* 1. Prepare project

    Ensure repository contains:
    
    app.py
    requirements.txt
    Procfile
    .gitignore
    
    Create a Procfile:
    
    web: streamlit run app.py --server.port 8080 --server.address 0.0.0.0

* 2. Create Elastic Beanstalk App

      Open AWS Console
      
      Go to Elastic Beanstalk
      
      Create Application
      
      Choose Python platform
      
      Upload repo or zip
      
      AWS generates a public URL.

* 3. Setup CodePipeline

    Open AWS CodePipeline
    
    Create pipeline
    
    Source → GitHub
    
    Deploy → Elastic Beanstalk
    
    Select your application
    
    Now every push:
    
    git push origin main
    
    triggers automatic deployment.


### Result

Live production chatbot available via AWS URL.

Automatic CI/CD enabled.

Recruiters can access demo instantly.
