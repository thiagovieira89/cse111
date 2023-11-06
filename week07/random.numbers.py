import random


def main():
    
    numbers  = [16.2,75.1,52.3]
    print(numbers)
    append_random_numbers(numbers)
    print()
    print(numbers)
    print()
    append_random_numbers(numbers, quantity=3)
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        new_number = random.uniform(0,100)
        new_number = round(new_number,1)
        numbers_list.append(new_number)


if __name__=='__main__':
    main()


