# Plot a pie chart from Example 1.7
# Define the vector of frequencies and ratings
freq<-c(35,260,93,12)
rating<-c("A","B","C","D")
# Plot the piechart
pie(freq,rating,main="US Education Rating")
# Plot the barchart
barplot(freq,names.arg=rating,xlab="Rating",ylab="Frequency")

mmfreq<-c(6,5,3,3,2,2)
mmcolor<-c("Brown","Blue","Green","Orange","Red","Yellow")
barplot(mmfreq,names.arg=mmcolor,xlab="Color",ylab="Frequency")

