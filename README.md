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
| 4   | Iterative Deepening                    | ![ID](gifs/iterative.gif)   |
| 5   | Greedy Best-First Search               | ![Greedy](gifs/greedy.gif)  |
| 6   | A* Search                               | ![A*](gifs/astar.gif)       |
| 7   | Iterative Deepening A* (IDA*)          | ![IDA*](gifs/ida.gif)       |
| 8   | Steepest Hill Climbing (SHC)           | ![SHC](gifs/shc.gif)        |
| 9   | Simulated Annealing                    | ![SA](gifs/annealing.gif)   |
| 10  | Beam Search                            | ![Beam](gifs/beam.gif)      |
| 11  | Genetic Algorithm                      | ![Genetic](gifs/genetic.gif)|
| 12  | Stochastic Hill Climbing               | ![Stochastic](gifs/stochastic.gif) |
| 13  | AND-OR BFS                             | ![ANDOR](gifs/andor.gif)    |
| 14  | Belief-based Search                    | ![Belief](gifs/belief.gif)  |
| 15  | Import Data (trạng thái từ file)       | ![Import](gifs/import.gif)  |
| 16  | Random Walk                            | ![Random](gifs/random.gif)  |
| 17  | Backtracking                           | ![BT](gifs/backtracking.gif)|
| 18  | Backtracking + Forward Checking        | ![BT+FC](gifs/fc.gif)       |
| 19  | Min-Conflicts                          | ![MinC](gifs/minconflict.gif)|
| 20  | ??? *(Tuỳ bạn bổ sung thêm nếu còn slot)* | ![20](gifs/placeholder.gif) |


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



