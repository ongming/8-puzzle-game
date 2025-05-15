# 🧩 8-Puzzle Game – Đồ án trí tuệ nhân tạo

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
 ### CÁCH TRUYỀN DỮ LIỆU:
- Nhấn nút **"Random"** để tạo trạng thái khởi đầu ngẫu nhiên và truyền thẳng trực tiếp dữ liệu vào trong bài.
- Sau khi nhập giữ liệu bạn hãy nhấn nút **"Import data"** để truyền dữ liệu từ ô nhập vào trong bài.
 ### CÁCH CHƠI:
- Chọn **thuật toán AI** từ danh sách để chạy thuật toán để giải câu đó.
- Phía dưới sẽ hiển thị thời gian chạy và cần bao nhiêu bước để giải.
---
## 🧠 Các thuật toán được tích hợp
Trong đồ án này, hệ thống được xây dựng với khả năng hỗ trợ tới 20 thuật toán trí tuệ nhân tạo để tự động giải bài toán 8-Puzzle. Mỗi thuật toán có đặc điểm và cách tiếp cận riêng biệt nhằm tìm ra chuỗi di chuyển tối ưu để đạt được trạng thái đích.

Đầu tiên là các thuật toán tìm kiếm cơ bản như Breadth-First Search (BFS) và Depth-First Search (DFS), với BFS khám phá trạng thái theo lớp từng bước từ trạng thái ban đầu còn DFS đi sâu theo nhánh trước khi quay lui. Uniform Cost Search (UCS) tiếp tục phát triển bằng cách ưu tiên các bước di chuyển có chi phí thấp nhất. Thuật toán Iterative Deepening kết hợp ưu điểm của BFS và DFS bằng cách giới hạn độ sâu từng vòng lặp để cân bằng giữa bộ nhớ và thời gian.

Trong nhóm thuật toán tìm kiếm theo heuristic, Greedy Best-First Search chọn trạng thái gần đích nhất dựa trên hàm đánh giá heuristic, còn A* Search là một cải tiến nổi bật khi kết hợp cả chi phí đã đi và ước lượng còn lại để đảm bảo tìm được lời giải tối ưu. Iterative Deepening A* (IDA*) là phiên bản giảm bộ nhớ của A* bằng cách lặp lại giới hạn chi phí dần tăng. Các phương pháp tối ưu cục bộ như Steepest Hill Climbing (SHC), Steppest Ascent Hill Climbing và Stochastic Hill Climbing liên tục cải thiện trạng thái hiện tại dựa trên giá trị heuristic nhưng có thể bị kẹt ở cực trị địa phương. Simulated Annealing được thiết kế để vượt qua các cực trị địa phương bằng cách cho phép chấp nhận tạm thời các trạng thái kém hơn với xác suất giảm dần. Beam Search giữ một số lượng giới hạn các trạng thái tốt nhất tại mỗi bước nhằm giảm chi phí tính toán.

Bên cạnh đó, các thuật toán metaheuristic như Genetic Algorithm mô phỏng cơ chế chọn lọc tự nhiên để tiến hóa các giải pháp tốt hơn qua các thế hệ. Thuật toán AND-OR BFS mở rộng tìm kiếm sang không gian hành động có điều kiện, còn Belief-based Search dựa trên thông tin niềm tin về trạng thái hệ thống. Thuật toán học tăng cường Sarsa và Q-learning cho phép máy học cách tối ưu hành động dựa trên trải nghiệm tương tác. Phương pháp Backtracking và Backtracking kết hợp Forward Checking là các kỹ thuật tìm kiếm trở lui có kiểm soát nhằm tránh các trạng thái không khả thi. Cuối cùng, Min-Conflicts là thuật toán hiệu quả cho bài toán thỏa mãn ràng buộc, giảm xung đột trong giải pháp.

---
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

## Đánh giá:
- Các thuật toán như BFS, DFS, UCS, và Iterative Deepening không sử dụng thông tin về trạng thái đích (heuristic), do đó thường khám phá toàn bộ không gian trạng thái một cách mù quáng. Chúng có thể tìm được lời giải đúng (đặc biệt là BFS và UCS), nhưng thường mất nhiều thời gian và tài nguyên tính toán, đặc biệt với không gian trạng thái lớn như 8-Puzzle.

- Ưu điểm: Dễ cài đặt, đảm bảo tìm ra lời giải nếu tồn tại (BFS, UCS), có thể dùng để đánh giá độ sâu của lời giải.

- Nhược điểm: Không tối ưu về thời gian, tiêu tốn bộ nhớ lớn, DFS dễ rơi vào vòng lặp.

