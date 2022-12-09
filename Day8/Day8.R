library(stringr)

connection <- file(description = "Day8Input.txt", open = "r")
grid <- unname(sapply(readLines(connection), function(x) { as.numeric(str_split(x, "")[[1]]) }))
close(connection)

grid_vector <- sapply(grid, function(x) { x })
n <- nrow(grid) # square grid

is_visible <- function(height, directions) {
  for (direction in directions) { if ((length(direction) == 0) | ((sum(direction < height) == length(direction)))) { return(T) } }
  return(F)
}

find_scenic_score <- function(height, directions) {
  return(prod(sapply(directions, function(x) {
    if (length(x) == 0) { return(0) }
    else {
      not_visible <- which(x >= height)
      if (length(not_visible) > 0) { return(not_visible[1]) }
      else { return(length(x)) }
    }
  })))
}

find_tree_info <- function(grid_vector, n, score) {
  tree_info <- sapply(1:n**2, function(x) {
    r <- x %% n
    height <- grid_vector[x]
    if (x > 1) { before_i <- (1:n**2)[1:(x - 1)] }
    else { before_i <- as.numeric(c()) }
    if (x < n**2) { after_i <- (1:n**2)[(x+1):n**2] }
    else { after_i <- as.numeric(c()) }
    
    above <- rev(grid_vector[before_i[before_i %% n == r]])
    if (x <= n) { above <- as.numeric(c()) }
    below <- grid_vector[after_i[after_i %% n == r]]
    if (x >= n*(n-1) + 1) { below <- as.numeric(c()) }
    if (length(before_i) == 0) { left <- as.numeric(c()) }
    if (x %% n == 1) { left <- as.numeric(c()) }
    else { left <- rev(grid_vector[tail((before_i[before_i %% n == 1]), 1):(x-1)]) }
    if (length(after_i) == 0) { right <- as.numeric(c()) }
    if (x %% n == 0) { right <- as.numeric(c()) }
    else { right <- grid_vector[(x+1):(after_i[after_i %% n == 0][1])] }
    
    if (score) { find_scenic_score(height, list(above, below, left, right)) }
    else { is_visible(height, list(above, below, left, right)) }
  })
  if (score) { return(max(tree_info)) }
  else { return(sum(tree_info)) }
}

# puzzle answers
print(paste0("puzzle 1 answer = ", find_tree_info(grid_vector, n, FALSE)))
print(paste0("puzzle 1 answer = ", find_tree_info(grid_vector, n, TRUE)))
