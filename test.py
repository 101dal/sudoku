testarray = [
    [1,5,1,4,4,4,7,7,7],
    [1,1,1,4,4,4,7,7,7],
    [1,1,1,4,4,4,7,7,7],
    [2,2,2,5,5,5,8,8,8],
    [2,2,2,5,5,5,8,8,8],
    [2,2,2,5,5,5,8,8,8],
    [3,3,3,6,6,6,9,9,9],
    [3,3,3,6,6,6,9,9,9],
    [3,3,3,6,6,6,9,9,9]
]

subarrays = []

# Loop through the test array to create subarrays
for i in range(0, len(testarray), 3):  # Increment by 3 to move to the next row of squares
    for j in range(0, len(testarray[i]), 3):  # Increment by 3 to move to the next column of squares
        square = []
        for row in testarray[i:i+3]:  # Select the 3 rows for the square
            square.append(row[j:j+3])  # Select the 3 columns for the square from each row
        square = [element for sublist in square for element in sublist]
        subarrays.append(square)

# Print the subarrays
for subarray in subarrays:
    print(subarray)
