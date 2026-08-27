from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(
    chunk_size=512,
    chunk_overlap=50
)

def chunk_text(text: str):
    
    document = Document(text=text)

    nodes = splitter.get_nodes_from_documents([document])

    return nodes

