from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama


# Import necessary stuff


def embedding_model():
    """
    This code defines a function named embedding_model that initializes and returns a HuggingFaceEmbeddings model for
    text embeddings.
    :return: HuggingFaceEmbeddings model
    """

    # embeddings model
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": False}
    # return HuggingFaces embeddings model
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
    )


def llm_loader():
    return Ollama(
        model="llama2",
        verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
