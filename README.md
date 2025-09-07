# 📄 IntelliDocs: Your Conversational PDF Assistant

IntelliDocs is an intelligent web application that allows you to have conversations with your PDF documents. Built with Python, LangChain, and Streamlit, it leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers based solely on the content of your uploaded files.

---

### 🚀 Live Demo

**https://intellidocs-pdf-assistant-v3j5wuohgyjvm2ex8fx2nd.streamlit.app/**

---

### ✨ Key Features

* **Interactive Chat Interface:** Ask questions in natural language and get answers directly from your document.
* **Retrieval-Augmented Generation (RAG):** Ensures answers are accurate and grounded in the provided text, eliminating model "hallucinations."
* **Conversational Memory:** Remembers previous questions to provide context-aware follow-up answers.
* **Powered by LangChain:** Utilizes the latest and most robust components from the LangChain ecosystem for chaining, retrieval, and memory.
* **Flexible Model Support:** Easily switch between powerful cloud APIs (OpenAI) and private, local models (Ollama/Llama 3).

---

### 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.2-222222?style=for-the-badge&logo=langchain)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai)
![FAISS](https://img.shields.io/badge/FAISS-1.8-blue?style=for-the-badge)

---

### ⚙️ Project Architecture

The application follows a Retrieval-Augmented Generation (RAG) pipeline:

1.  **Document Ingestion:** A PDF document is loaded and split into smaller, manageable text chunks.
2.  **Embedding & Indexing:** Each chunk is converted into a numerical vector (embedding) using OpenAI's models and stored in a FAISS vector database for efficient searching.
3.  **User Query:** The user asks a question through the Streamlit interface.
4.  **Retrieval:** The user's question is embedded, and the FAISS database finds the most semantically similar text chunks from the document.
5.  **Generation:** The original question and the retrieved text chunks are passed to the LLM (e.g., GPT-4o-mini), which generates a final, context-aware answer.

---

### 🔧 Installation & Usage

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/luxan-shanmugalingam/IntelliDocs-PDF-Assistant.git
    cd IntelliDocs-PDF-Assistant
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    * Create a file named `.env` in the root of the project.
    * Add your OpenAI API key to the file:
        ```
        OPENAI_API_KEY="sk-..."
        ```

5.  **Run the indexing script (one-time setup):**
    * Place your PDF in the root directory.
    * Run the script to create your vector store.
        ```bash
        python create_index.py  # Assuming you create a separate script for this
        ```

6.  **Launch the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

---

### 🤔 Challenges & Learnings

One of the key challenges was keeping up with the rapid evolution of the LangChain library. Deprecation warnings for core components like `ConversationChain` and tool integrations required refactoring the code to use the modern LangChain Expression Language (LCEL) and `RunnableWithMessageHistory`. This was a valuable lesson in writing adaptable code and the importance of reading documentation to stay current with best practices in a fast-moving field.
