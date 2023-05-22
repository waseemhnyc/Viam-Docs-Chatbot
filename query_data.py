from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
You can assume the question about LangChain.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = """You are an AI assistant for the open source library Viam Robotics. The documentation is located at https://python.viam.dev/.
You are given the following extracted parts of a long document and a question. Provide a conversational answer with a hyperlink to the documentation.
You should only use hyperlinks that are explicitly listed as a source in the context. Do NOT make up a hyperlink that is not listed.
If the question includes a request for code, provide a code block directly from the documentation.
If you don't know the answer, just say "Hmm, I'm not sure." Don't try to make up an answer.
If the question is not about Viam Robotics, politely inform them that you are tuned to only answer questions about Viam Robotics.

Question: {question}
=========
{context}
=========
Answer in Markdown:"""

# QA_PROMPT = PromptTemplate(
#     template=template, input_variables=["question", "context"]
# )


def get_chain(vectorstore):
    llm = ChatOpenAI(
        temperature=0, model_name="gpt-4"
    )
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        vectorstore.as_retriever(),
        chain_type="stuff",
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain
