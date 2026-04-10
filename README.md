# Highridge Construction Company — Weekly Payment Generator

This project automates weekly payment slip generation for 420 construction
workers using Python and R.

---

## Files

- payment_generator.py — Python implementation
- payment_generator.R  — R implementation
- README.md            — Project documentation

---

## How it works

- Dynamically generates a list of 420 workers with unique IDs, names, roles, and salaries
- Loops through every worker and produces a payment slip
- Classifies each worker into an employee level based on salary and gender
- Handles errors without crashing the program

---

## Employee Level Rules

- A5-F: Salary between $7,500 and $30,000 and employee is Female
- A1:   Salary between $10,000 and $20,000
- N/A:  Does not meet any criteria

Note: A5-F is checked first and takes priority over A1.

---

## Requirements

- Python 3.10 or higher
- R 4.0 or higher
- No external libraries or packages needed for either language

---

## How to run

Python:
  python payment_generator.py

R:
  Rscript payment_generator.R

---

## Author

Elizabeth — Highridge Construction Company Assignment
Languages: Python, R
Tools: Git, GitHub, VS Code, Git Bash