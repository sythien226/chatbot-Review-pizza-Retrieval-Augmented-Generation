from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2") #gọi mô hình llama3.2

#tạo template câu hỏi
template ="""
you are an expert in aswering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
#dùng ChatPromptTemplate để định dạng câu hỏi 
prompt= ChatPromptTemplate.from_template(template)
#tạo chuỗi xử lí truy vấn 
chain= prompt | model 

while True:
    print("\n\n------------------------------")
    question= input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    #tìm kiếm truy vấn đánh giá liên quan đến question
    reviews=retriever.invoke(question)
    #điền dl vào prompt template và in ra result
    result= chain.invoke({"reviews": reviews, "question": question})
    print(result)