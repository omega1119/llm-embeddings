import re
from IPython.display import display, Markdown
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from .config import LLM_MODEL, EMBEDDING_MODEL, FAISS_INDEX_DIR, RETRIEVER_TOP_K

llm = None
embeddings_model = None
vectorstore = None
retriever = None
memory = None
conversation_chain = None

def fix_latex_delimiters(text):
    text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', text, flags=re.DOTALL)
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text, flags=re.DOTALL)
    return text

def setup_chat():
    global llm, embeddings_model, vectorstore, retriever, memory, conversation_chain

    llm = ChatOpenAI(model=LLM_MODEL, temperature=0.0)
    embeddings_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = FAISS.load_local(
        FAISS_INDEX_DIR,
        embeddings_model,
        allow_dangerous_deserialization=True
    )

    # Explicitly use parameter from config.py
    retriever = vectorstore.as_retriever(search_kwargs={"k": RETRIEVER_TOP_K})

    chat_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        chat_memory=chat_history,
        memory_key="chat_history",
        return_messages=True,
        input_key="question",
        output_key="answer"
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

def chat(query, char_limit=200, use_retriever=True):
    if conversation_chain is None:
        raise RuntimeError("Chat system not initialized. Please run setup_chat() first.")

    if use_retriever:
        result = conversation_chain.invoke({"question": query})
        question = fix_latex_delimiters(result['question'])
        answer = fix_latex_delimiters(result['answer'])
        sources = result['source_documents']
    else:
        chat_history = memory.load_memory_variables({})["chat_history"]
        prompt = f"{chat_history}\nUser: {query}\nAssistant:"
        result_text = llm.invoke(prompt)
        question = query
        answer = fix_latex_delimiters(result_text.content)
        sources = []

    print("\nQuestion:")
    display(Markdown(question))

    print("\nAnswer:")
    display(Markdown(answer))

    print("\nSources:")
    for i, doc in enumerate(sources, 1):
        source_info = doc.metadata.get('source', 'Unknown')
        page_content = fix_latex_delimiters(doc.page_content)
        
        # Limit page content length
        if len(page_content) > char_limit:
            page_content = page_content[:char_limit] + "...\n\n*(truncated)*"

        source_md = f"#### Source {i}: {source_info}\n\n```\n{page_content}\n```"
        display(Markdown(source_md))

def clear_memory():
    if memory:
        memory.clear()
