# PDF RAG Chatbot | AI-Powered PDF Analyzer

An AI-powered PDF Analyzer built using **Retrieval-Augmented Generation (RAG)** that allows users to upload multiple PDF documents and ask questions based on their content. The application uses LangChain, Google Gemini, FAISS, Sentence Transformers, and Streamlit to provide context-aware answers through conversational AI.

## 👨‍💻 Developer

**Rishabh Sharma**

- B.Tech – Computer Science & Artificial Intelligence
- GL Bajaj Institute of Technology & Management

## 🚀 Demo

[Watch Project Demo](https://github.com/user-attachments/assets/a4607370-360f-432a-8dec-4b19ca6e4d99)

## ✨ Features

- **Multiple PDF Upload:** Upload and process multiple PDF documents.
- **PDF Text Extraction:** Extract textual content from PDFs using PyPDF2.
- **Text Chunking:** Split extracted text into smaller chunks using LangChain's RecursiveCharacterTextSplitter.
- **Semantic Embeddings:** Generate vector embeddings using Sentence Transformers.
- **Vector Database:** Store and index document embeddings using FAISS.
- **Semantic Search:** Retrieve the most relevant document chunks based on user queries.
- **LLM Integration:** Generate contextual answers using Google's Gemini model.
- **Conversational Memory:** Maintain conversation context across multiple questions using LangChain ConversationBufferMemory.
- **Interactive Interface:** Streamlit-based interface for document uploads and conversations.
- **Environment Configuration:** Secure API key management using environment variables.
- **Error Handling:** Handle document processing and API-related errors.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Framework | LangChain |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| PDF Processing | PyPDF2 |
| Environment Management | Python-dotenv |
| Version Control | Git & GitHub |

## 🧠 How It Works

The project follows a Retrieval-Augmented Generation (RAG) architecture.

### 1. Document Processing
- Users upload one or more PDF documents.
- PyPDF2 extracts text from the uploaded documents.
- Extracted text is divided into smaller chunks using RecursiveCharacterTextSplitter.

### 2. Embedding Generation
- Sentence Transformers converts text chunks into numerical vector embeddings.
- These embeddings represent the semantic meaning of the text.

### 3. Vector Storage
- Generated embeddings are stored in a FAISS vector database.
- FAISS enables efficient similarity-based document retrieval.

### 4. Query Processing
- The user asks a question through the Streamlit interface.
- The query is converted into an embedding.
- FAISS retrieves the most relevant document chunks.

### 5. Response Generation
- Retrieved context and the user's question are passed to Google Gemini through LangChain.
- Gemini generates a context-aware response based on the retrieved PDF content.
- The response is displayed in the Streamlit interface.

## 📂 Project Structure

```text
PDF-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
│
├── src/
│   ├── processor.py
│   ├── embedding.py
│   ├── chat.py
│   └── config.py
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PDF-Analyzer.git
cd PDF-Analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 Usage

1. Launch the application.
2. Upload one or multiple PDF documents.
3. Click on Process Documents.
4. Wait for document extraction and embedding generation.
5. Enter your questions in the chat interface.
6. Receive answers based on the uploaded PDF documents.
7. Continue the conversation with contextual memory.

## 🔮 Future Improvements

- Add support for additional document formats.
- Implement source citations for retrieved information.
- Improve retrieval accuracy using advanced retrieval techniques.
- Add persistent vector database storage.
- Deploy the application on Streamlit Cloud.

## 📌 Key Learning Outcomes

Through this project, I gained practical experience in:

- Understanding Retrieval-Augmented Generation (RAG).
- Working with Large Language Models (LLMs).
- Implementing semantic search using vector embeddings.
- Building vector databases using FAISS.
- Integrating Gemini with LangChain.
- Developing interactive AI applications using Streamlit.
- Managing API keys and environment variables.

---

**Developed by Rishabh Sharma**

[GitHub](https://github.com/Rishabhsharma111)