# Define the function below to compute the inverse of a 2 by 2 matrix.
def inverse2(matrix):
    '''
    Matrix takes a 2D list, verifies that it has an inverse, and computes 
    the inverse before returning it as a 2D list.
    @param matrix: 2D list of numeric data
    @return: 2D list of numeric data or alert if not compatible
    '''
    pass    

# Define the function below to compute the inverse of a 3 by 3 matrix
def inverse3(matrix):
    '''
    Matrix takes a 2D list, verifies that it has an inverse and computes 
    the inverse before returning it as a 2D list.
    @param matrix: 2D list of numeric data
    @return: 2D list of numeric data or alert if not compatible
    '''
    pass    

def get_matrix():
    # Get rows and columns from user
    rows = int(input("Enter the number of rows and columns: "))
    columns = rows

    # Create empty list to store matrix values
    matrix = []

    # Iterate over rows and columns to fill matrix
    for r in range(rows):
        # Create empty list to store each row
        row_list = []
        for c in range(columns):
            # Get the value for the matrix position and append it to the row
            value = int(input(f"Enter the value for element {r+1}, {c+1}: "))
            row_list.append(value)
        
        # Append entire row to matrix
        matrix.append(row_list)
    
    # Return matrix
    return matrix

def main():
    '''
    Main function for the program.
    '''
    matrix = get_matrix()
    inverse = []

    # Determine size
    if len(matrix) == 2:
        inverse = inverse2(matrix)
    elif len(matrix) == 3:
        inverse = inverse3(matrix)
    else:
        print("The matrix's inverse cannot be computed.")

    print(inverse)


if __name__ == "__main__":
    main()
