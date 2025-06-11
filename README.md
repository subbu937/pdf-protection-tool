# PDF Protection Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A simple command-line tool to password-protect PDF files using Python.

## 🔐 Features
- Add password protection to any PDF file
- Lightweight and easy to use
- Terminal-based tool with colorful output

## 📦 Requirements

- Python 3.8+
- Packages: `PyPDF2`, `pyfiglet`

Install with:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python pdf_protect.py <input_pdf> <output_pdf> <password>
```

**Example**:

```bash
python pdf_protect.py "What is Linux.pdf" kali.pdf 8520
```

## 🛠️ Setup (Kali Linux / Virtual Environment Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run:

```bash
python pdf_protect.py "input.pdf" "output.pdf" "yourpassword"
```

Or use the helper script:

```bash
chmod +x run.sh
./run.sh "input.pdf" "output.pdf" "yourpassword"
```

## 📁 Project Structure

```
pdf-protection-tool/
│
├── pdf_protect.py       # Main script
├── requirements.txt     # Dependencies
├── run.sh               # Quick run helper
├── README.md            # Project overview
├── LICENSE              # MIT License
└── .gitignore           # Ignore venv and cache files
```

## 📸 Screenshots

*(Upload images in the repo and link here like below)*

```markdown
![Screenshot](screenshot.png)
```

## 📄 License

This project is licensed under the MIT License.
