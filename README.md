# AI-Document-Summarizer
This project is an AI-powered document summarizer that extracts and condenses content from PDF and TXT files using a locally hosted large language model and returns short, concise .summary with original text words count and summary words counts.

# AI-Document-Summarizer
This project is an AI-powered document summarizer that extracts and condenses content from PDF and TXT files using a locally hosted large language model and returns short, concise .summary with original text words count and summary words counts.

## ✨ Features

* Summarize **PDF** and **TXT** documents
* Uses **llama3.2** via Ollama’s **generate API**
* Fast and efficient summarization
* Fully **local inference** (secure & private)
* Simple and interactive **Swagger UI**
* Built using **FastAPI** for high performance

---

## 🛠️ Requirements

* Python **3.10+**
* FastAPI
* Uvicorn
* Requests
* pdfplumber
* Ollama (running locally)

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/AI-Document-Summarizer.git
cd AI-Document-Summarizer
```

---

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Start Ollama and pull the model

```bash
ollama serve
ollama pull llama3.2
```

---

## 🚀 Running the Application

Start the FastAPI server:

```bash
uvicorn app.api:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

Use the **/summarize** endpoint to upload a document.

---

## 📤 API Endpoint

### **POST /summarize**

Upload a **PDF or TXT** file to receive a summary.

---

### 🧪 Example Response

```json
{
  "summary": "The document highlights the significance and applications of roses across culture and industry.",
  "original_words": 142,
  "summary_words": 16
}
```

---

## 📁 Project Structure

```
AI-Document-Summarizer/
│
├── app/
│   ├── api.py              # FastAPI app with summarization endpoint
│   ├── summarizer.py       # Summary generation logic
│   ├── ollama_client.py    # Ollama API communication
│   ├── config.py           # Model and API configuration
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .venv/                  # Virtual environment (ignored in Git)
```

---

## 🔐 Privacy & Security

* All document processing happens **locally**
* No data is sent to external servers
* Suitable for confidential documents

