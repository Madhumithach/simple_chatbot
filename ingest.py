import pdfplumber
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
data={}
with pdfplumber.open("a-practical-guide-to-building-agents.pdf") as pdf:
      for i,pages in enumerate(pdf.pages):
            text=pages.extract_text()
            if text:
                  data.append({"text":text,"page":i+1})

    
text_splitter=RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=50,seperators=["\n\n","\n"," ",""])    
chunks=text_splitter.split_text(pdf)

