#Create a function that returns sum, average, max, and min of a list.
def calculate_stats(numbers):
    if not numbers:
        return None, None, None, None
    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total_sum, average, maximum, minimum
# Example usage:
numbers = [10, 20, 30, 40, 50]
sum_result, avg_result, max_result, min_result = calculate_stats(numbers)
print(f"Sum: {sum_result}, Average: {avg_result}, Max: {max_result}, Min: {min_result}")

