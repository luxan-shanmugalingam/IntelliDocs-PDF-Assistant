from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import streamlit as st

# --- App UI ----
st.title("Chat with Your PDF")

# --- Logic for the RAG Chain ---
# We'll put this in a function to load it only once
@st.cache_resource
def load_rag_chain():
    vector_store = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever()
    model = ChatOpenAI(model="gpt-4o-mini")
    # This prompt is designed for RAG. It instructs the AI to answer based on context.
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context.
    If you don't know the answe, just say that you don't know.
                                              
    <context>{context}</context>
    Question: {input}                                          
    """)
    # This will take a question and the retrieved documents and generate an answer.
    document_chain = create_stuff_documents_chain(model, prompt)
    return create_retrieval_chain(retriever, document_chain)

retrieval_chain = load_rag_chain()

# --- Session State for Chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Handle User Input ---
if prompt := st.chat_input("Ask a question about your document"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response 
    response = retrieval_chain.invoke({"input": prompt})
    answer = response["answer"]


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(answer)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})