from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    while True:
        query_text = input("\nAsk Me> ")
        if query_text == "quit": break
        response_text, sources = query_rag(query_text)
        print(f"Response: {response_text}\n\nSources: {sources}")
    

def query_rag(query_text):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory = CHROMA_PATH, embedding_function = embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    
    return response_text, sources


if __name__ == "__main__":
    main()