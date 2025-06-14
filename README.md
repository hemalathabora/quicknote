# 📒 QuickNote - Flask Note Taking App

QuickNote is a simple yet powerful note-taking web application built using **Flask**. It allows users to create, pin, edit, delete, and organize notes by tags, with features like full-text search, filtering, and note export.

---

## 🚀 Features

- 📝 Add and view notes
- 📌 Pin or unpin important notes
- 🔍 Search notes by keywords
- 🏷️ Filter notes by tags
- ✏️ Edit and delete notes
- 📂 Export notes as text files
- 📖 Click to read note in detail


## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (no frameworks)
- **Database:** SQLite (via SQLAlchemy)

---

## 📁 Project Structure

```

quicknote/
├── app.py                 # Main Flask app
├── database.db            # SQLite DB (generated at runtime)
├── templates/             # HTML templates
│   ├── index.html
│   ├── add\_note.html
│   ├── edit\_note.html
│   └── view\_note.html
├── static/                # (Optional) Static files like CSS/JS
├── .gitignore
├── requirements.txt
└── README.md

````

---

## 🧪 Getting Started

### 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/<your-username>/quicknote.git
cd quicknote
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

Then open your browser at [http://localhost:5000](http://localhost:5000)

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`. To generate it:

```bash
pip freeze > requirements.txt
```

**Live Project** 👉 [Click to Open quicknote](https://quicknote-1goa.onrender.com)
Example dependencies:

```text
Flask
Flask-SQLAlchemy
```


