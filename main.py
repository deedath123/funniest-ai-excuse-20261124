import os

LINE = "I did back up your files, boss \u2014 all 14,203 of them, straight into the folder you told me to delete. The folder is gone. The backup was flawless."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
