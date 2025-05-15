# 🧩 8-Puzzle Game – Đồ án Python

Đây là đồ án Python mô phỏng trò chơi **8-Puzzle** – một bài toán cổ điển trong trí tuệ nhân tạo, nơi người chơi phải di chuyển các ô số để đạt được trạng thái mục tiêu.

---

## 2. 🎯 Mục tiêu của dự án

Mục tiêu chính của dự án là triển khai một nền tảng giải bài toán 8-puzzle một cách hiệu quả, cho phép người dùng có thể quan sát và thực hành giải bài toán này thông qua giao diện trực quan. Dự án tập trung áp dụng nhiều thuật toán trí tuệ nhân tạo đa dạng, từ những phương pháp tìm kiếm cơ bản cho đến các thuật toán nâng cao, nhằm khai thác và so sánh hiệu suất của từng thuật toán trong việc tìm ra lời giải tối ưu hoặc gần tối ưu. Ngoài ra, dự án còn hướng tới việc cung cấp một công cụ hữu ích cho mục đích giáo dục và nghiên cứu, giúp người học và nhà nghiên cứu hiểu rõ hơn về các kỹ thuật tìm kiếm trong không gian trạng thái, từ đó nâng cao kiến thức và kỹ năng về trí tuệ nhân tạo và giải thuật.

---
## 🎮 Giao diện trò chơi

Hình ảnh giao diện game được xây dựng bằng thư viện Tkinter:

