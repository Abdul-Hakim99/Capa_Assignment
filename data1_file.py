# Function to calculate average value of a specific column
def calculate_average(csv_file, column_name):
    total = 0
    count = 0
    
    try:
        # Open the CSV file and read lines
        with open(csv_file, 'r') as file:
            lines = file.readlines()
            # Extract column headers and find the index of the specified column
            headers = lines[0].strip().split(',')
            column_index = headers.index(column_name)
            
            # Iterate through rows and calculate the total and count for the specified column
            for line in lines[1:]:
                values = line.strip().split(',')
                if len(values) > column_index:
                    total += float(values[column_index])
                    count += 1
                else:
                    return f"Error: Column '{column_name}' not found in the CSV file."
            
            # Calculate the average value if there are valid rows
            if count > 0:
                average_value = total / count
                return f"The average value of '{column_name}' column is: {average_value}"
            else:
                return "Error: No valid data to calculate the average."
    except FileNotFoundError:
        return "Error: File not found."

# File name and column name to calculate the average
csv_file = '/home/abdud/Documents/data.csv'  # Replace this with the actual file name or path
column_name = "Score"  # Replace this with the actual column header name

# Call the function and store the result in a variable
results = calculate_average(csv_file, column_name)

# Print the result
print(results)

