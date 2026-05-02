# log_reader.py

import os

def read_all_logs(folder_path):
    logs = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith((".txt", ".csv")):
            full_path = os.path.join(folder_path, file_name)

            with open(full_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

                logs.append({
                    "file_name": file_name,
                    "lines": lines
                })

    return logs