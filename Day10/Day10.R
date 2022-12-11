library(stringr)

connection <- file(description = "Day10Input.txt", open = "r")
program <- readLines(connection)
close(connection)

get_pixel <- function(cycle, pixel_position, sprite_position) {
  if (pixel_position %in% sprite_position) { return("#") }
  else { return(".") }
}

cycle <- 1
signal_strengths <- c()
sprite_position <- 0:2
pixel_position <- 0
pixels <- c()
for (instruction in program) {
  instruction <- str_split(instruction, " ")[[1]]
  if (instruction[1] == "noop") { 
    pixels <- c(pixels, get_pixel(cycle, pixel_position, sprite_position))
    cycle <- cycle + 1
    pixel_position <- pixel_position + 1
  }
  if (instruction[1] == "addx") {
    pixels <- c(pixels, get_pixel(cycle, pixel_position, sprite_position))
    cycle <- cycle + 1
    pixel_position <- pixel_position + 1
    if (cycle %% 40 == 20) { signal_strengths <- c(signal_strengths, cycle * sprite_position[2]) }
    if (cycle %% 40 == 1) { pixel_position <- 0 }
    pixels <- c(pixels, get_pixel(cycle, pixel_position, sprite_position))
    sprite_position <- sprite_position + as.numeric(instruction[2])
    cycle <- cycle + 1
    pixel_position <- pixel_position + 1
  }
  if (cycle %% 40 == 20) { signal_strengths <- c(signal_strengths, cycle * sprite_position[2]) }
  if (cycle %% 40 == 1) { pixel_position <- 0 }
}

# puzzle answers
print(paste0("puzzle 1 answer = ", sum(signal_strengths)))
print("puzzle 2 answer:")
for (i in seq(from = 40, to = 240, by = 40)) { print(paste0(pixels[(i-39):i], collapse = "")) }
