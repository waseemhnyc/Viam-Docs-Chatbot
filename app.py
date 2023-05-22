from query_data import get_chain
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

if __name__ == "__main__":
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="db", embedding_function=embeddings)
    qa_chain = get_chain(vectorstore)
    chat_history = []
    line = "*" * 95
    print(line)
    print("AI: Hi, I'm the Viam Docs Chatbot. Ask me a question about: https://docs.viam.com/")
    print(line)
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        result = qa_chain({"question": question, "chat_history": chat_history})
        chat_history.append((question, result["answer"]))
        print("AI:", result["answer"])
        print(line)
