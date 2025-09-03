import os, shutil

path = "C:/Users/swaru"
d = os.path.join(path, "Downloads")

categories = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".exe", ".msi"],
    "Sheets": [".xlsx", ".csv"]
}

for i in os.listdir(d):
    file_path = os.path.join(d, i)

    # Skip directories
    if not os.path.isfile(file_path):
        continue

    ext = os.path.splitext(i)[1].lower()
    moved = False

    for category, extensions in categories.items():
        if ext in extensions:
            tfolder = os.path.join(d, category)
            os.makedirs(tfolder, exist_ok=True)
            shutil.move(file_path, os.path.join(tfolder, i))
            print(f"Moved {i} to {category}")
            moved = True
            break

    if not moved:  # only if no category matched
        tfolder1 = os.path.join(d, "Others")
        os.makedirs(tfolder1, exist_ok=True)
        shutil.move(file_path, os.path.join(tfolder1, i))
        print(f"Moved {i} to Others")
