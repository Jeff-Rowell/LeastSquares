import numpy as np
import matplotlib.pyplot as plt
'''
leastSquares Function: Solves the least squares fit problem. Sets up
                       a Vondermonde matrix, A, where the first column
                       is all ones, and any succesive column will contain
                       the values from the 'x' array raised to the 'n - 1'
                       power. For example, the second column of A will contain
                       'x' values, the third column will contain 'x**2' values
                       and so on. B is a vector containing the values from the
                       'y' array. N is the degree of our fit. 'c' will be a 2-d
                       array (or matrix) containing our constant values for our
                       fit. In this example it will only contain the slope and
                       y-intercept since it is a linear model
                       
Input:   x -   An array of our predictor variables.
         y -   An arrray of our outcome variables.
         N -   The degree of our fit.
'''
def leastSquares(x, y, N):
	n = len(x)
	A = np.matrix(np.ones((n, N+1)))
	B = np.matrix(y)
	B = B.T

	for i in range(1, N+1):
		A[0:n, i] = np.multiply(A[0:n, i-1], np.matrix(x).T)

	c = np.linalg.solve((A.T*A), (A.T*B))
	return np.array(c)

#The following arrays 'x' and 'y' will be used for plotting our data points.
x = [11, 12, 13, 13, 15, 15, 16, 15, 17]
y = [76, 77, 80, 83, 76, 84, 85, 88, 85]

#The following arrays 'x1' and 'y1' will be used for our linear regression model
x1 = [11, 12, 13, 13, 15, 15, 16, 15, 17, 20, 21, 22]
y1 = [76, 77, 80, 83, 76, 84, 85, 88, 85, 90, 93, 98]

b,m = leastSquares(x1,y1,1)     #b is the y-intercept, m is the slope (linear model)
bestFit = b + m*x1              #Note: this is our model, it will change if we need a non-linear model
fig, ax = plt.subplots()
ax.set_title('Study Time vs. Exam Scores')
ax.set_xlabel('Study Time')
ax.set_ylabel('Exam Scores')
ax.set_ylim(70, 100)

ax.plot(x,y,'x',x1, bestFit)
plt.show()