![image](https://github.com/user-attachments/assets/9470a0fc-1505-4889-9638-9fa4d0ff1200)

---
## 🕹️ Hướng dẫn cách chơi

_Vui lòng ghi hướng dẫn chi tiết tại đây, ví dụ:_
- CÁCH TRUYỀN DỮ LIỆU:
- Nhấn nút **"Random"** để tạo trạng thái khởi đầu ngẫu nhiên và truyền thẳng trực tiếp dữ liệu vào trong bài.
- Sau khi nhập giữ liệu bạn hãy nhấn nút **"Import data"** để truyền dữ liệu từ ô nhập vào trong bài.
- CÁCH CHƠI:
- Chọn **thuật toán AI** từ danh sách để chạy thuật toán để giải câu đó.
- Phía dưới sẽ hiển thị thời gian chạy và cần bao nhiêu bước để giải.
---
## 🧠 Các thuật toán được tích hợp
Trong đồ án này, hệ thống được xây dựng với khả năng hỗ trợ tới 20 thuật toán trí tuệ nhân tạo để tự động giải bài toán 8-Puzzle. Mỗi thuật toán có đặc điểm và cách tiếp cận riêng biệt nhằm tìm ra chuỗi di chuyển tối ưu để đạt được trạng thái đích.

Đầu tiên là các thuật toán tìm kiếm cơ bản như Breadth-First Search (BFS) và Depth-First Search (DFS), với BFS khám phá trạng thái theo lớp từng bước từ trạng thái ban đầu còn DFS đi sâu theo nhánh trước khi quay lui. Uniform Cost Search (UCS) tiếp tục phát triển bằng cách ưu tiên các bước di chuyển có chi phí thấp nhất. Thuật toán Iterative Deepening kết hợp ưu điểm của BFS và DFS bằng cách giới hạn độ sâu từng vòng lặp để cân bằng giữa bộ nhớ và thời gian.

Trong nhóm thuật toán tìm kiếm theo heuristic, Greedy Best-First Search chọn trạng thái gần đích nhất dựa trên hàm đánh giá heuristic, còn A* Search là một cải tiến nổi bật khi kết hợp cả chi phí đã đi và ước lượng còn lại để đảm bảo tìm được lời giải tối ưu. Iterative Deepening A* (IDA*) là phiên bản giảm bộ nhớ của A* bằng cách lặp lại giới hạn chi phí dần tăng. Các phương pháp tối ưu cục bộ như Steepest Hill Climbing (SHC), Steppest Ascent Hill Climbing và Stochastic Hill Climbing liên tục cải thiện trạng thái hiện tại dựa trên giá trị heuristic nhưng có thể bị kẹt ở cực trị địa phương. Simulated Annealing được thiết kế để vượt qua các cực trị địa phương bằng cách cho phép chấp nhận tạm thời các trạng thái kém hơn với xác suất giảm dần. Beam Search giữ một số lượng giới hạn các trạng thái tốt nhất tại mỗi bước nhằm giảm chi phí tính toán.

Bên cạnh đó, các thuật toán metaheuristic như Genetic Algorithm mô phỏng cơ chế chọn lọc tự nhiên để tiến hóa các giải pháp tốt hơn qua các thế hệ. Thuật toán AND-OR BFS mở rộng tìm kiếm sang không gian hành động có điều kiện, còn Belief-based Search dựa trên thông tin niềm tin về trạng thái hệ thống. Thuật toán học tăng cường Sarsa và Q-learning cho phép máy học cách tối ưu hành động dựa trên trải nghiệm tương tác. Phương pháp Backtracking và Backtracking kết hợp Forward Checking là các kỹ thuật tìm kiếm trở lui có kiểm soát nhằm tránh các trạng thái không khả thi. Cuối cùng, Min-Conflicts là thuật toán hiệu quả cho bài toán thỏa mãn ràng buộc, giảm xung đột trong giải pháp.

Dưới đây là bảng tổng hợp kèm theo các ảnh GIF mô phỏng trực quan minh họa quá trình giải của từng thuật toán:
Hệ thống hỗ trợ **20 thuật toán AI** để giải bài toán 8-puzzle một cách tự động. Dưới đây là danh sách thuật toán và hình ảnh động minh họa từng thuật toán:
---
## 1. Uninformed Search Algorithms
Nhóm các thuật toán tìm kiếm không thông tin, không dùng hàm heuristic mà chỉ dựa vào cấu trúc không gian trạng thái:
- **Breadth-First Search (BFS)**: Tìm kiếm theo tầng, mở rộng các nút theo cấp độ từ gốc đến sâu dần, đảm bảo tìm được lời giải ngắn nhất về số bước đi nhưng có thể tiêu tốn bộ nhớ lớn khi không gian trạng thái rộng.
- **Depth-First Search (DFS)**: Tìm kiếm theo chiều sâu, đi sâu đến cùng một nhánh trước khi quay lui. Ưu điểm là sử dụng ít bộ nhớ nhưng không đảm bảo tìm lời giải ngắn nhất và có thể rơi vào vòng lặp vô tận nếu không kiểm soát.
- **Uniform Cost Search (UCS)**: Là biến thể của BFS nhưng mở rộng các nút dựa trên chi phí tích lũy thấp nhất, thích hợp khi các bước di chuyển có chi phí khác nhau.

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1   | Breadth-First Search (BFS)             | ![BFS](https://github.com/user-attachments/assets/ff6ca2ac-9ad2-4fbe-92e7-972df04121e5) |
| 2   | Depth-First Search (DFS)               | ![DFS](https://github.com/user-attachments/assets/6896d1ae-613c-4a25-9b21-e002f36d4ab0) |
| 3   | Uniform Cost Search (UCS)              | ![UCS](https://github.com/user-attachments/assets/1d6c868e-db11-44b7-a8f2-a9b67c64a3ef) |
| 4   | Iterative Deepening                    | ![ID](https://github.com/user-attachments/assets/27f72802-3597-405b-8c6e-a66f92dcb3f4)|

## 2. Informed Search Algorithms
Nhóm các thuật toán tìm kiếm có thông tin, sử dụng hàm heuristic để dẫn đường tìm kiếm hiệu quả hơn:

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1   | Greedy Best-First Search               | ![GREEDY](https://github.com/user-attachments/assets/9fe3f61d-0e53-40eb-9aa7-97d17f72888b)|
| 2   | A* Search                              | ![A SAO](https://github.com/user-attachments/assets/7e6e91da-24d8-47c0-8835-136cddf8046d)|
| 3   | Iterative Deepening A* (IDA*)          | ![IDASAO](https://github.com/user-attachments/assets/0587b55d-d72c-4e84-a317-12fd8d68edd4)|

## 3. Local Search and Metaheuristic Algorithms
Nhóm các thuật toán tìm kiếm cục bộ và metaheuristic, sử dụng các kỹ thuật tối ưu hóa để tìm giải pháp gần tối ưu:

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1   | Steepest Hill Climbing (SHC)           | ![SHC](https://github.com/user-attachments/assets/f7f10a19-89ac-459a-982c-31e8a000f7c1)|
| 2   | Simulated Annealing                    | ![SA](https://github.com/user-attachments/assets/2ef1e6ed-62ae-455f-91aa-d43aab542c1e)|
| 3  | Beam Search                            | ![BEAM](https://github.com/user-attachments/assets/1da22eab-b015-4a86-9ab1-51db1a911ff4)|
| 4  | Genetic Algorithm                      | ![GENETIC](https://github.com/user-attachments/assets/69ebcc7d-b465-4774-a6c3-835922a2b363)|
| 5  | Stochastic Hill Climbing               | ![STOCHASTIC](https://github.com/user-attachments/assets/5a523082-ee5a-46a0-ba32-09c4c6b80125)|
| 6  | Steppest Ascent hill climbing          |![SAHC](https://github.com/user-attachments/assets/bf983941-d933-439c-aa4d-03347543beb3)|

## 4. Specialized and Advanced Search Algorithms
Nhóm các thuật toán mở rộng, kết hợp hoặc các thuật toán đặc biệt để giải quyết các bài toán phức tạp hơn:

| 1  | AND-OR BFS                             | ![AND OR](https://github.com/user-attachments/assets/b40d2300-e05c-4683-896e-1af0668c0017)|
| 2  | Belief-based Search                    | ![BELIEF](https://github.com/user-attachments/assets/77fe9529-f19b-4e43-af15-a4aec78db211)|

## 5. Reinforcement Learning and Machine Learning Based Algorithms
Nhóm các thuật toán dựa trên học tăng cường hoặc học máy để tìm giải pháp thông qua việc học:

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1  | Sarsa                                  | ![SARSA](https://github.com/user-attachments/assets/05012cc7-5c03-4cc2-bceb-f290eee58fc5)|
| 2  | Q learning                             | ![Q LEARNING ](https://github.com/user-attachments/assets/0e15308f-4cc4-4bfd-a4d7-f0abd9a002c3)|

## 6. Constraint Satisfaction Problem (CSP) Algorithms
Nhóm các thuật toán tập trung vào kỹ thuật backtracking và forward checking để tối ưu hóa tìm kiếm trong các bài toán thỏa mãn ràng buộc:

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1  | Backtracking                           | ![BACKTRACKING](https://github.com/user-attachments/assets/55d52c48-40b6-44db-b8bd-e4691661f9b4)|
| 2  | Backtracking + Forward Checking        | ![BACKTRACKING WITH](https://github.com/user-attachments/assets/37af4a98-26e1-4fab-97d5-d44ba0986782)|
| 3  | Min-Conflicts                          | ![MIN CONFLICTS](https://github.com/user-attachments/assets/a839d9d5-832f-437a-b370-82a9c0bdc5cc)|

---


## 💻 Công nghệ sử dụng

- Ngôn  ngữ Python
- Tkinter – GUI Framework
- GIF animation
