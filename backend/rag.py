from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI

documents = ["This project is a real-time voice AI assistant using RAG."]

embeddings = OpenAIEmbeddings()
db = Chroma.from_texts(documents, embedding=embeddings)
llm = OpenAI()

def get_rag_response(query):
    docs = db.similarity_search(query)
    context = " ".join([d.page_content for d in docs])
    prompt = f"Context: {context}\nQuestion: {query}"
    return llm(prompt)
