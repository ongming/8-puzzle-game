import os
import sys
import time
from collections import deque
import heapq
import tkinter as tk
from tkinter import messagebox
import random
import torch
import math
from copy import deepcopy
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

def find_empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j  

def move_tile(board, empty_pos, direction):
    x, y = empty_pos
    dx, dy = direction
    new_x, new_y = x + dx, y + dy
    
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_board = [list(row) for row in board]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return new_board
    return None 

def heuristic(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                goal_pos = next((x, y) for x in range(3) for y in range(3) if goal[x][y] == val)
                distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return distance

def bfs_8_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(board_to_tuple(start))

    while queue:
        current_board, path = queue.popleft()
        
        if current_board == goal:
            return path
        empty_pos = find_empty(current_board)

        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                queue.append((new_board, path + [new_board]))
                visited.add(board_to_tuple(new_board))

    return None 

def dfs_8_puzzle(start, goal, max_depth=50):
    stack = [(start, [], 0)]
    visited = set()
    visited.add(board_to_tuple(start))

    while stack:
        current_board, path, depth = stack.pop()
        if current_board == goal:
            return path
        if depth >= max_depth:
            continue
        empty_pos = find_empty(current_board)
        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                visited.add(board_to_tuple(new_board))
                stack.append((new_board, path + [new_board], depth + 1))
    return None

def greedy_8_puzzle(start, goal):
    pq = [(heuristic(start, goal), start, [])]
    visited = set()
    visited.add(board_to_tuple(start))
    
    while pq:
        _, current_board, path = heapq.heappop(pq)
        if current_board == goal:
            return path
        empty_pos = find_empty(current_board)
        
        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                heapq.heappush(pq, (heuristic(new_board, goal), new_board, path + [new_board]))
                visited.add(board_to_tuple(new_board))

    return None 

def iterative_deepening_ucs_8_puzzle(start, goal, max_cost_limit=50):
    def dls(current_board, path, cost, cost_limit, visited):
        if current_board == goal:
            return path
        if cost > cost_limit:
            return None
        visited.add(board_to_tuple(current_board))
        empty_pos = find_empty(current_board)
        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board:
                board_key = board_to_tuple(new_board)
                if board_key not in visited:
                    result = dls(new_board, path + [new_board], cost + 1, cost_limit, visited)
                    if result:
                        return result
        return None

    for cost_limit in range(1, max_cost_limit + 1):
        visited = set()
        result = dls(start, [], 0, cost_limit, visited)
        if result:
            return result
    return None

def ucs_8_puzzle(start, goal):
    pq = [(0, start, [])]
    visited = set()
    visited.add(board_to_tuple(start))
    
    while pq:
        cost, current_board, path = heapq.heappop(pq)
        if current_board == goal:
            return path
        empty_pos = find_empty(current_board)
        
        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                heapq.heappush(pq, (cost + 1, new_board, path + [new_board]))
                visited.add(board_to_tuple(new_board))

    return None

def a_star_8_puzzle(start, goal):
    pq = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()
    visited.add(board_to_tuple(start))
    
    while pq:
        f, g, current_board, path = heapq.heappop(pq)
        if current_board == goal:
            return path
        empty_pos = find_empty(current_board)
        
        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                new_g = g + 1
                heapq.heappush(pq, (new_g + heuristic(new_board, goal), new_g, new_board, path + [new_board]))
                visited.add(board_to_tuple(new_board))

    return None 

def ida_star_8_puzzle(start, goal):
    def search(board, g, threshold, path, visited):
        f = g + heuristic(board, goal)
        if f > threshold:
            return f, None
        if board == goal:
            return f, path
        min_threshold = float('inf')
        empty_pos = find_empty(board)
        
        for direction in DIRECTIONS:
            new_board = move_tile(board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                visited.add(board_to_tuple(new_board))
                temp_threshold, result = search(new_board, g + 1, threshold, path + [new_board], visited)
                if result:
                    return temp_threshold, result
                if temp_threshold < min_threshold:
                    min_threshold = temp_threshold
                visited.remove(board_to_tuple(new_board))
        return min_threshold, None
    
    threshold = heuristic(start, goal)
    path = []
    while True:
        visited = {board_to_tuple(start)}
        temp_threshold, result = search(start, 0, threshold, path, visited)
        if result:
            return result
        if temp_threshold == float('inf'):
            return None
        threshold = temp_threshold

def hill_climbing(start, goal, max_steps=1000, max_sideways=20):
    current_board = start
    current_h = heuristic(current_board, goal)
    path = []
    sideways_moves = 0
    
    for _ in range(max_steps):
        if current_board == goal:
            return path
        
        empty_pos = find_empty(current_board)
        neighbors = [move_tile(current_board, empty_pos, d) for d in DIRECTIONS]
        neighbors = [n for n in neighbors if n is not None]
        
        if not neighbors:
            return None
        
        random.shuffle(neighbors)
        next_board = None
        for neighbor in neighbors:
            neighbor_h = heuristic(neighbor, goal)
            if neighbor_h < current_h:
                next_board = neighbor
                sideways_moves = 0
                break
            elif neighbor_h == current_h and sideways_moves < max_sideways:
                next_board = neighbor
                sideways_moves += 1
                break
        
        if next_board is None:
            return None
        
        current_board = next_board
        current_h = heuristic(current_board, goal)
        path.append(current_board)
    
    return None

def steepest_hill_climbing(start, goal, max_steps=1000, max_sideways=20):
    current_board = start
    current_h = heuristic(current_board, goal)
    path = []
    sideways_moves = 0
    
    for _ in range(max_steps):
        if current_board == goal:
            return path
        
        empty_pos = find_empty(current_board)
        neighbors = [move_tile(current_board, empty_pos, d) for d in DIRECTIONS]
        neighbors = [n for n in neighbors if n is not None]
        
        if not neighbors:
            return None
        
        neighbors.sort(key=lambda n: heuristic(n, goal))
        best_h = heuristic(neighbors[0], goal)
        
        if best_h < current_h:
            next_board = neighbors[0]
            sideways_moves = 0
        elif best_h == current_h and sideways_moves < max_sideways:
            best_neighbors = [n for n in neighbors if heuristic(n, goal) == best_h]
            next_board = random.choice(best_neighbors)
            sideways_moves += 1
        else:
            return None
        
        current_board = next_board
        current_h = heuristic(current_board, goal)
        path.append(current_board)
    
    return None

def simulated_annealing(start, goal, max_iterations=50000, initial_temp=5000.0, cooling_rate=0.999):
    current_board = [row[:] for row in start]
    current_h = heuristic(current_board, goal)
    path = []
    temperature = initial_temp
    best_board = deepcopy(current_board)
    best_h = current_h
    same_state_count = 0

    for iteration in range(max_iterations):
        if current_board == goal:
            return path

        if temperature < 0.01 or same_state_count > 300:
            break

        empty_pos = find_empty(current_board)
        neighbors = []

        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board:
                neighbors.append((new_board, heuristic(new_board, goal)))

        if not neighbors:
            break

        if random.random() < 0.7 or temperature < 100:
            next_board, next_h = min(neighbors, key=lambda x: x[1])
        else:
            next_board, next_h = random.choice(neighbors)

        delta_e = current_h - next_h

        moved = False
        if delta_e > 0:
            if board_to_tuple(next_board) != board_to_tuple(current_board):
                current_board = next_board
                current_h = next_h
                path.append(deepcopy(current_board))
                moved = True
        else:
            probability = math.exp(delta_e / temperature)
            if random.random() < probability:
                if board_to_tuple(next_board) != board_to_tuple(current_board):
                    current_board = next_board
                    current_h = next_h
                    path.append(deepcopy(current_board))
                    moved = True

        if moved:
            same_state_count = 0
            if current_h < best_h:
                best_board = deepcopy(current_board)
                best_h = current_h
        else:
            same_state_count += 1

        temperature *= cooling_rate

    if current_board != goal and best_h < current_h:
        if board_to_tuple(best_board) != board_to_tuple(path[-1]) if path else True:
            path.append(best_board)
    return path

def stochastic_hill_climbing(start, goal, max_steps=1000):
    current_board = start
    current_h = heuristic(current_board, goal)
    path = []

    for _ in range(max_steps):
        if current_board == goal:
            return path

        empty_pos = find_empty(current_board)
        neighbors = [move_tile(current_board, empty_pos, d) for d in DIRECTIONS]
        neighbors = [n for n in neighbors if n]

        better_neighbors = [n for n in neighbors if heuristic(n, goal) <= current_h]
        if not better_neighbors:
            return None

        current_board = random.choice(better_neighbors)
        current_h = heuristic(current_board, goal)
        path.append(current_board)

    return None

def beam_search_8_puzzle(start, goal, beam_width=100):
    if start == goal:
        return []

    beam = [(heuristic(start, goal), start, [])]
    visited = {board_to_tuple(start)}
    
    while beam:
        next_beam = []
        
        for h, current_board, path in beam:
            empty_pos = find_empty(current_board)
            
            for direction in DIRECTIONS:
                new_board = move_tile(current_board, empty_pos, direction)
                if not new_board:
                    continue
                    
                board_tuple = board_to_tuple(new_board)
                if board_tuple in visited:
                    continue
                
                visited.add(board_tuple)
                new_path = path + [new_board]
                new_h = heuristic(new_board, goal)
                
                if new_board == goal:
                    return new_path
                
                next_beam.append((new_h, new_board, new_path))

        next_beam.sort(key=lambda x: x[0])
        beam = next_beam[:beam_width]
    
    return None

def genetic_algorithm_8_puzzle(start, goal, population_size=50, generations=1000, mutation_rate=0.2):
    def fitness(board):
        return -heuristic(board, goal)

    def is_valid_transition(board1, board2):
        diff = [(i, j) for i in range(3) for j in range(3) if board1[i][j] != board2[i][j]]
        return len(diff) == 2

    population = []
    for _ in range(population_size):
        individual = {
            'board': deepcopy(start),
            'path': [],
            'moves': random.randint(5, 20)
        }
        current_board = deepcopy(start)
        for _ in range(individual['moves']):
            empty_pos = find_empty(current_board)
            possible_moves = [move_tile(current_board, empty_pos, d) for d in DIRECTIONS]
            possible_moves = [m for m in possible_moves if m and board_to_tuple(m) not in map(board_to_tuple, individual['path'] + [current_board])]
            if not possible_moves:
                break
            current_board = random.choice(possible_moves)
            individual['path'].append(deepcopy(current_board))
        individual['board'] = current_board
        population.append(individual)

    for _ in range(generations):
        for individual in population:
            individual['fitness'] = fitness(individual['board'])
            if individual['board'] == goal:
                return individual['path']

        selected = []
        for _ in range(population_size):
            candidates = random.sample(population, min(5, len(population)))
            selected.append(deepcopy(max(candidates, key=lambda x: x['fitness'])))

        new_population = []
        for i in range(0, population_size, 2):
            if i + 1 >= len(selected):
                break
            parent1, parent2 = selected[i], selected[i + 1]
            child1 = {'board': deepcopy(start), 'path': []}
            child2 = {'board': deepcopy(start), 'path': []}

            min_path_len = min(len(parent1['path']), len(parent2['path']))
            if min_path_len <= 0:
                continue

            split_point = random.randint(0, min_path_len)

            current_board1 = deepcopy(start)
            for move in parent1['path'][:split_point] + parent2['path'][split_point:]:
                if is_valid_transition(current_board1, move):
                    child1['path'].append(deepcopy(move))
                    current_board1 = deepcopy(move)

            current_board2 = deepcopy(start)
            for move in parent2['path'][:split_point] + parent1['path'][split_point:]:
                if is_valid_transition(current_board2, move):
                    child2['path'].append(deepcopy(move))
                    current_board2 = deepcopy(move)

            child1['board'] = current_board1
            child2['board'] = current_board2
            new_population.extend([child1, child2])

        for individual in new_population:
            if random.random() < mutation_rate and len(individual['path']) > 0:
                mut_point = random.randint(0, len(individual['path']))
                individual['path'] = individual['path'][:mut_point]
                individual['board'] = deepcopy(individual['path'][-1]) if individual['path'] else deepcopy(start)
                for _ in range(random.randint(1, 5)):
                    empty_pos = find_empty(individual['board'])
                    possible_moves = [move_tile(individual['board'], empty_pos, d) for d in DIRECTIONS]
                    possible_moves = [m for m in possible_moves if m and board_to_tuple(m) not in map(board_to_tuple, individual['path'] + [individual['board']])]
                    if possible_moves:
                        individual['board'] = random.choice(possible_moves)
                        individual['path'].append(deepcopy(individual['board']))

        population = new_population[:population_size]

        for individual in population:
            if 'fitness' not in individual:
                individual['fitness'] = fitness(individual['board'])

        if not population:
            return None

    best = max(population, key=lambda x: x['fitness'])
    return best['path'] if best['board'] == goal else None

def and_or_tree_with_bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(board_to_tuple(start))

    class Node:
        def __init__(self, board, node_type, parent=None):
            self.board = board
            self.type = node_type 
            self.children = []
            self.parent = parent
            self.solved = False

    root = Node(start, 'OR')
    node_map = {board_to_tuple(start): root}
    solution_path = None
    
    while queue:
        current_board, path = queue.popleft()
        current_node = node_map.get(board_to_tuple(current_board))
        
        if current_board == goal:
            solution_path = path
            break
            
        empty_pos = find_empty(current_board)
        if empty_pos is None: 
            continue
        
        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board is None:
                continue
                
            board_key = board_to_tuple(new_board)
            if board_key not in visited:
                child_type = 'AND' if current_node.type == 'OR' else 'OR'
                child_node = Node(new_board, child_type, current_node)
                node_map[board_key] = child_node
                current_node.children.append(child_node)

                queue.append((new_board, path + [new_board]))
                visited.add(board_key)

    if solution_path:
        def mark_solved(node):
            if node.board == goal:
                node.solved = True
                return True
                
            if node.type == 'AND':
                node.solved = all(mark_solved(child) for child in node.children)
            else:
                node.solved = any(mark_solved(child) for child in node.children)
            return node.solved
        
        mark_solved(root)

        return solution_path
    
    return None

def q_learning_8_puzzle(start, goal, alpha=0.1, gamma=0.9, epsilon=0.2, episodes=5000):
    from collections import defaultdict

    def get_possible_moves(board):
        empty = find_empty(board)
        moves = []
        for direction in DIRECTIONS:
            new_board = move_tile(board, empty, direction)
            if new_board:
                moves.append((direction, new_board))
        return moves

    Q = defaultdict(lambda: defaultdict(float))
    goal_tuple = board_to_tuple(goal)

    for episode in range(episodes):
        board = deepcopy(start)
        board_tuple = board_to_tuple(board)

        for step in range(100):
            if board_tuple == goal_tuple:
                break

            if random.random() < epsilon:
                moves = get_possible_moves(board)
                if not moves:
                    break
                action, next_board = random.choice(moves)
            else:
                moves = get_possible_moves(board)
                if not moves:
                    break
                action, next_board = max(moves, key=lambda m: Q[board_tuple][m[0]])

            next_tuple = board_to_tuple(next_board)
            max_q_next = max(Q[next_tuple].values(), default=0)
            reward = 1 if next_tuple == goal_tuple else -0.1

            Q[board_tuple][action] += alpha * (
                reward + gamma * max_q_next - Q[board_tuple][action]
            )

            board = next_board
            board_tuple = next_tuple

    board = deepcopy(start)
    path = []
    for _ in range(100):
        board_tuple = board_to_tuple(board)
        if board_tuple == goal_tuple:
            break
        if not Q[board_tuple]:
            break
        action = max(Q[board_tuple], key=Q[board_tuple].get)
        next_board = move_tile(board, find_empty(board), action)
        if not next_board:
            break
        path.append(next_board)
        board = next_board

    return path if board == goal else None


def sarsa_8_puzzle(start, goal, alpha=0.1, gamma=0.9, epsilon=0.2, episodes=5000):
    from collections import defaultdict

    def get_possible_moves(board):
        empty = find_empty(board)
        moves = []
        for direction in DIRECTIONS:
            new_board = move_tile(board, empty, direction)
            if new_board:
                moves.append((direction, new_board))
        return moves

    Q = defaultdict(lambda: defaultdict(float))
    goal_tuple = board_to_tuple(goal)

    for episode in range(episodes):
        board = deepcopy(start)
        board_tuple = board_to_tuple(board)
        moves = get_possible_moves(board)
        if not moves:
            continue
        action, next_board = random.choice(moves) if random.random() < epsilon else max(
            moves, key=lambda m: Q[board_tuple][m[0]])

        for step in range(100):
            next_tuple = board_to_tuple(next_board)
            reward = 1 if next_tuple == goal_tuple else -0.1
            next_moves = get_possible_moves(next_board)
            if not next_moves:
                break

            next_action, next_board2 = random.choice(next_moves) if random.random() < epsilon else max(
                next_moves, key=lambda m: Q[next_tuple][m[0]])

            Q[board_tuple][action] += alpha * (
                reward + gamma * Q[next_tuple][next_action] - Q[board_tuple][action]
            )

            if next_tuple == goal_tuple:
                break

            board_tuple = next_tuple
            action = next_action
            next_board = next_board2

    board = deepcopy(start)
    path = []
    for _ in range(100):
        board_tuple = board_to_tuple(board)
        if board_tuple == goal_tuple:
            break
        if not Q[board_tuple]:
            break
        action = max(Q[board_tuple], key=Q[board_tuple].get)
        next_board = move_tile(board, find_empty(board), action)
        if not next_board:
            break
        path.append(next_board)
        board = next_board

    return path if board == goal else None

def backtracking_8_puzzle(start, goal, max_depth=50):
    visited = set()
    path = []

    def backtrack(board, depth):
        if depth > max_depth:
            return False
        board_t = board_to_tuple(board)
        if board_t in visited:
            return False
        visited.add(board_t)
        path.append(deepcopy(board))

        if board == goal:
            return True

        empty_pos = find_empty(board)
        for direction in DIRECTIONS:
            new_board = move_tile(board, empty_pos, direction)
            if new_board and backtrack(new_board, depth + 1):
                return True

        path.pop()
        return False

    if backtrack(start, 0):
        return path
    return None

def backtracking_with_forward_checking(start, goal, max_depth=50):
    visited = set()
    path = []

    def forward_check(board, depth):
        if depth > max_depth:
            return False
        board_t = board_to_tuple(board)
        if board_t in visited:
            return False
        visited.add(board_t)
        path.append(deepcopy(board))

        if board == goal:
            return True

        empty_pos = find_empty(board)
        possible_moves = []
        for direction in DIRECTIONS:
            new_board = move_tile(board, empty_pos, direction)
            if new_board and board_to_tuple(new_board) not in visited:
                possible_moves.append((heuristic(new_board, goal), new_board))
        
        possible_moves.sort(key=lambda x: x[0])
        for _, new_board in possible_moves:
            if forward_check(new_board, depth + 1):
                return True

        path.pop()
        return False

    if forward_check(start, 0):
        return path
    return None

def min_conflicts_8_puzzle(start, goal, max_steps=1000):
    current_board = deepcopy(start)
    path = [deepcopy(current_board)]

    for _ in range(max_steps):
        if current_board == goal:
            return path

        empty_pos = find_empty(current_board)
        neighbors = []

        for direction in DIRECTIONS:
            new_board = move_tile(current_board, empty_pos, direction)
            if new_board:
                conflicts = heuristic(new_board, goal)
                neighbors.append((conflicts, new_board))

        if not neighbors:
            return None

        neighbors.sort(key=lambda x: x[0])
        min_conflict = neighbors[0][0]
        best_neighbors = [b for c, b in neighbors if c == min_conflict]

        current_board = random.choice(best_neighbors)
        path.append(deepcopy(current_board))

    return None  

class PuzzleApp:
    def __init__(self, root):
        self.flag = False
        self.root = root
        self.root.configure(bg="lightgray")
        self.root.title("8-Puzzle Solver")
        self.root.geometry("1300x380")

        self.start_state = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

        self.solution = []
        self.current_step = 0
        self.step_count = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", width=5, height=2, font=("Arial", 20, "bold"))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=10)
        
        self.state_label = tk.Label(self.root, text="State Tuple:", font=("Arial", 12))
        self.state_label.place(x=330, y=20)

        self.state_frame = tk.Frame(self.root)
        self.state_frame.place(x=330, y=50, width=100, height=260)

        self.state_scrollbar = tk.Scrollbar(self.state_frame)
        self.state_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.state_text = tk.Text(self.state_frame, height=10, width=25, font=("Arial", 15), yscrollcommand=self.state_scrollbar.set)
        self.state_text.pack(side=tk.LEFT, fill=tk.BOTH)

        self.state_scrollbar.config(command=self.state_text.yview)



        self.text_box1 = tk.Text(root, height=2, width=5)
        self.text_box1.place(x=1100, y=20)

        self.text_box2 = tk.Text(root, height=2, width=5)
        self.text_box2.place(x=1160, y=20)

        self.text_box3 = tk.Text(root, height=2, width=5)
        self.text_box3.place(x=1220, y=20)

        self.text_box4 = tk.Text(root, height=2, width=5)
        self.text_box4.place(x=1100, y=70)

        self.text_box5 = tk.Text(root, height=2, width=5)
        self.text_box5.place(x=1160, y=70)

        self.text_box6 = tk.Text(root, height=2, width=5)
        self.text_box6.place(x=1220, y=70)

        self.text_box7 = tk.Text(root, height=2, width=5)
        self.text_box7.place(x=1100, y=120)

        self.text_box8 = tk.Text(root, height=2, width=5)
        self.text_box8.place(x=1160, y=120)

        self.text_box9 = tk.Text(root, height=2, width=5)
        self.text_box9.place(x=1220, y=120)

        self.update_board(self.start_state)

        self.algo_frame1 = tk.Frame(root, bg="lightgray")
        self.algo_frame1.place(x=450, y=20)

        self.algo_frame2 = tk.Frame(root, bg="lightgray")
        self.algo_frame2.place(x=450, y=70)

        self.algo_frame3 = tk.Frame(root, bg="lightgray")
        self.algo_frame3.place(x=450, y=120)

        self.algo_frame4 = tk.Frame(root, bg="lightgray")
        self.algo_frame4.place(x=450, y=170)

        self.algo_frame5 = tk.Frame(root, bg="lightgray")
        self.algo_frame5.place(x=190, y=340)

        self.algo_frame6 = tk.Frame(root, bg="lightgray")
        self.algo_frame6.place(x=450, y=220)

        self.algo_frame7 = tk.Frame(root, bg="lightgray")
        self.algo_frame7.place(x=450, y=270)

        self.algo_frame8 = tk.Frame(root, bg="lightgray")
        self.algo_frame8.place(x=450, y=320)

        self.import_data_btn = tk.Button(root, text="Import Data", font=("Arial", 12), width=10, height=1, command=self.import_data)
        self.import_data_btn.place(x=1130, y=180)

        self.import_data_btn = tk.Button(root, text="Random", font=("Arial", 12), width=10, height=1, command=self.generate_random)
        self.import_data_btn.place(x=1130, y=230)

        self.bfs_btn = tk.Button(self.algo_frame1, text="BFS", font=("Arial", 12), command=lambda: self.solve_puzzle(bfs_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame1, text="DFS", font=("Arial", 12), command=lambda: self.solve_puzzle(dfs_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")
        
        self.greedy_btn = tk.Button(self.algo_frame2, text="Greedy", font=("Arial", 12), command=lambda: self.solve_puzzle(greedy_8_puzzle))
        self.greedy_btn.pack(side=tk.LEFT, padx=3, anchor="w")
        
        self.ucs_btn = tk.Button(self.algo_frame1, text="UCS", font=("Arial", 12), command=lambda: self.solve_puzzle(ucs_8_puzzle))
        self.ucs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame1, text="Iterative Deepening", font=("Arial", 12), command=lambda: self.solve_puzzle(iterative_deepening_ucs_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")
        
        self.a_star_btn = tk.Button(self.algo_frame2, text="A*", font=("Arial", 12), command=lambda: self.solve_puzzle(a_star_8_puzzle))
        self.a_star_btn.pack(side=tk.LEFT, padx=3, anchor="w")
        
        self.ida_star_btn = tk.Button(self.algo_frame2, text="IDA*", font=("Arial", 12), command=lambda: self.solve_puzzle(ida_star_8_puzzle))
        self.ida_star_btn.pack(side=tk.LEFT, padx=3, anchor="w")
        
        self.bfs_btn = tk.Button(self.algo_frame4, text="AND OR BFS", font=("Arial", 12), command=lambda: self.solve_puzzle(and_or_tree_with_bfs))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame4, text="Belief", font=("Arial", 12), command=lambda: self.solve_puzzle(and_or_tree_with_bfs))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")
        
        self.reset_btn = tk.Button(self.algo_frame8, text="Reset", font=("Arial", 12), command=self.reset_board)
        self.reset_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.shc_btn = tk.Button(self.algo_frame3, text="SHC", font=("Arial", 12), command=lambda: self.solve_puzzle(hill_climbing))
        self.shc_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.sahc_btn = tk.Button(self.algo_frame3, text="Simulated Annealing", font=("Arial", 12), command=lambda: self.solve_puzzle(simulated_annealing))
        self.sahc_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame3, text="Beam", font=("Arial", 12), command=lambda: self.solve_puzzle(beam_search_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame3, text="Genetic", font=("Arial", 12), command=lambda: self.solve_puzzle(genetic_algorithm_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame3, text="Steepest Ascent HC", font=("Arial", 12), command=lambda: self.solve_puzzle(steepest_hill_climbing))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame3, text="Stochastic HC", font=("Arial", 12), command=lambda: self.solve_puzzle(stochastic_hill_climbing))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")    
        
        self.step_label = tk.Label(self.algo_frame5, text="Steps: 0", font=("Arial", 12))
        self.step_label.grid(row=0, column=0, padx=3, sticky="w")

        self.bfs_btn = tk.Button(self.algo_frame6, text="Q Learning", font=("Arial", 12), command=lambda: self.solve_puzzle(q_learning_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame7, text="Backtracking", font=("Arial", 12), command=lambda: self.solve_puzzle(backtracking_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame7, text="Backtracking with Forward Checking", font=("Arial", 12), command=lambda: self.solve_puzzle(backtracking_with_forward_checking))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame7, text="Min-Conflicts", font=("Arial", 12), command=lambda: self.solve_puzzle(min_conflicts_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.bfs_btn = tk.Button(self.algo_frame6, text="Sarsa", font=("Arial", 12), command=lambda: self.solve_puzzle(sarsa_8_puzzle))
        self.bfs_btn.pack(side=tk.LEFT, padx=3, anchor="w")

        self.time_label = tk.Label(self.algo_frame5, text="Time: 0s", font=("Arial", 12))
        self.time_label.grid(row=0, column=1, padx=3, sticky="w")

    def display_tuple_state(self, board):
        board_tuple = tuple(tuple(row) for row in board)
        for row in board_tuple:
            self.state_text.insert(tk.END, str(row) + "\n")
        self.state_text.insert(tk.END, "\n")  # Dòng trắng phân cách giữa các trạng thái
        self.state_text.see(tk.END)

    def update_board(self, board):
        for i in range(3):
            for j in range(3):
                value = board[i][j]
                self.buttons[i][j].config(text=str(value) if value != 0 else "")

    def solve_puzzle(self, algorithm):
        start_time = time.perf_counter()
        if self.start_state == self.goal_state or self.flag == True:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            self.time_label.config(text=f"Time: {execution_time:.6f}s")
            messagebox.showinfo("Thành công", "Trạng thái bắt đầu đã là đích!")
            return

        self.solution = algorithm(self.start_state, self.goal_state)
        self.flag = True;
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        self.time_label.config(text=f"Time: {execution_time:.6f}s")

        if self.solution:
            self.current_step = 0
            self.step_count = 0
            self.animate_solution()
        else:
            messagebox.showerror("Error", "No solution found!")


    def animate_solution(self):
        if self.current_step < len(self.solution):
            self.update_board(self.solution[self.current_step])
            self.display_tuple_state(self.solution[self.current_step])
            self.current_step += 1
            self.step_count = self.current_step
            self.step_label.config(text=f"Steps: {self.step_count}")
            self.root.after(500, self.animate_solution)
        else:
            messagebox.showinfo("Thành công", "Đã giải xong bài toán!")

    def generate_random(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(numbers)
        self.start_state = [
            [numbers[0], numbers[1], numbers[2]],
            [numbers[3], numbers[4], numbers[5]],
            [numbers[6], numbers[7], numbers[8]]
        ]
        self.update_board(self.start_state)

    def import_data(self):
        try:
            self.number1 = int(self.text_box1.get("1.0", "end-1c"))
            self.number2 = int(self.text_box2.get("1.0", "end-1c"))
            self.number3 = int(self.text_box3.get("1.0", "end-1c"))
            self.number4 = int(self.text_box4.get("1.0", "end-1c"))
            self.number5 = int(self.text_box5.get("1.0", "end-1c"))
            self.number6 = int(self.text_box6.get("1.0", "end-1c"))
            self.number7 = int(self.text_box7.get("1.0", "end-1c"))
            self.number8 = int(self.text_box8.get("1.0", "end-1c"))
            self.number9 = int(self.text_box9.get("1.0", "end-1c"))

            self.start_state = [
                [self.number1, self.number2, self.number3],
                [self.number4, self.number5, self.number6],
                [self.number7, self.number8, self.number9]
            ]
            self.update_board(self.start_state)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

    def reset_board(self):
        self.update_board(self.start_state)
        self.step_count = 0
        self.step_label.config(text="Steps: 0")
        self.time_label.config(text="Time: 0s")
        self.text_box1.delete("1.0", tk.END)
        self.text_box2.delete("1.0", tk.END)
        self.text_box3.delete("1.0", tk.END)
        self.text_box4.delete("1.0", tk.END)
        self.text_box5.delete("1.0", tk.END)
        self.text_box6.delete("1.0", tk.END)
        self.text_box7.delete("1.0", tk.END)
        self.text_box8.delete("1.0", tk.END)
        self.text_box9.delete("1.0", tk.END)
        self.state_text.delete("1.0", tk.END)
        self.flag = False

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleApp(root)
    root.mainloop() 
