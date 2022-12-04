pairs <- as.list(read.csv("Day4Input.txt", header = F, sep = "\n")$V1)

fully_contained <- sapply(lapply(pairs, function(pair) {
  sections <- strsplit(pair, split = ",")[[1]]
  section_1 <- as.numeric(strsplit(sections[1], split = "-")[[1]])
  section_2 <- as.numeric(strsplit(sections[2], split = "-")[[1]])
  if (section_1[1] >= section_2[1] & section_1[2] <= section_2[2] |
      section_2[1] >= section_1[1] & section_2[2] <= section_1[2]) { return(1) }
  else { return(0) }
}), function(x) { x })

overlap <- sapply(lapply(pairs, function(pair) {
  sections <- strsplit(pair, split = ",")[[1]]
  section_1 <- as.numeric(strsplit(sections[1], split = "-")[[1]])
  section_2 <- as.numeric(strsplit(sections[2], split = "-")[[1]])
  if (section_1[2] >= section_2[1] & section_1[1] <= section_2[2]) { return(1) }
  else { return(0) }
}), function(x) { x })

# puzzle answers
print(paste0("puzzle 1 answer = ", sum(fully_contained)))
print(paste0("puzzle 2 answer = ", sum(overlap)))
