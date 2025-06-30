import os

print("Current Working Directory:", os.getcwd())
print("Files in Current Directory:")
for file in os.listdir():
    print("-", file)

file_to_check = "input_image.jpg"
print("\nDoes input_image.jpg exist?")
print("Result:", os.path.exists(file_to_check))
