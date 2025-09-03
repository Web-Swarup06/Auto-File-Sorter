# Auto-File-Sorter
A Python automation script that scans the Downloads folder, detects files based on their extensions (e.g., .png, .mp4, .pdf), and automatically moves them into categorized subfolders

⚙️ Features:
1.Detects file extensions automatically
2.Sorts into predefined categories (Images, Documents, Videos, Archives, Installers, Sheets, Others)
3.Creates category folders if they don’t exist
4.Safe to run multiple times (doesn’t break existing folders)
5.Can be scheduled with Windows Task Scheduler to run automatically

🖥️ Requirements:
Python 3.x installed
Modules:
os (built-in)
shutil (built-in)
