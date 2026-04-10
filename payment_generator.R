set.seed(42)

# Name and role data used to build worker records dynamically
first_names_male <- c("James","John","Robert","Michael","William","David",
  "Richard","Joseph","Thomas","Charles","Christopher","Daniel",
  "Matthew","Anthony","Mark","Donald","Steven","Paul","Andrew","Kenneth")

first_names_female <- c("Mary","Patricia","Jennifer","Linda","Barbara",
  "Elizabeth","Susan","Jessica","Sarah","Karen","Lisa","Nancy",
  "Betty","Margaret","Sandra","Ashley","Dorothy","Kimberly","Emily","Donna")

last_names <- c("Smith","Johnson","Williams","Brown","Jones","Garcia",
  "Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez",
  "Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin")

roles <- c("Site Engineer","Project Manager","Foreman","Electrician",
  "Plumber","Carpenter","Mason","Welder","Safety Officer","Equipment Operator")

# Dynamically build a data frame of 420 worker records
count    <- 420
genders  <- sample(c("Male","Female"), count, replace = TRUE)
salaries <- round(runif(count, 5000, 35000), 2)
firsts   <- ifelse(genders == "Male",
                   sample(first_names_male,   count, replace = TRUE),
                   sample(first_names_female, count, replace = TRUE))

workers <- data.frame(
  id     = sprintf("HCC-%04d", 1:count),
  name   = paste(firsts, sample(last_names, count, replace = TRUE)),
  gender = genders,
  role   = sample(roles, count, replace = TRUE),
  salary = salaries,
  stringsAsFactors = FALSE
)

cat(sprintf("Generated %d workers.\n\n", nrow(workers)))

# Loop through all workers and generate a payment slip for each one
payment_slips <- list()

for (i in seq_len(nrow(workers))) {
  tryCatch({
    w      <- workers[i, ]
    salary <- w$salary
    gender <- w$gender

    # Validate salary is numeric
    if (!is.numeric(salary)) stop(paste("Invalid salary for", w$id))

    # Salary must not be negative
    if (salary < 0) stop(paste("Negative salary for", w$id))

    # Assign employee level based on salary and gender
    # A5-F is checked first — a qualifying female takes this level over A1
    if (salary > 7500 && salary < 30000 && gender == "Female") {
      level <- "A5-F"
    } else if (salary > 10000 && salary < 20000) {
      level <- "A1"
    } else {
      level <- "N/A"
    }

    # Build the payment slip for this worker
    payment_slips[[i]] <- data.frame(
      id = w$id, name = w$name, gender = gender,
      role = w$role, salary = salary, level = level,
      stringsAsFactors = FALSE
    )

  }, error = function(e) {
    # Log the error and continue processing remaining workers
    cat(sprintf("Error on row %d: %s\n", i, conditionMessage(e)))
  })
}

# Combine all slips into a single data frame
slips <- do.call(rbind, Filter(Negate(is.null), payment_slips))

# Print a preview of the first 10 payment slips
cat("Sample payment slips:\n")
cat(strrep("-", 70), "\n")
for (i in 1:min(10, nrow(slips))) {
  s <- slips[i, ]
  cat(sprintf("[%s] %-28s | %-6s | $%10.2f | Level: %s\n",
              s$id, s$name, s$gender, s$salary, s$level))
}

# Print overall payroll summary
level_counts <- table(slips$level)
cat(sprintf("\nTotal slips: %d\n", nrow(slips)))
cat(sprintf("Total payroll: $%s\n", format(sum(slips$salary), big.mark=",")))
cat("\nEmployee Level Distribution:\n")
for (lvl in sort(names(level_counts))) {
  cat(sprintf("  %s: %d workers\n", lvl, level_counts[[lvl]]))
}