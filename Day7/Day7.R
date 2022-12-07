connection <- file(description = "Day7Input.txt", open = "r")
directories <- hash()
path <- ""
for (line in readLines(connection)) {
  if (str_sub(line, 1, 1) == "$"){
    if (str_sub(line, 3, 4) == "cd") {
      if (str_sub(line, 6, 7) != "..") {
        path <- paste(path, str_sub(line, 6, nchar(line)))
        directories[[path]] <- c("")
      }
      else { 
        path_split <- str_split(path, " ")[[1]]
        path <- paste(path_split[1:(length(path_split) - 1)], collapse = " ")
      }
    }
  }
  else {
    if (nchar(path) > 0) {
      if (length(directories[[path]]) == 1 & directories[[path]][1] == "") { directories[[path]] <- line }
      else { directories[[path]] <- c(directories[[path]], line) }
    }
  }
}
close(connection)

sum_sizes <- function(files) { return(sum(as.numeric(sapply(str_split(files, " "), function(x) { x[1] })))) }

sizes <- hash()
while (TRUE) {
  for (key in keys(directories)) {
    directories_i <- str_detect(directories[[key]], pattern = "dir")
    if (sum(directories_i) == 0) { sizes[[key]] <- sum_sizes(directories[[key]]) }
    else {
      need <- sapply(str_split(directories[[key]][directories_i], " "), function(x) { paste(key, x[2]) })
      if (length(keys(sizes)) > 0) {
        if (length(intersect(need, keys(sizes))) == length(need)) {
          sizes[[key]] <- sum_sizes(directories[[key]][!directories_i]) + sum(sapply(need, function(x) { sizes[[x]] }))
        }
      }
    }
  }
  if (length(keys(sizes)) == length(keys(directories))) { break }
}

space_available <- 70000000
space_required <- 30000000
space_used <- sizes[[" /"]]
space_unused <- space_available - space_used
space_needed <- space_required - space_unused

# puzzle answers
print(paste0("puzzle 1 answer = ", sum(values(sizes)[values(sizes) <= 100000])))
print(paste0("puzzle 2 answer = ", min(values(sizes)[values(sizes) >= space_needed])))
