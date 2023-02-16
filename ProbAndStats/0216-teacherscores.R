rm(list = ls())

# Given a set of measurements
scores <- c(26.1,26.0,14.5,29.3,19.7,22.1,21.2,26.6,31.9,25.0,15.9,20.8,20.2,17.8,13.3,25.6,26.5,15.7,22.1,13.8,29.0,21.3,23.5,22.1,10.2)

# mean and standard deviation
meanscores <- mean(scores)
s=sd(scores)

# for k=1,

print(meanscores-s)
print(meanscores+s)

# So, AT LEAST none of the measurements lie within the interval 16.06 to 27.157
# for k=2,

print(meanscores-2*s)
print(meanscores+2*s)

# So, at least 3/4ths (75%) of the measurements lie in the interval 10.51 to 32.706.
# for k=3,

print(meanscores-3*s)
print(meanscores+3*s)

# At least 8/9ths (89%) of the measurements lie in the interval 4.961 to 38.255.