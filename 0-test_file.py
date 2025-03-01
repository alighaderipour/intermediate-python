import os

files = ["document.txt", "image.png", "report.pdf"]

for i, file in enumerate(files, start=1):
    new_name = f"file_{i}_{file}"
    print(f"Renaming {file} to {new_name}")
    # os.rename(file, new_name)  # Uncomment this when working with real files