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

- Python 3.10 or higher — download from https://python.org/downloads
- R 4.0 or higher — download from https://cran.r-project.org
- Git Bash — download from https://git-scm.com/downloads
- No external libraries or packages needed for either language

---

## How to use the Python code

1. Make sure Python is installed by running:
   python --version

2. Navigate into the project folder:
   cd highridge

3. Run the program:
   python payment_generator.py

4. You will see 420 payment slips generated with employee levels
   and a full payroll summary printed at the end.

---

## How to use the R code

1. Make sure R is installed by running:
   Rscript --version

2. If you get "command not found", add R to your PATH by running:
   export PATH=$PATH:"/c/Program Files/R/R-4.5.3/bin"

3. Navigate into the project folder:
   cd highridge

4. Run the program:
   Rscript payment_generator.R

5. You will see the same output as the Python version — 420 payment
   slips and a payroll summary.

---

## Author

Elizabeth — Highridge Construction Company Assignment
Languages: Python, R
Tools: Git, GitHub, VS Code, Git Bash