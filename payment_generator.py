import random

random.seed(42)

# Name and role data used to build worker records dynamically
first_names_male = ["James", "John", "Robert", "Michael", "William", "David",
    "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel",
    "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Kenneth"]

first_names_female = ["Mary", "Patricia", "Jennifer", "Linda", "Barbara",
    "Elizabeth", "Susan", "Jessica", "Sarah", "Karen", "Lisa", "Nancy",
    "Betty", "Margaret", "Sandra", "Ashley", "Dorothy", "Kimberly", "Emily", "Donna"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
    "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez",
    "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

roles = ["Site Engineer", "Project Manager", "Foreman", "Electrician",
    "Plumber", "Carpenter", "Mason", "Welder", "Safety Officer", "Equipment Operator"]

# Dynamically build a list of 420 worker dictionaries
workers = []
for i in range(1, 421):
    gender = random.choice(["Male", "Female"])
    first = random.choice(first_names_male if gender == "Male" else first_names_female)
    worker = {
        "id": f"HCC-{i:04d}",
        "name": f"{first} {random.choice(last_names)}",
        "gender": gender,
        "role": random.choice(roles),
        "salary": round(random.uniform(5000, 35000), 2),
    }
    workers.append(worker)

print(f"Generated {len(workers)} workers.\n")

# Loop through all workers and generate a payment slip for each one
payment_slips = []

for worker in workers:
    try:
        salary = worker["salary"]
        gender = worker["gender"]

        # Validate salary is a valid number
        if not isinstance(salary, (int, float)):
            raise TypeError(f"Invalid salary type for {worker['id']}")

        # Salary must not be negative
        if salary < 0:
            raise ValueError(f"Negative salary for {worker['id']}")

        # Assign employee level based on salary and gender
        # A5-F is checked first — a qualifying female takes this level over A1
        if salary > 7500 and salary < 30000 and gender == "Female":
            level = "A5-F"
        elif salary > 10000 and salary < 20000:
            level = "A1"
        else:
            level = "N/A"

        # Build the payment slip for this worker
        slip = {
            "id":     worker["id"],
            "name":   worker["name"],
            "gender": gender,
            "role":   worker["role"],
            "salary": salary,
            "level":  level,
        }
        payment_slips.append(slip)

    except (KeyError, TypeError, ValueError) as e:
        # Log the error and continue processing remaining workers
        print(f"Error processing worker: {e}")

# Print a preview of the first 10 payment slips
print("Sample payment slips:")
print("-" * 70)
for slip in payment_slips[:10]:
    print(f"[{slip['id']}] {slip['name']:<28} | {slip['gender']:<6} | "
          f"${slip['salary']:>10,.2f} | Level: {slip['level']}")

# Print overall payroll summary
from collections import Counter
levels = Counter(s["level"] for s in payment_slips)
print(f"\nTotal slips generated: {len(payment_slips)}")
print(f"Total payroll: ${sum(s['salary'] for s in payment_slips):,.2f}")
print("\nEmployee Level Distribution:")
for lvl, count in sorted(levels.items()):
    print(f"  {lvl}: {count} workers")