library(stringr)
library(tidyverse)

connection <- file(description = "Day9Input.txt", open = "r")
motions <- readLines(connection)
close(connection)

update_tail <- function(head, tail) {
  case_when((head[1] == tail[1]) & (abs(head[2] - tail[2]) == 2) ~ c(tail[1], tail[2] + sign(head[2] - tail[2])),
            (head[2] == tail[2]) & (abs(head[1] - tail[1]) == 2) ~ c(tail[1] + sign(head[1] - tail[1]), tail[2]),
            (((abs(head[1] - tail[1]) == 1) & (abs(head[2] - tail[2]) == 2)) | ((abs(head[1] - tail[1]) == 2) & (abs(head[2] - tail[2]) == 1)) |
               ((abs(head[1] - tail[1]) == 2) & (abs(head[2] - tail[2]) == 2))) ~ c(tail[1] + sign(head[1] - tail[1]), tail[2] + sign(head[2] - tail[2])),
            TRUE ~ tail)
}

simulate_rope <- function(motions, n_knots) {
  tail_positions <- list()
  knots <- list()
  for (i in 1:n_knots) { knots <- c(knots, list(c(0,0))) }
  for (motion in motions) {
    motion <- str_split(motion, " ")[[1]]
    steps <- as.numeric(motion[2])
    for (step in 1:steps) {
      knots[[1]] <- case_when(motion[1] == "R" ~ c(knots[[1]][1] + 1, knots[[1]][2]), motion[1] == "L" ~ c(knots[[1]][1] - 1, knots[[1]][2]),
                              motion[1] == "U" ~ c(knots[[1]][1], knots[[1]][2] + 1), motion[1] == "D" ~ c(knots[[1]][1], knots[[1]][2] - 1))
      for (i in 2:n_knots) { knots[[i]] <- update_tail(knots[[i-1]], knots[[i]]) }
      tail_positions <- unique(c(tail_positions, list(knots[[n_knots]])))
    }
  }
  return(length(tail_positions))
}

# puzzle answers
print(paste0("puzzle 1 answer = ", simulate_rope(motions, 2)))
print(paste0("puzzle 2 answer = ", simulate_rope(motions, 10)))
