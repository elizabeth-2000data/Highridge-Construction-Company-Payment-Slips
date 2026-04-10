# Highridge Construction Company — Weekly Payment Generator

A Python and R program that dynamically generates weekly payment slips
for 420 construction workers, classifies each by employee level, and
prints a payroll summary.

---

## Files in this project

- `payment_generator.py` — Python implementation
- `payment_generator.R`  — R implementation
- `README.md`            — This file

---

## Employee Level Rules

| Level | Condition |
|-------|-----------|
| A5-F  | Salary > $7,500 AND < $30,000 AND gender is Female |
| A1    | Salary > $10,000 AND < $20,000 |
| N/A   | Does not meet any criterion |

Note: A5-F is checked first. A female worker in the $10k–$20k range
gets A5-F, not A1.

---

## How to run the Python code

### Requirements
- Python 3.10 or higher
- No external packages needed (uses built-in `random` module only)

### Check Python is installed