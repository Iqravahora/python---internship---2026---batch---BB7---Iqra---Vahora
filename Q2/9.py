# marks = [80, 75, 90, 65, 70]
marks = [80, 75, 90, 65, 70]

total = 0
for mark in marks:
    total += mark
    
percentage = total / 500 * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"
    
print("total:", total)
print("percentage:", percentage)
print("Result:", result)

