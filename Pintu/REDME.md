# Calendar Puzzle Solver (Pintu)

A Python solver and visualizer for a **calendar puzzle** (日历拼图).

Given a target **month**, **day**, and optionally **weekday**, the program computes **all valid tilings** of the puzzle board and lets you **browse every solution interactively** using a page-flipping interface.

This project supports:
- A standard calendar puzzle (month + day)
- An extended version with weekday support (month + day + weekday)

---

## ✨ Features

- 🧩 Backtracking-based puzzle solver
- 🔄 Automatic handling of rotations and reflections
- 📅 Supports **Month / Day / (Optional) Weekday**
- 🖼 Interactive visualization using `matplotlib`
- ⬅️ ➡️ Flip through **all valid solutions**
- 🔤 Calendar labels displayed directly in empty cells
  - Month shown as `Jan`, `Feb`, `Mar`, etc.
  - Day shown as number
  - Weekday shown as `Mon`, `Tue`, etc.

---

## 📂 Project Structure

