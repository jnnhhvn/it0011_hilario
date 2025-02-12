f= open("Technical Midterm Exam/numbers.txt", "r")
lines = f.readlines()
f.close()

line_num = 1
for line in lines:
    numbers = line.strip().split(',')
    if all(num.isdigit() for num in numbers):
        numbers = [int(num) for num in numbers]
        total_sum = sum(numbers)
        if str(total_sum) == str(total_sum)[::-1]:
            print(f"Line {line_num}: {line.strip()} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {line_num}: {line.strip()} (sum {total_sum}) - Not a palindrome")
    line_num += 1
