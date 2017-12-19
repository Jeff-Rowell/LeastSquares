# LeastSquares
This is a linear regression example that uses input data (time spent studying for an exam) 
and output data (exam scores) to extrapolate what exam scores will be based on how much 
time the students spend studying. Here we only set up a linear model, but the leastSquares
function can be used for quadratic models, cubic models, etc. 
Note: The use of a Vondermonde matrix can be very unstable for large sets of data becuase
      the condition number will be very high, Vondermonde matrix is being used here because
      the data set is rather small and the condition number is not too high.
