# 🔐 Password Strength Checker

A simple yet powerful Windows desktop app built with Python and Tkinter. It evaluates password strength and securely stores hashed passwords using **SHA-256 encryption**.

## 🚀 Features
- ✅ Real-time password strength feedback
- 🔒 Secure SHA-256 password hashing
- 💾 Option to store hashed passwords locally (`passwords.txt`)
- 🖼️ Clean and beginner-friendly GUI with Tkinter
- 🧪 Offline functionality — privacy-focused

## 📸 Screenshot
*Coming soon: Interface preview of the strength checker window!*

## 🛠️ How It Works
1. Enter a password
2. Click `Check Strength` to see its rating
3. Optionally, store the SHA-256 hash in a local file

## 📁 File Structure
PasswordCheckerApp/ ├── password_checker.py └── passwords.txt

## 🧰 Technologies Used
- Python 3+
- Tkinter (GUI)
- re (Regex)
- hashlib (SHA-256 encryption)

## ⚙️ Getting Started

### Prerequisites
- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Installation

```bash
git clone https://github.com/yourusername/PasswordCheckerApp.git
cd PasswordCheckerApp
python password_checker.py
💡 Ensure Python is added to PATH and all modules are installed (most are built-in).
🔒 Password Security Notes
This tool does not store plain text passwords. All entries are hashed using SHA-256 and stored locally.

📝 To-Do
[ ] Export logs as CSV or Excel

[ ] Add dark mode UI

[ ] Integrate random password generator

[ ] Package as .exe for easy distribution

📄 License
MIT License © SATYAM VIJAYAN
