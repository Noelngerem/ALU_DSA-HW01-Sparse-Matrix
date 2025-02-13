from sparse_matrix import SparseMatrix
from utils import validate_input_file, save_matrix_to_file

def main():
    print("Sparse Matrix Operations")

    file1 = input("Enter path for first matrix: ").strip()
    file2 = input("Enter path for second matrix: ").strip()

    validate_input_file(file1)
    validate_input_file(file2)

    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")

    choice = input("Enter choice (1/2/3): ").strip()

    result = None
    output_file = input("Enter output file name (e.g., result.txt): ").strip()

    try:
        if choice == "1":
            result = matrix1 + matrix2
            print("Addition successful!")
        elif choice == "2":
            result = matrix1 - matrix2
            print("Subtraction successful!")
        elif choice == "3":
            result = matrix1 * matrix2
            print("Multiplication successful!")
        else:
            print("Invalid choice. Exiting.")
            return

        save_matrix_to_file(result, output_file)
        print(f"Result saved to {output_file}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
