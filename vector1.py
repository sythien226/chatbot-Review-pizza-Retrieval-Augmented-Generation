from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

#đọc file csv
df = pd.read_csv("realistic_restaurant_reviews.csv")
#tạo vector embeddings từ dữ liệu
embeddings= OllamaEmbeddings(model="mxbai-embed-large")
#lưu trữ vector
db_location = "./chrome_langchain_db"

add_documents = not os.path.exists(db_location)
#xử lí dữ liệu vào chroma DB
if add_documents:
    documents=[]
    ids=[]
    for i,row in df.iterrows():
        document=Document(
            page_content=row["title"] +" "+ row["review"],
            metadata={"rating":row["Rating"], "date":row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)
#thêm dữ liệu vào Chroma DB        
vector_store =Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)
#tạo bộ truy vấn retriever lọc lay 5 đánh giá liên quan nhất
if add_documents:
    vector_store.add_documents(documents=documents, ids =ids)
    retriever= vector_store.as_retriever(
        search_kwargs={"k":5}
    )
                               