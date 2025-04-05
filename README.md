# LocalAIAgentWithRAG
🧠 Hệ Thống Hỏi Đáp Review Nhà Hàng Pizza (LangChain + Ollama)
📌 Mô tả Dự Án
Dự án này xây dựng một hệ thống hỏi đáp thông minh sử dụng mô hình ngôn ngữ LLaMA3.2 và mxbai-embed-large thông qua thư viện LangChain, kết hợp với Chroma DB để truy xuất các đánh giá phù hợp nhất từ một tập dữ liệu review nhà hàng pizza.

Người dùng có thể đặt câu hỏi liên quan đến nhà hàng, hệ thống sẽ tìm các review có liên quan nhất, sau đó dùng mô hình LLM để đưa ra câu trả lời thông minh và chính xác.

🧱 Cấu Trúc Dự Án

.
├── main1.py               # Tập chính chạy hệ thống hỏi đáp
├── vector1.py             # Xử lý dữ liệu review và tạo vector truy vấn
├── realistic_restaurant_reviews.csv  # File dữ liệu đánh giá nhà hàng
├── chrome_langchain_db/   # Thư mục chứa cơ sở dữ liệu vector 
└── README.md              
🔧 Công Nghệ Sử Dụng
LangChain

Ollama LLM

Chroma Vector DB

Mô hình:

llama3.2 (trả lời câu hỏi)

mxbai-embed-large (chuyển văn bản thành vector)

Python

Pandas

🚀 Hướng Dẫn Chạy Dự Án
1. Cài Đặt Thư Viện

pip install langchain langchain-core langchain-ollama langchain-chroma pandas
2. Đảm bảo rằng bạn đã cài và chạy mô hình Ollama
Bạn cần chạy các mô hình sau qua Ollama:


ollama run llama3.2
ollama run mxbai-embed-large
3. Chuẩn Bị Dữ Liệu
Đảm bảo có file realistic_restaurant_reviews.csv nằm cùng thư mục với code.

4. Khởi Tạo Vector DB
Chạy file vector1.py để tạo vector từ dữ liệu review:


python vector1.py
Lưu ý: Việc này chỉ cần làm một lần.

5. Chạy Ứng Dụng Hỏi Đáp

python main1.py
Hệ thống sẽ hiển thị dòng lệnh để bạn nhập câu hỏi. Gõ q để thoátát

✅ Output Mẫu

Ask your question (q to quit): Which is the best pizza place in this town?

I'd be happy to help you out!

Based on our excellent customer reviews, I would highly recommend "Bella Vita" as the top-rated pizza place in town. They've received rave reviews for their authentic Neapolitan-style pizzas, made with fresh, high-quality ingredients and cooked to perfection in a wooI'd be happy to help you out!

Based on our excellent customer reviews, I would highly recommend "Bella Vita" as the top-rated pizza place in town. They've received rave reviews for their authentic Neapolitan-style pizzas, made with fresh, high-quality ingredients and cooked to perfection in a wood-fired oven.

Based on our excellent customer reviews, I would highly recommend "Bella Vita" as the top-rated pizza place in town. They've received rave reviews for their authentic Neapolitan-style pizzas, made with fresh, high-quality ingredients and cooked to perfection in a wood-fired oven.

Some reviewers have praised their creative topping combinations, such as the "Tuscan Sunsd-fired oven.

Some reviewers have praised their creative topping combinations, such as the "Tuscan SunsSome reviewers have praised their creative topping combinations, such as the "Tuscan Sunset" (prosciutto, arugula, and burrata) and the "Meat Lover's Masterpiece" (pepperoni, sausage, bacon, and ham). Others have raved about their crusts, calling them crispy on the osage, bacon, and ham). Others have raved about their crusts, calling them crispy on the outside and chewy on the inside.

Of course, every pizza place has its own unique charm

Of course, every pizza place has its own unique charm, but based on our reviews, I think Bella Vita is the way to go if you're looking for an authentic, delicious pizza experience in town. Would you like more information or recommendations?