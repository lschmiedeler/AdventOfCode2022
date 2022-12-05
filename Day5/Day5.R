library(stringr)

connection <- file(description = "Day5Input.txt", open = "r")
procedure <- FALSE
stacks <- c()
steps <- list()
for (line in readLines(connection)) {
  if (str_detect(line, "\\[", negate = TRUE)) { procedure <- TRUE }
  if (!procedure) {
    index <- seq(from = 2, to = nchar(line), by = 4)
    for (i in 1:length(index)) {
      crate <- str_sub(line, index[i], index[i])
      if (crate != " ") {
        if (length(stacks) > 0) {
          if (!is.na(stacks[i])) { stacks[i] <- paste0(stacks[i], crate) }
          else { stacks[i] <- crate }
        }
        else { stacks[i] <- crate }
      }
    }
  }
  else {
    if (str_detect(line, pattern = "move")) {
      step <- as.numeric(str_split(line, pattern = "move | from | to ")[[1]][2:4])
      steps <- c(steps, list(step))
    }
  }
}
close(connection)

move_crates <- function(stacks, move_multiple) {
  for (step in steps) {
    n <- step[1]
    from_stack <- step[2]
    to_stack <- step[3]
    crates <- str_sub(stacks[from_stack], 1, n)
    stacks[from_stack] <- str_sub(stacks[from_stack], n + 1, nchar(stacks[from_stack]))
    if (move_multiple) { stacks[to_stack] <- paste0(paste0(str_split(crates, pattern = "")[[1]], collapse = ""), stacks[to_stack]) }
    else { stacks[to_stack] <- paste0(paste0(rev(str_split(crates, pattern = "")[[1]]), collapse = ""), stacks[to_stack]) }
  }
  return(paste0(str_sub(stacks, 1, 1), collapse = ""))
}

# puzzle answers
print(paste0("puzzle 1 answer = ", move_crates(stacks, FALSE)))
print(paste0("puzzle 2 answer = ", move_crates(stacks, TRUE)))
