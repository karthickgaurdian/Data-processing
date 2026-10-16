import re
import pandas as pd
from datetime import datetime

# Load your text content (save your raw input in a file or directly in a variable)
with open('C:\\Users\\karthick\\Desktop\\my files\\notepad docs\\daily tracker.txt', 'r', encoding='utf-8') as file:
    raw_data = file.read()

# Regex to split date-wise blocks
entries = re.split(r"=+\s*(\d{2}-\d{2}-\d{4})\s*-\s*(\w+)", raw_data)
structured = []

for i in range(1, len(entries), 3):
    date_str = entries[i].strip()
    day = entries[i + 1].strip()
    notes = entries[i + 2].strip()

    try:
        date = datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y-%m-%d")
    except ValueError:
        date = date_str

    lines = [line.strip(" -") for line in notes.splitlines() if line.strip()]
    
    keywords = []
    main_notes = []
    sub_notes = []
    detailed_notes = []

    for line in lines:
        lower = line.lower()

        if "trigger" in lower:
            keywords.append("trigger")
        if "load test" in lower:
            keywords.append("load test")
        if "client meeting" in lower:
            keywords.append("client meeting")
        if "tech meeting" in lower:
            keywords.append("tech meeting")
        if "prefill" in lower:
            keywords.append("prefill")

        if re.match(r"^\d+\.", line):  # numbered items
            main_notes.append(line)
        elif line.lower().startswith("internal meeting") or "meeting" in lower:
            main_notes.append(line)
        elif "-" in line or ":" in line:
            sub_notes.append(line)
        else:
            detailed_notes.append(line)

    structured.append({
        "Date": date,
        "Day": day,
        "Keywords": ", ".join(set(keywords)),
        "Main Notes": "; ".join(main_notes),
        "Sub Notes": "; ".join(sub_notes),
        "Detailed Notes": "; ".join(detailed_notes),
    })

# Create and export DataFrame
df = pd.DataFrame(structured)
df.to_excel("Daily_Log_Analysis_Report.xlsx", index=False)

print("✅ Report generated: 'Daily_Log_Analysis_Report.xlsx'")
