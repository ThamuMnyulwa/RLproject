# 2 State MC
# Parralel Simulation
# Pseudocode :

alpha = 0.3
beta  = 1 - alpha


n=10
L = 4 #10^5
xsample = matrix(0,nrow=L,ncol=n) # np.zeros((L,n))

   
for (j in 1:L){
  x.vec = 0 # x_{0} initial realization, set to zero
  for (i in 1:n) {
    
  U = runif(1)
  
  if (U <= alpha) x=1
  if (U > alpha)  x=0
  
  x.vec <- c(x.vec,x)

  }
  
  # Place simulations in matrix
  if(j==1) {x.vec1 = x.vec} # for first iteration
  if(j!= 1){x.vec1 <- rbind(x.vec1,x.vec)} # for all other iterations
  
}

x.vec1 <- as.matrix(x.vec1)
print(x.vec1)  # Iterations stored in matrix


# Print lines in parralel simulation
plot( x= c(0-1,n+2) ,
      y= c(min(x.vec1-0.25),max(x.vec1)+0.5) ,
      type='n',
      xlab="i",
      ylab = "X_{i}") # Create the background

for (m in 1:L) {
  lines( y=x.vec1[m,], x=c(0:10)  ,type='l',xlab="i",ylab = "X_{i}", col=m)
  print(m)
}

title(main= paste("Parallel Simulation L = " ,L, "&  n = " ,n))
# fix legend

legend("topright", legend = c('X_{1}','X_{2}','X_{3}','X_{4}'), col = c(1:4),lty = c(1,1,1,1))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
# Ergodic Simulation
#    - Simulate 1 long trajectory 
#    - Time-averaged occupation

# Pseudocode :

n = 100
xsample = vector()

x.zero = 0 # x_{0} initial realization, set to zero
for (i in 0:n) {
  
  U = runif(1)
  
  if (U <= alpha) x=1
  if (U > alpha)  x=0
  
  x <- c(x)


# Place simulations in matrix
if(i==0) {xsample[1] = x.zero} # for first iteration
if(i!= 1){xsample[i] <- c(x) } # for all other iterations

}

print (xsample)

plot(  xsample ,type='l',xlab="i",ylab = "X_{i}") # Create the background
title(main= paste("Ergodic Simulation n = " ,n))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4

# rm(list=objects())
