# 🤖 CrewAI Learning Project — Automated Research & Article Generator

A simple **multi-agent AI system** built using CrewAI that automatically:

- Researches a topic from the web 🌐  
- Extracts key insights 🧠  
- Generates a structured article ✍️  

This project demonstrates how **agent-based AI workflows** can replace single-prompt LLM systems for better structure, modularity, and scalability.

---

## 📁 Project Structure

```text
crewai-learning/
│
├── config/
│   ├── agents.yaml        # Agent definitions (role, goal, backstory)
│   └── tasks.yaml         # Task definitions (description, output)
│
├── src/
│   ├── agents.py          # Loads agents from YAML
│   ├── tasks.py           # Loads tasks from YAML
│   ├── tools.py           # Serper search tool setup
│   └── crew.py            # Crew orchestration
│
├── outputs/
│   └── output.txt         # Final generated article
│
├── screenshots/
│   └── example_run.png
│
└── requirements.txt
````

---

## 🚀 What This Project Does

Given a topic like:

```text
AI in Healthcare
```

The system automatically:

1. Searches the internet for relevant information
2. Extracts important trends and insights
3. Structures the information
4. Writes a clean, readable article

---

## 🔄 Workflow

```text
User Topic
   ↓
Research Agent (Web Search via Serper)
   ↓
Structured Research Output
   ↓
Writer Agent (Gemini LLM)
   ↓
Final Article (Markdown/Text)
```

---

## 🤖 Agents

### 🔍 Research Agent

* Searches the web for relevant information
* Identifies trends, risks, and opportunities
* Collects structured insights

**Tool used:** Serper API (Google Search)

---

### ✍️ Writer Agent

* Uses research output
* Converts findings into a readable article
* Formats output in markdown/text

**Tool used:** Gemini 2.5 Flash LLM

---

## ⚙️ Configuration (YAML-Based)

Instead of hardcoding agents and tasks in Python, this project uses YAML configuration files.

### Why YAML?

* Cleaner code
* Easier to update prompts
* No need to modify Python logic
* Better scalability for new agents

---

## 🧠 Example: Agents (`config/agents.yaml`)

```yaml
researcher:
  role: Senior Researcher
  goal: Research and analyze {topic}
  backstory: Expert in identifying tech trends and insights

writer:
  role: Tech Writer
  goal: Write engaging articles about {topic}
  backstory: Skilled in simplifying complex technical ideas
```

---

## 📄 Example: Tasks (`config/tasks.yaml`)

```yaml
research_task:
  description: Research latest trends in {topic}
  expected_output: Structured research report

write_task:
  description: Write article using research findings
  expected_output: Markdown article with clear sections
```

---

## 🛠 Tech Stack

* 🧠 CrewAI — Multi-agent orchestration
* 🔎 Serper API — Google Search integration
* 🤖 Google Gemini — LLM for generation
* 🐍 Python — Core language
* 🔧 PyYAML — Configuration handling
* 📦 python-dotenv — Environment variable management

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd crewai-learning
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

---

### 4. Run the Project

```bash
python src/crew.py
```

---

## 📤 Output

Final generated article is saved in:

```text
outputs/output.txt
```

It includes:

* Summary of topic
* Key trends
* Market insights
* Future outlook

---

## 💡 Why This Project Matters

Traditional LLM apps:

* Single prompt → single response
* Limited reasoning structure
* Hard to scale workflows

This project demonstrates:

✔ Multi-step reasoning
✔ Agent-based decomposition
✔ Tool usage (search + LLM)
✔ Real workflow orchestration

---

## 🧭 Future Improvements

* Add Fact Checker Agent
* Add SEO Optimization Agent
* Switch fully to `@CrewBase` architecture
* Add vector database memory
* Deploy using FastAPI
* Add UI using Streamlit or Next.js

---

## 👨‍💻 Author

Built as a learning project for understanding CrewAI and agentic AI systems.