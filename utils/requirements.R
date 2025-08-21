# Liste de paquets requis (base + données)
req <- c(
  "tidyverse",
  "broom",
  "janitor",
  "GGally",
  "performance",
  "car",
  "yardstick",
  "pROC",
  "AmesHousing",
  "titanic",
  "kableExtra",
  "patchwork",
  "ISLR",
  "scales"
)

inst <- req[!(req %in% installed.packages()[, "Package"])]
if (length(inst) > 0) install.packages(inst, dependencies = TRUE)

# Chargement silencieux
invisible(lapply(req, require, character.only = TRUE))
