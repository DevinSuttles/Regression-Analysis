# Regression-Analysis
A program for generating random data and finding the lines of best fit using linear or quadratic regression.
## Examples
![Linear Regression Example](docs/linRegExample.PNG)
## How does it work?
### Linear Regression
For a line of the form &nbsp; ![Linear Line Equation](docs/linearLine.gif) &nbsp; the sum of the squared residuals is 

![SE formula](docs/SE_Latex.gif) 

which we want to minimize. But first, we expand the sum to 

![Simplified Sum](docs/SE2_Latex.gif) 

which simplifies to 

![Further Simplified Sum](docs/SE3_Latex.gif)

Of the right expression, all terms are constant except &nbsp; ![a0](docs/a0.gif) &nbsp; and &nbsp; ![a0](docs/a1.gif), so the minimum of the function can be found by setting the partial derivatives with respect to both those terms to zero and solving the system of equations. Doing this gives

![a1](docs/linA1.gif)
![a0](docs/linA0.gif)

Both of which can finally be used to plot the line.

### Quadratic Regression

## Room for improvement
- The types of regression lines can easily be expanded, incorporating power or logarithmic lines for example.
- It might be possible to generalize all polynomial regression lines using gradient descent to find the minimum sum of squared residuals instead of calculating the coefficients for each one out by hand.
