# 🧩 8-Puzzle Game – Đồ án Python

Đây là đồ án Python mô phỏng trò chơi **8-Puzzle** – một bài toán cổ điển trong trí tuệ nhân tạo, nơi người chơi phải di chuyển các ô số để đạt được trạng thái mục tiêu.

---

## 🎮 Giao diện trò chơi

Hình ảnh giao diện game được xây dựng bằng thư viện Tkinter:

![image](https://github.com/user-attachments/assets/9470a0fc-1505-4889-9638-9fa4d0ff1200)

---

## 🧠 Các thuật toán được tích hợp

Hệ thống hỗ trợ **20 thuật toán AI** để giải bài toán 8-puzzle một cách tự động. Dưới đây là danh sách thuật toán và hình ảnh động minh họa từng thuật toán:

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1   | Breadth-First Search (BFS)             | ![BFS](https://github.com/user-attachments/assets/ff6ca2ac-9ad2-4fbe-92e7-972df04121e5) |
| 2   | Depth-First Search (DFS)               | ![DFS](https://github.com/user-attachments/assets/6896d1ae-613c-4a25-9b21-e002f36d4ab0) |
| 3   | Uniform Cost Search (UCS)              | ![UCS](https://github.com/user-attachments/assets/1d6c868e-db11-44b7-a8f2-a9b67c64a3ef) |
| 4   | Iterative Deepening                    | ![ID](https://github.com/user-attachments/assets/27f72802-3597-405b-8c6e-a66f92dcb3f4)|
| 5   | Greedy Best-First Search               | ![GREEDY](https://github.com/user-attachments/assets/9fe3f61d-0e53-40eb-9aa7-97d17f72888b)|
| 6   | A* Search                              | ![A SAO](https://github.com/user-attachments/assets/7e6e91da-24d8-47c0-8835-136cddf8046d)|
| 7   | Iterative Deepening A* (IDA*)          | ![IDASAO](https://github.com/user-attachments/assets/0587b55d-d72c-4e84-a317-12fd8d68edd4)|
| 8   | Steepest Hill Climbing (SHC)           | ![SHC](https://github.com/user-attachments/assets/f7f10a19-89ac-459a-982c-31e8a000f7c1)|
| 9   | Simulated Annealing                    | ![SA](https://github.com/user-attachments/assets/2ef1e6ed-62ae-455f-91aa-d43aab542c1e)|
| 10  | Beam Search                            | ![BEAM](https://github.com/user-attachments/assets/1da22eab-b015-4a86-9ab1-51db1a911ff4)|
| 11  | Genetic Algorithm                      | ![GENETIC](https://github.com/user-attachments/assets/69ebcc7d-b465-4774-a6c3-835922a2b363)|
| 12  | Stochastic Hill Climbing               | ![STOCHASTIC](https://github.com/user-attachments/assets/5a523082-ee5a-46a0-ba32-09c4c6b80125)|
| 13  | AND-OR BFS                             | ![AND OR](https://github.com/user-attachments/assets/b40d2300-e05c-4683-896e-1af0668c0017)|
| 14  | Belief-based Search                    | ![BELIEF](https://github.com/user-attachments/assets/77fe9529-f19b-4e43-af15-a4aec78db211)|
| 15  | Sarsa                                  | ![SARSA](https://github.com/user-attachments/assets/05012cc7-5c03-4cc2-bceb-f290eee58fc5)|
| 16  | Backtracking                           | ![BACKTRACKING](https://github.com/user-attachments/assets/55d52c48-40b6-44db-b8bd-e4691661f9b4)|
| 17  | Backtracking + Forward Checking        | ![BACKTRACKING WITH](https://github.com/user-attachments/assets/37af4a98-26e1-4fab-97d5-d44ba0986782)|
| 18  | Q learning                             | ![Q LEARNING ](https://github.com/user-attachments/assets/0e15308f-4cc4-4bfd-a4d7-f0abd9a002c3)|
| 19  | Min-Conflicts                          | ![MIN CONFLICTS](https://github.com/user-attachments/assets/a839d9d5-832f-437a-b370-82a9c0bdc5cc)|
| 20  | Steppest Ascent hill climbing          |![SAHC](https://github.com/user-attachments/assets/bf983941-d933-439c-aa4d-03347543beb3)|


---

## 🕹️ Hướng dẫn cách chơi

_Vui lòng ghi hướng dẫn chi tiết tại đây, ví dụ:_

- Nhấn nút **"Random"** để tạo trạng thái khởi đầu ngẫu nhiên.
- Chọn **thuật toán AI** từ danh sách để chạy thuật toán để giải câu đó.
- phis dưới sẽ hiển thị thười gian chạy và cần bao nhiêu bước để giải.
---

## 💻 Công nghệ sử dụng

- Ngôn  ngữ Python
- Tkinter – GUI Framework
- GIF animation



