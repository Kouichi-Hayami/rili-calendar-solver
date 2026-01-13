# Calendar Puzzle Solver (Pintu)

A Python-based solver and visualizer for a **calendar puzzle** (日历拼图).

This project computes **all valid tilings** of a physical calendar puzzle board given a target **month**, **day**, and optionally **weekday**, and provides an **interactive page-flipping visualization** to browse every solution.

The project supports two puzzle variants:

- **Standard puzzle**: Month + Day  
- **Extended puzzle**: Month + Day + Weekday  

The solver automatically selects the appropriate puzzle based on user input.

---

## Overview

Calendar puzzles are mechanical tiling puzzles where a set of fixed polyomino-like pieces must exactly cover a board, leaving specific cells empty to indicate the current date.

This project models the puzzle as a **constraint satisfaction problem** and solves it using **recursive backtracking**, while eliminating symmetric duplicates via rotation and reflection normalization.

Key goals of this project:
- Correctness: enumerate **all** valid solutions
- Clarity: keep algorithm and visualization cleanly separated
- Usability: interactive browsing instead of console spam

---

## Project Structure

```
.
├── rilie.py        # User input, puzzle selection, configuration
├── shape.py        # Core solver, backtracking, visualization
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Requirements

- Python **3.8+**
- Dependencies:
  - `numpy`
  - `matplotlib`

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## How to Run

From the project root directory:

```bash
python rilie.py
```

---

## Interactive Input Flow

The program prompts the user **step by step**:

```
请输入月份 (1-12):
请输入日期 (1-31):
请输入星期 (1=Mon ... 7=Sun，可留空):
```

### Input Rules

- **Month**: integer `1`–`12`
- **Day**: integer `1`–`31`
- **Weekday**:
  - Enter `1–7` (`1 = Mon`, `7 = Sun`) → uses extended puzzle
  - Press **Enter** directly → uses standard puzzle

---

## Puzzle Variants

### Standard Puzzle (`rilie`)

- Two empty cells:
  - Month
  - Day

### Extended Puzzle (`rilie_w`)

- Three empty cells:
  - Month
  - Day
  - Weekday

---

## Visualization

- All valid solutions are collected first
- A **single matplotlib window** opens after solving
- Use **Prev / Next** buttons to browse solutions
- Calendar labels are drawn directly inside empty cells

---

## Algorithm Details

- Shapes are normalized to `(0, 0)`
- All unique orientations are generated via rotation and reflection
- Recursive backtracking fills the board cell by cell
- Each complete tiling is stored and visualized

---

## License

This project is intended for educational and personal use.
