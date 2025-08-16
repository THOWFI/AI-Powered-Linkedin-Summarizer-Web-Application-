## AI-Powered LinkedIn Summarizer

An intelligent web application that extracts, processes, and summarizes information from **LinkedIn profiles** using AI.
It uses **web scraping + AI models** to quickly generate concise, professional summaries — perfect for recruiters, HR professionals, and anyone who needs quick insights.


## 📌 Features

* 🔍 **LinkedIn Profile Lookup** – Fetch profile details automatically.
* 🧠 **AI Summarization** – Uses advanced NLP models to summarize experience, skills, and background.
* 🌐 **Web Interface** – Simple Flask-based frontend for easy access.
* ⚡ **Fast & Lightweight** – Optimized Python backend with modular design.
* 🔒 **Environment Variables** – Secure API key management via `.env`.


## 🛠️ Tech Stack

* **Python 3.12+**
* **Flask** – Web framework
* **LangChain / LLM API** – For AI summarization
* **Requests / BeautifulSoup** – For LinkedIn scraping
* **Jinja2** – For rendering HTML templates


## 📂 Project Structure

```
AI-Powered-Linkedin-Summarizer-main/
│── .env_example               # Example environment variables
│── .gitignore                 # Ignore unnecessary files in Git
│── Requirements.txt           # Python dependencies
│── app.py                     # Main Flask app
│── LS.py                      # LinkedIn Summarizer logic
│── output_parsers.py          # AI output parsing
│── agents/                    # LinkedIn lookup agent
│── third_parties/             # LinkedIn API/scraping handler
│── tools/                     # Additional helper tools
│── templates/
│   └── index.html              # Frontend HTML template
```


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Powered-Linkedin-Summarizer.git
cd AI-Powered-Linkedin-Summarizer-main
```

### 2️⃣ Install Dependencies

```bash
pip install -r Requirements.txt
```

### 3️⃣ Configure Environment Variables

* Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

* You can refer to `.env_example` for guidance.

### 4️⃣ Run the Application

```bash
python app.py
```

Then visit:

```
http://127.0.0.1:5000
```


## 🧩 How It Works

1. **User enters LinkedIn profile name or URL**.
2. **LinkedIn Lookup Agent** (`agents/linkedin_lookup_agent.py`) fetches raw profile data.
3. **Third-party module** (`third_parties/linkedin.py`) handles LinkedIn scraping/API.
4. **Summarization logic** (`LS.py`) uses AI to create a concise profile summary.
5. **Output parser** (`output_parsers.py`) formats the summary for display.
6. Flask app (`app.py`) renders the results on the web interface.


## 🔮 Future Improvements

* Add **multi-language support**.
* Improve **summarization accuracy** with fine-tuned models.
* Enable **batch profile summarization**.
* Support **PDF/CSV export**.


## 📜 License

This project is not licensed for public use. 
