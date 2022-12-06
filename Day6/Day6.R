library(stringr)

input <- read.csv("Day6Input.txt", header = FALSE)[1,1]

find_marker <- function(string, marker_type) {
  if (marker_type == "packet") { n <- 4 }
  if (marker_type == "message") { n <- 14 }
  for (i in n:nchar(string)) {
    if (sum(table(str_split(str_sub(string, i-n+1, i), pattern = "")[[1]]) > 1) == 0) { return(i) }
  }
}

# puzzle answers
print(paste0("puzzle 1 answer = ", find_marker(input, "packet")))
print(paste0("puzzle 1 answer = ", find_marker(input, "message")))
