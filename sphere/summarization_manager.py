from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter

from sphere.utils import llm_loader

text_splitter = CharacterTextSplitter()


def main(file_type, file):
    docs = ""
    if file_type == "pdf":
        docs = file.load_and_split()
    elif file_type == "txt":
        texts = text_splitter.split_text(file)
        docs = [Document(page_content=t) for t in texts[:3]]
    llm = llm_loader()

    prompt_template = """Utilisez les éléments de contexte suivants pour rédiger un résumé complet de ce cours. Si 
    vous ne connaissez pas la réponse, dites simplement que vous ne savez pas, n'essayez pas d'inventer une réponse. 
    La réponse doit être aussi aussi concise que possible. Dites toujours "merci d'avoir posé la question" à la fin 
    de la réponse. Tu dois toujours répondre à la question en français et dans le format markdown.
    
    Réfléchi étape par étape.
    {text}
    
    RÉSUMÉ:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(
        llm, chain_type="map_reduce", map_prompt=prompt, combine_prompt=prompt
    )

    return chain({"input_documents": docs}, return_only_outputs=True)["output_text"]
