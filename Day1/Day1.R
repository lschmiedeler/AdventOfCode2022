connection <- file(description = "Day1Input.txt", open = "r")
all_calories <- c()
calories <- 0
for (line in readLines(connection)) {
  if (line == "") {
    all_calories <- append(all_calories, calories)
    calories <- 0
  } else { calories <- calories + as.integer(line) }
}
close(connection)

# puzzle answers
print(paste0("puzzle 1 answer = ", max(all_calories)))
print(paste0("puzzle 2 answer = ", sum(sort(all_calories, decreasing = TRUE)[1:3])))
