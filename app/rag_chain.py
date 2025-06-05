from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from app.data_loader import create_vectorstore
import os
from dotenv import load_dotenv

load_dotenv()

def get_rag_chain():
    vectorstore = create_vectorstore()
    retriever = vectorstore.as_retriever()

    prompt_template = PromptTemplate.from_template(
        """
        Answer the question using the context below. If the answer is not in the context, say you don't know.

        Context:
        {context}

        Question:
        {question}
        """
    )

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-70b-8192"
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template}
    )

    return chain

# ✅ Add this line to expose it
qa_chain = get_rag_chain()
