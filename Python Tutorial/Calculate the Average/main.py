def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average) 
