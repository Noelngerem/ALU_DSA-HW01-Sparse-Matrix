# Sparse Matrix Operations

This project implements a **Sparse Matrix** data structure and supports **addition, subtraction, and multiplication** of sparse matrices. The implementation follows efficient memory usage by storing only non-zero elements.

## How to Run the Program

### Clone the Repository

git clone {your repository url}

### Example Sparse Matrix Input File

Your input files should be formatted as follows:
rows=3

cols=3

(0, 1, 5)

(1, 2, -3)

(2, 0, 7)



### Run the Program
python code/src/main.py


### Follow the On-Screen Prompts
- Enter the path of the first and second matrix files (e.g., `sample_inputs/matrixfile1.txt`).
- Choose an operation: **Addition (+), Subtraction (-), or Multiplication (*)**.
- Enter the output file name (e.g., `result.txt`).
- The computed matrix will be saved to the specified file.

## Example Run

Sparse Matrix Operations

Enter path for first matrix: sample_inputs/matrixfile1.txt

Enter path for second matrix: sample_inputs/matrixfile2.txt

Choose an operation:

1. Addition (+)

2. Subtraction (-)

3. Multiplication (*)

Enter choice (1/2/3): 1

Enter output file name: result_addition.txt

Addition successful!

Result saved to result_addition.txt

