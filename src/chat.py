
from typing import List
import time

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.conversational_retrieval.base import (
    ConversationalRetrievalChain,
)
from langchain.memory.buffer import ConversationBufferMemory
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage


class ChatManager:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.memory = None
        self.chain = None
        self.llm = None
        self._initialize_components()

    def _initialize_components(self):
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
        )

        try:
          self.llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=self.api_key,
    temperature=0.7,
    max_output_tokens=2048,
    top_p=0.95,
    top_k=40
)
        except Exception as e:
            print(f"Error initializing LLM: {e}")
            self.llm = None

    def _create_chain(self, retriever):
        system_template = """You are a helpful assistant that answers
questions based on the provided document context.

If the answer is not in the context, say so clearly.
Do not invent information or sources.

Context:
{context}
"""

        qa_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=system_template + "\nQuestion: {question}",
        )

        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": qa_prompt},
            verbose=False,
        )

        return self.chain

    def _fallback_generation(self, query: str, context_text: str):
        if not self.llm:
            return {
                "answer": "The language model could not be initialized. Check the API configuration.",
                "sources": [],
            }

        messages = [
            SystemMessage(
                content=(
                    "Answer using the provided document context. "
                    "If the answer is missing, say so.\n\n"
                    f"Context:\n{context_text}"
                )
            ),
            HumanMessage(content=query),
        ]

        for attempt in range(2):
            try:
                response = self.llm.invoke(messages)
                return {
                    "answer": response.content,
                    "sources": [],
                }
            except Exception as e:
                print(f"Fallback attempt {attempt + 1} failed: {e}")
                if attempt == 0:
                    time.sleep(3)

        return {
            "answer": (
                "The Gemini request failed. Check the terminal for the "
                "API error, model availability, and quota."
            ),
            "sources": [],
        }

    def generate_response(
        self,
        query: str,
        context_docs: List[Document],
    ):
        time.sleep(2)

        context_text = "\n".join(
            doc.page_content for doc in context_docs
        )

        if self.chain:
            try:
                result = self.chain.invoke({"question": query})

                answer = result.get("answer", "")
                sources = []

                for doc in result.get("source_documents", []):
                    sources.append({
                        "text": doc.page_content,
                        "metadata": doc.metadata,
                    })

                return {
                    "answer": answer,
                    "sources": sources,
                }

            except Exception as e:
                print(f"RAG chain failed: {e}")

        print("Trying direct generation fallback...")
        return self._fallback_generation(query, context_text)

    def set_retriever(self, retriever):
        self._create_chain(retriever)

    def reset_conversation(self):
        if self.memory:
            self.memory.clear()

    def get_conversation_history(self):
        if self.memory:
            return self.memory.chat_memory.messages
        return []
