#perfor matrix addition and subtraction using nested lists 
def matrix_operations(mat1, mat2, operation='add'):
    rows = len(mat1)
    cols = len(mat1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if operation == 'add':
                result[i][j] = mat1[i][j] + mat2[i][j]
            elif operation == 'subtract':
                result[i][j] = mat1[i][j] - mat2[i][j]
            else:
                raise ValueError("Operation must be 'add' or 'subtract'")
    
    return result
# --- IGNORE ---
if __name__ == "__main__":
    user_input1 = input("Enter the first matrix rows separated by semicolons and elements by spaces (e.g., '1 2 3;4 5 6'): ")
    user_input2 = input("Enter the second matrix rows separated by semicolons and elements by spaces (e.g., '7 8 9;10 11 12'): ")
    operation = input("Enter operation (add/subtract): ").strip().lower()
    
    mat1 = [list(map(int, row.split())) for row in user_input1.split(';')]
    mat2 = [list(map(int, row.split())) for row in user_input2.split(';')]
    
    result_matrix = matrix_operations(mat1, mat2, operation)
    print(f"Resultant Matrix after {operation}:")
    for row in result_matrix:
        print(' '.join(map(str, row)))
        