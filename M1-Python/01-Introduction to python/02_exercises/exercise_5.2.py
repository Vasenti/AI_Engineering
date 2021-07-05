# Your functions
def largest_number(collection):
    return max(collection)

def smaller_number(collection):
    return min(collection)

def dividable_by(number, collection):
    divisable_numbers = []
    for i in range(len(collection)):
        if collection[i] % number == 0:
            divisable_numbers.append(collection[i])
    return len(divisable_numbers)
    
def main():
    a = [2, 4, 6, 12, 15, 99, 100]
    
    print("Largest number: ", str(largest_number(a)))
    print("Smaller number: ", str(smaller_number(a)))
    print("Divisable numbers: ", str(dividable_by(3, a)))

main()