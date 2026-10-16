import re
import pandas as pd

# Step 1: Load data from a file
with open("C:\\Users\\karthick\\Desktop\\my files\\notepad docs\\daily tracker.txt", "r", encoding="utf-8") as file:

    raw_data = file.read()

# Step 2: Extract date sections
date_sections = re.split(r'={10,}', raw_data)
output_rows = []

for section in date_sections:
    date_match = re.search(r'(\d{2}-\d{2}-\d{4})\s*-\s*(\w+)', section)
    if not date_match:
        continue

    date = date_match.group(1).strip()
    day = date_match.group(2).strip()
    content = section.split("\n", 2)[-1].strip()

    # Split by numbered task headers like "1. task name"
    matches = list(re.finditer(r'\n*(\d+\.)\s+(.*)', content))
    if not matches:
        # If no numbered task, treat each line as separate task
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        for line in lines:
            output_rows.append([date, day, '', line, ''])
    else:
        for i, match in enumerate(matches):
            task_num = match.group(1).strip('.')
            task_title = match.group(2).strip()
            start = match.end()
            end = matches[i+1].start() if i+1 < len(matches) else len(content)
            task_block = content[start:end].strip()

            # Clean and format sub-tasks
            lines = [line.strip('-• ') for line in task_block.splitlines() if line.strip()]
            details = '\n'.join(f'- {line}' for line in lines if line)
            output_rows.append([date, day, task_num, task_title, details])

# Step 3: Save to Excel
df = pd.DataFrame(output_rows, columns=["Date", "Day", "Task Number", "Task Title", "Details"])
df.to_excel("Yearly_Tasks_Summary.xlsx", index=False)

print("✅ Excel file 'Yearly_Tasks_Summary.xlsx' created successfully.")
