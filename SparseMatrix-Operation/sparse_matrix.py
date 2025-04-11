class SparseMatrix:
    def __init__(self, file_path=None, rows=None, cols=None):
        """This function will initialize sparse matrix from a file or create an empty one."""
        self.data = {}
        if file_path:
            self.load_from_file(file_path)
        else:
            self.rows = rows
            self.cols = cols

    def load_from_file(self, file_path):
        """This function is going to load sparse matrix from a file while handling errors."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            self.rows = int(lines[0].strip().split('=')[1])
            self.cols = int(lines[1].strip().split('=')[1])

            for line in lines[2:]:
                line = line.strip()
                if line and line.startswith('(') and line.endswith(')'):
                    row, col, val = line[1:-1].split(',')
                    row, col, val = int(row), int(col), int(val)
                    self.data[(row, col)] = val
                else:
                    raise ValueError(f"Invalid line in input file: {line}")

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{file_path}' not found.")
        except ValueError:
            raise ValueError(f"Error: Input file '{file_path}' has the wrong format.")

    def getElement(self, row, col):
        """In this line, the code will return the value at (row, col), defaulting to 0."""
        return self.data.get((row, col), 0)

    def setElement(self, row, col, value):
        """This will set the value at (row, col), storing only if non-zero."""
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def __add__(self, other):
        """ This function will perform a matrix addition."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Error: Matrices must have the same dimensions for addition.")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.data = self.data.copy()

        for (row, col), value in other.data.items():
            result.setElement(row, col, result.getElement(row, col) + value)

        return result

    def __sub__(self, other):
        """This function will perform a matrix subtraction."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Error: Matrices must have the same dimensions for subtraction.")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.data = self.data.copy()

        for (row, col), value in other.data.items():
            result.setElement(row, col, result.getElement(row, col) - value)

        return result

    def __mul__(self, other):
        """This function is going to perform a matrix multiplication."""
        if self.cols != other.rows:
            raise ValueError("Error: Cannot multiply matrices. Dimensions do not match.")

        result = SparseMatrix(rows=self.rows, cols=other.cols)

        for (r, c), val in self.data.items():
            for k in range(other.cols):
                if (c, k) in other.data:
                    new_value = result.getElement(r, k) + val * other.getElement(c, k)
                    result.setElement(r, k, new_value)

        return result

    def save_to_file(self, file_path):
        """This function will save the sparse matrix to a file."""
        with open(file_path, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for (row, col), val in sorted(self.data.items()):
                file.write(f"({row}, {col}, {val})\n")
