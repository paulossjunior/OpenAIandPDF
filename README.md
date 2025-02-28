# 🤖 GPT PDF Processor 📚

A Python application that extracts text from PDF documents and processes it using OpenAI's GPT models to answer questions about the document content.

## 🔎 Overview

This application provides a simple interface to:
1. 📄 Extract text from PDF documents
2. 🧠 Process the text using LangChain and OpenAI's GPT models
3. ❓ Ask questions about the document contents and receive AI-generated answers

## 👨‍🏫 Attribution

This code was originally created by [Professor Daniel Cavalieri](https://www.linkedin.com/in/daniel-cavalieri-323272123/) and adapted by [Paulo Sergio dos Santos Júnior](https://www.linkedin.com/in/paulossjunior/).

## ✅ Prerequisites

- 🐍 Python 3.6+
- 🔑 OpenAI API key

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/paulossjunior/OpenAIandPDF.git
cd OpenAIandPDF
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Usage

1. Place your PDF file in the project directory or specify the path in the code.
2. Run the main program:
```bash
python program_gpt.py
```

3. The program will:
   - 🔐 Load your OpenAI API key from the .env file
   - 📝 Process the PDF file specified in the code (default: "edital.pdf")
   - 🧩 Ask a predefined question about the document ("Qual o objetivo do Edital")
   - 📊 Print the answer from GPT

## ⚙️ Customization

To ask different questions, modify the `send_question` parameter in `program_gpt.py`:

```python
answer = gpt.send_question("Your question here")
```

To use a different PDF file, change the `pdf_path` variable:

```python
pdf_path = "your_document.pdf"
```

## 📁 Project Structure

- `program_gpt.py`: Main entry point for the application
- `fapes_gpt.py`: Contains the `GPT` class with methods for processing PDFs and interacting with the OpenAI API

## ✨ Features

- 📄 PDF text extraction
- 🔌 Integration with OpenAI's GPT models (default: gpt-4o-mini)
- 🧩 Simple API for asking questions about document content
- 🔒 Environment variable support for secure API key storage

## ⚠️ Known Issues

- The code has an error in the `__create_chain` method, where the chain assignment is missing.
- The private methods `__create_prompt`, `__chunkify_txt`, and `__get_vector` are defined but not used in the current workflow.
