import random

random.seed(42)

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

# Step 2: Dynamically create a list of 420 workers
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

# Step 3 & 4: For loop with conditional statements + Step 5: Exception handling
payment_slips = []

for worker in workers:
    try:
        salary = worker["salary"]
        gender = worker["gender"]

        if not isinstance(salary, (int, float)):
            raise TypeError(f"Invalid salary type for {worker['id']}")
        if salary < 0:
            raise ValueError(f"Negative salary for {worker['id']}")

        # Conditional 1 & 2 — A5-F checked first (takes priority)
        if salary > 7500 and salary < 30000 and gender == "Female":
            level = "A5-F"
        elif salary > 10000 and salary < 20000:
            level = "A1"
        else:
            level = "N/A"

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
        print(f"Error processing worker: {e}")

# Print first 10 slips
print("Sample payment slips:")
print("-" * 70)
for slip in payment_slips[:10]:
    print(f"[{slip['id']}] {slip['name']:<28} | {slip['gender']:<6} | "
          f"${slip['salary']:>10,.2f} | Level: {slip['level']}")

# Summary
from collections import Counter
levels = Counter(s["level"] for s in payment_slips)
print(f"\nTotal slips generated: {len(payment_slips)}")
print(f"Total payroll: ${sum(s['salary'] for s in payment_slips):,.2f}")
print("\nEmployee Level Distribution:")
for lvl, count in sorted(levels.items()):
    print(f"  {lvl}: {count} workers")