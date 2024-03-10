# Geometric Shape Area Calculator
Overview:
This Python script calculates the areas of trapezoids, rectangles, and squares using sequential, multithreaded, and multiprocess approaches. It provides classes for each geometric shape, offering insights into the impact of parallel execution on performance.

## Usage:
- Ensure Python (3.6+) is installed.
- Clone the repository: git clone <repository-url>
# Classes:
- Trapezoid: Represents a trapezoid.
- Rectangle: Represents a rectangle (inherits from Trapezoid).
- Square: Represents a square (inherits from Rectangle).

# Functions:
- regular(arr): Sequentially computes shape areas.
- threads(params): Uses multithreading for parallel execution.
 -multiprocess(arr): Uses multiprocessing with internal threading.

# Sample Performance:

```python
in general Finished in: 0.23s
with pools Finished in: 0.58s
with threads Finished in: 0.24s
```
# Customization:
- Adjust the number and parameters of shapes in the code.
- Experiment with execution methods for performance insights.

## Contributing

Feel free to contribute, report issues, or provide feedback. Happy coding!
