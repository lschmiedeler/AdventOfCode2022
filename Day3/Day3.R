library(stringr)

rucksacks <- as.list(read.csv("Day3Input.txt", header = F, sep = "\n")[,1])

find_common_char <- function(x) {
  common_char <- c()
  str_1 <- x[1]
  for (i in 1:(length(x)-1)) {
    str_2 <- x[i+1]
    new_common_char <- sort(str_extract(str_1, str_split(str_2, pattern = "")[[1]]))
    if (i > 1) { common_char <- unique(intersect(common_char, new_common_char)) }
    else { common_char <- unique(new_common_char) }
  }
  return(common_char)
}

find_priority <- function(c) {
  ascii_dec <- as.numeric(charToRaw(c))
  if (ascii_dec <= 90) { return(ascii_dec - 38) }
  else { return(ascii_dec - 96) }
}

priorities_1 <- sapply(lapply(rucksacks, function(x) {
  c_1 <- substring(x, 1, nchar(x)/2)
  c_2 <- substring(x, 1 + nchar(x)/2, nchar(x))
  find_priority(find_common_char(c(c_1, c_2)))
}), function(x) { x })

priorities_2 <- c()
for (i in seq(from = 1, to = length(rucksacks), by = 3)) {
  priorities_2 <- c(priorities_2, find_priority(find_common_char(c(rucksacks[[i]], rucksacks[[i+1]], rucksacks[[i+2]]))))
}

# puzzle answers
print(paste0("puzzle 1 answer = ", sum(priorities_1)))
print(paste0("puzzle 2 answer = ", sum(priorities_2)))
