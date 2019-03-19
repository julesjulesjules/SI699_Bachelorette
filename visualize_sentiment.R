library(ggplot2)
library(reshape2)
library(tidyr)
library(dplyr)

setwd("C:/Users/julie/Documents/SI699/SI699_Bachelorette")
senti <- read.csv("ette14_twitterfeatures.csv")

# melt variables into long form
senti_long <- melt(senti)

#split variable column
senti_long <- separate(data = senti_long, col = variable, into = c("week", "sentiment"), sep = "\\.")

to_chart <- filter(senti_long, sentiment == "Positive")
to_chart$win <- ifelse(to_chart$Name == "Garrett", "1", "0")

ggplot(data=to_chart, aes(x=week, y=value, group=Name)) +
geom_line(aes(color=win), size=1.2) +
geom_point(aes(color=win)) + 
theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
scale_x_discrete(limits=c("X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11")) +
ggtitle("Positive") +
ylim(0, 600)


senti$x2.PosPercent <- senti$X2.Positive / senti$X2.Total
senti$x2.NegPercent <- senti$X2.Negative / senti$X2.Total
senti$x2.NeuPercent <- senti$X2.Neutral / senti$X2.Total

senti$x3.PosPercent <- senti$X3.Positive / senti$X3.Total
senti$x3.NegPercent <- senti$X3.Negative / senti$X3.Total
senti$x3.NeuPercent <- senti$X3.Neutral / senti$X3.Total

senti$x4.PosPercent <- senti$X4.Positive / senti$X4.Total
senti$x4.NegPercent <- senti$X4.Negative / senti$X4.Total
senti$x4.NeuPercent <- senti$X4.Neutral / senti$X4.Total

senti$x5.PosPercent <- senti$X5.Positive / senti$X5.Total
senti$x5.NegPercent <- senti$X5.Negative / senti$X5.Total
senti$x5.NeuPercent <- senti$X5.Neutral / senti$X5.Total

senti$x6.PosPercent <- senti$X6.Positive / senti$X6.Total
senti$x6.NegPercent <- senti$X6.Negative / senti$X6.Total
senti$x6.NeuPercent <- senti$X6.Neutral / senti$X6.Total

senti$x7.PosPercent <- senti$X7.Positive / senti$X7.Total
senti$x7.NegPercent <- senti$X7.Negative / senti$X7.Total
senti$x7.NeuPercent <- senti$X7.Neutral / senti$X7.Total

senti$x8.PosPercent <- senti$X8.Positive / senti$X8.Total
senti$x8.NegPercent <- senti$X8.Negative / senti$X8.Total
senti$x8.NeuPercent <- senti$X8.Neutral / senti$X8.Total

senti$x9.PosPercent <- senti$X9.Positive / senti$X9.Total
senti$x9.NegPercent <- senti$X9.Negative / senti$X9.Total
senti$x9.NeuPercent <- senti$X9.Neutral / senti$X9.Total

senti$x10.PosPercent <- senti$X10.Positive / senti$X10.Total
senti$x10.NegPercent <- senti$X10.Negative / senti$X10.Total
senti$x10.NeuPercent <- senti$X10.Neutral / senti$X10.Total

senti$x11.PosPercent <- senti$X11.Positive / senti$X11.Total
senti$x11.NegPercent <- senti$X11.Negative / senti$X11.Total
senti$x11.NeuPercent <- senti$X11.Neutral / senti$X11.Total


# melt variables into long form
senti_long <- melt(senti)

#split variable column
senti_long <- separate(data = senti_long, col = variable, into = c("week", "sentiment"), sep = "\\.")

to_chart <- filter(senti_long, sentiment == "NeuPercent")
to_chart$win <- ifelse(to_chart$Name == "Garrett", "1", "0")

ggplot(data=to_chart, aes(x=week, y=value, group=Name)) +
  geom_line(aes(color=win), size=1.2) +
  geom_point(aes(color=win)) + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  scale_x_discrete(limits=c("x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11")) +
  ggtitle("Neutral Percentage") 

