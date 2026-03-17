size = int(input("Enter size: "))
arr = [int(input()) for _ in range(size)]
target = int(input("Enter search element: "))

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Found at index {i}")
        found = True
        break
if not found:
    print("Not found")
    