---
## 2. Informed Search Algorithms
Nhóm các thuật toán tìm kiếm có thông tin, sử dụng hàm heuristic để dẫn đường tìm kiếm hiệu quả hơn:
- **Greedy Best-First Search**: Luôn chọn mở rộng nút có giá trị heuristic nhỏ nhất, tìm kiếm nhanh nhưng không đảm bảo lời giải tối ưu.
- **A* Search**: Kết hợp chi phí đã đi và ước lượng còn lại, luôn đảm bảo tìm lời giải tối ưu nếu hàm heuristic là hợp lệ (không vượt quá chi phí thực).
- **Iterative Deepening A* (IDA*)**: Kết hợp phương pháp iterative deepening và A*, giảm tiêu thụ bộ nhớ so với A* truyền thống nhưng vẫn đảm bảo lời giải tối ưu.

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1   | Greedy Best-First Search               | ![GREEDY](https://github.com/user-attachments/assets/9fe3f61d-0e53-40eb-9aa7-97d17f72888b)|
| 2   | A* Search                              | ![A SAO](https://github.com/user-attachments/assets/7e6e91da-24d8-47c0-8835-136cddf8046d)|
| 3   | Iterative Deepening A* (IDA*)          | ![IDASAO](https://github.com/user-attachments/assets/0587b55d-d72c-4e84-a317-12fd8d68edd4)|

## Đánh giá:
- Các thuật toán như Greedy Best-First Search, A* và IDA* sử dụng hàm heuristic để hướng dẫn quá trình tìm kiếm. Trong đó, A* là một trong những thuật toán mạnh mẽ và phổ biến nhất cho 8-Puzzle vì tính chính xác và hiệu quả của nó.

- Ưu điểm: Giảm thời gian tìm kiếm đáng kể, thường đưa ra lời giải ngắn và tối ưu (đặc biệt A*).

- Nhược điểm: Phụ thuộc vào chất lượng heuristic; Greedy có thể nhanh nhưng không tối ưu; A* tiêu tốn nhiều bộ nhớ.
## 3. Local Search and Metaheuristic Algorithms
Nhóm các thuật toán tìm kiếm cục bộ và metaheuristic, sử dụng các kỹ thuật tối ưu hóa để tìm giải pháp gần tối ưu:
- **Steepest Hill Climbing (SHC) & Steppest Ascent Hill Climbing (SAHC)**: Luôn chọn bước đi làm cải thiện lớn nhất trên đường đi lên “đồi”, nhanh nhưng dễ bị mắc kẹt tại điểm tối ưu cục bộ.
- **Stochastic Hill Climbing**: Giới thiệu tính ngẫu nhiên trong chọn bước đi để tránh bị kẹt tại điểm cục bộ.
- **Simulated Annealing**: Giả lập quá trình làm nguội vật lý, cho phép chấp nhận các bước đi tạm thời xấu để thoát khỏi điểm tối ưu cục bộ.
- **Genetic Algorithm**: Thuật toán tiến hóa mô phỏng quá trình chọn lọc tự nhiên, sử dụng các thao tác lai ghép và đột biến để tạo ra các thế hệ lời giải tốt hơn.
- **Beam Search**: Giới hạn số lượng nút mở rộng tại mỗi bước để tiết kiệm bộ nhớ, chọn ra một số lời giải hứa hẹn nhất để tiếp tục mở rộng.

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1   | Steepest Hill Climbing (SHC)           | ![SHC](https://github.com/user-attachments/assets/f7f10a19-89ac-459a-982c-31e8a000f7c1)|
| 2   | Simulated Annealing                    | ![SA](https://github.com/user-attachments/assets/2ef1e6ed-62ae-455f-91aa-d43aab542c1e)|
| 3  | Beam Search                            | ![BEAM](https://github.com/user-attachments/assets/1da22eab-b015-4a86-9ab1-51db1a911ff4)|
| 4  | Genetic Algorithm                      | ![GENETIC](https://github.com/user-attachments/assets/69ebcc7d-b465-4774-a6c3-835922a2b363)|
| 5  | Stochastic Hill Climbing               | ![STOCHASTIC](https://github.com/user-attachments/assets/5a523082-ee5a-46a0-ba32-09c4c6b80125)|
| 6  | Steppest Ascent hill climbing          |![SAHC](https://github.com/user-attachments/assets/bf983941-d933-439c-aa4d-03347543beb3)|
    
## Đánh giá:
- Bao gồm các thuật toán như Steepest Hill Climbing, Stochastic Hill Climbing, Simulated Annealing, Beam Search và Genetic Algorithm. Những thuật toán này không đi theo đường tìm kiếm toàn cục mà thay vào đó tìm lời giải thông qua cải tiến cục bộ và ngẫu nhiên hóa.

- Ưu điểm: Khả năng xử lý không gian trạng thái lớn, tránh được bẫy cục bộ (đặc biệt là Simulated Annealing và Genetic Algorithm).

- Nhược điểm: Không đảm bảo tìm được lời giải tối ưu; dễ rơi vào bẫy tối ưu cục bộ; hiệu quả phụ thuộc nhiều vào tham số và cách khởi tạo.

## 4. Specialized and Advanced Search Algorithms
Nhóm các thuật toán mở rộng, kết hợp hoặc các thuật toán đặc biệt để giải quyết các bài toán phức tạp hơn:
- **AND-OR BFS**: Giải quyết các bài toán không chắc chắn hoặc có nhiều lựa chọn thay thế, tìm kiếm trong không gian trạng thái dạng cây AND-OR, hỗ trợ lý luận phức tạp hơn.
- **Belief-based Search**: Sử dụng thông tin niềm tin (belief) về trạng thái thực sự trong môi trường không chắc chắn để hướng dẫn tìm kiếm, áp dụng trong các tình huống có thông tin bị thiếu hoặc nhiễu.

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1  | AND-OR BFS                             | ![AND OR](https://github.com/user-attachments/assets/b40d2300-e05c-4683-896e-1af0668c0017)|
| 2  | Belief-based Search                    | ![BELIEF](https://github.com/user-attachments/assets/77fe9529-f19b-4e43-af15-a4aec78db211)|

## Đánh giá:
- Bao gồm AND-OR Search, Belief-based Search, Min-Conflicts, và Steepest Ascent Hill Climbing – là các phương pháp mở rộng hoặc đặc thù cho môi trường bất định hoặc bài toán logic phức tạp. Một số trong đó được xây dựng để xử lý bài toán có tính không chắc chắn hoặc nhiều mục tiêu song song.

- Ưu điểm: Đa dạng, linh hoạt, có thể mở rộng sang các bài toán lớn hơn.

- Nhược điểm: Ít phù hợp với 8-Puzzle thông thường; một số thuật toán khá phức tạp và khó triển khai hiệu quả.

## 5. Reinforcement Learning and Machine Learning Based Algorithms
Nhóm các thuật toán dựa trên học tăng cường hoặc học máy để tìm giải pháp thông qua việc học:
- **Sarsa**: Thuật toán học tăng cường on-policy, học chính sách bằng cách cập nhật giá trị hành động dựa trên trải nghiệm thực tế, phù hợp với bài toán có trạng thái và hành động rời rạc.
- **Q Learning**: Thuật toán học tăng cường off-policy, học giá trị tối ưu của các hành động mà không cần thực hiện chính sách hiện tại, giúp đạt hiệu suất tốt trong việc học các chính sách tối ưu.

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1  | Sarsa                                  | ![SARSA](https://github.com/user-attachments/assets/05012cc7-5c03-4cc2-bceb-f290eee58fc5)|
| 2  | Q learning                             | ![Q LEARNING ](https://github.com/user-attachments/assets/0e15308f-4cc4-4bfd-a4d7-f0abd9a002c3)|

## Đánh giá:
- Q-Learning và Sarsa đại diện cho nhóm học tăng cường, nơi thuật toán tự học thông qua tương tác với môi trường để dần tối ưu hóa chiến lược giải bài toán. Với 8-Puzzle, nhóm này có thể học được giải pháp tối ưu mà không cần mô hình hóa trạng thái rõ ràng.

- Ưu điểm: Có thể tổng quát hóa tốt, không cần mô hình hóa tường minh; thích hợp cho các bài toán học lâu dài.

- Nhược điểm: Cần nhiều thời gian để huấn luyện; yêu cầu điều chỉnh tham số tốt (learning rate, discount factor).

## 6. Constraint Satisfaction Problem (CSP) Algorithms
Nhóm các thuật toán tập trung vào kỹ thuật backtracking và forward checking để tối ưu hóa tìm kiếm trong các bài toán thỏa mãn ràng buộc:
- **Backtracking**: Kỹ thuật đệ quy tìm kiếm lời giải bằng cách thử từng lựa chọn và quay lui khi phát hiện mâu thuẫn, dễ hiểu nhưng có thể tốn thời gian nếu không được tối ưu.
- **Backtracking + Forward Checking**: Kết hợp forward checking để loại bỏ các lựa chọn không hợp lệ trước khi đi sâu vào các nhánh tìm kiếm, giúp giảm số lượng bước đi không cần thiết.
- **Min-Conflicts**: Thuật toán tìm kiếm cục bộ chuyên dùng cho các bài toán thỏa mãn ràng buộc, chọn các biến gây xung đột nhiều nhất và điều chỉnh để giảm thiểu xung đột.

| STT | Thuật toán                             | GIF mô phỏng                |
|-----|----------------------------------------|-----------------------------|
| 1  | Backtracking                           | ![BACKTRACKING](https://github.com/user-attachments/assets/55d52c48-40b6-44db-b8bd-e4691661f9b4)|
| 2  | Backtracking + Forward Checking        | ![BACKTRACKING WITH](https://github.com/user-attachments/assets/37af4a98-26e1-4fab-97d5-d44ba0986782)|
| 3  | Min-Conflicts                          | ![MIN CONFLICTS](https://github.com/user-attachments/assets/a839d9d5-832f-437a-b370-82a9c0bdc5cc)|

## Đánh giá:
- Backtracking và Backtracking kết hợp Forward Checking là các kỹ thuật cổ điển trong giải bài toán ràng buộc (Constraint Satisfaction Problems). Mặc dù ít dùng cho 8-Puzzle, nhóm này cung cấp cái nhìn khác về cách giải quyết vấn đề theo hướng phân nhánh và kiểm tra điều kiện hợp lệ.

- Ưu điểm: Đảm bảo lời giải hợp lệ; đơn giản và dễ hiểu.

- Nhược điểm: Hiệu suất thấp với bài toán không có ràng buộc cụ thể như 8-Puzzle; Forward Checking có cải tiến nhưng vẫn không tối ưu bằng A*.

---
## Kết luận
Bài toán 8-Puzzle là một ví dụ điển hình về tìm kiếm trong không gian trạng thái, và việc áp dụng đa dạng các thuật toán giải quyết không chỉ giúp hiểu rõ về các phương pháp tìm kiếm mà còn mở rộng khả năng so sánh, đánh giá hiệu suất của từng kỹ thuật trong thực tế. Các thuật toán uninformed search như BFS, DFS tuy đơn giản nhưng có thể gặp hạn chế về mặt hiệu quả khi không biết trước trạng thái đích. Trong khi đó, các thuật toán informed search như A* và IDA* tận dụng tốt thông tin heuristic, giúp rút ngắn thời gian tìm lời giải tối ưu.

Nhóm thuật toán local search và metaheuristic cung cấp những phương pháp linh hoạt, khả năng xử lý các trường hợp phức tạp và không gian trạng thái lớn, tuy không luôn đảm bảo tối ưu tuyệt đối nhưng thích hợp cho bài toán thực tế cần giải nhanh. Các thuật toán học tăng cường và machine learning như Sarsa, Q-Learning mở ra hướng tiếp cận mới, tận dụng kinh nghiệm để tự điều chỉnh chiến lược giải quyết, rất hứa hẹn cho các bài toán phức tạp hơn.

Cuối cùng, nhóm thuật toán xử lý ràng buộc CSP với Backtracking và các kỹ thuật tối ưu đi kèm giúp giải quyết bài toán một cách chính xác, hiệu quả trong các tình huống cần thỏa mãn nhiều điều kiện. Sự đa dạng này cho thấy rằng không có thuật toán “tuyệt đối nhất” mà mỗi thuật toán đều có ưu, nhược điểm và phù hợp với từng loại bài toán, yêu cầu cụ thể.

Việc nghiên cứu, triển khai và so sánh các thuật toán này không chỉ nâng cao kiến thức lý thuyết mà còn cung cấp công cụ thực tế để phát triển các ứng dụng trí tuệ nhân tạo có khả năng giải quyết các vấn đề phức tạp trong đời sống và kỹ thuật.

---

## 💻 Công nghệ sử dụng

- Ngôn  ngữ Python
- Tkinter – GUI Framework
- GIF animation

---

📚 Tài liệu sách
- Stuart Russell, Peter Norvig (2020). Artificial Intelligence: A Modern Approach (4th Edition). Pearson.
→ Giáo trình kinh điển, trình bày chi tiết về các thuật toán tìm kiếm như BFS, DFS, A*, Hill Climbing, Simulated Annealing, Q-learning,...

- Richard E. Neapolitan & Xia Jiang (2018). Artificial Intelligence: With an Introduction to Machine Learning. CRC Press.
→ Cung cấp lý thuyết nền về các thuật toán và phương pháp học máy liên quan đến Reinforcement Learning và tìm kiếm trạng thái.
