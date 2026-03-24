# ENT Statistical Validation Module
validate_snot22_distribution <- function(scores) {
  mean_score <- mean(scores)
  sd_score <- sd(scores)
  list(
    mean = mean_score,
    sd = sd_score,
    is_valid = (mean_score >= 0 && mean_score <= 110)
  )
}
