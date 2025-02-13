import os

def validate_input_file(file_path):
    """This function is going to ensure that the file exists and follows the correct sparse matrix format."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if len(lines) < 2 or not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
        raise ValueError("Error: Input file format is incorrect.")

def save_matrix_to_file(matrix, file_path):
    """This function will save a SparseMatrix object to a file."""
    matrix.save_to_file(file_path)
