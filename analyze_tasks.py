# import pandas as pd
# from collections import Counter

# # Load Excel
# df = pd.read_excel("Daily_Log_Analysis_Report.xlsx")

# # Clean and normalize
# df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
# df['Day'] = df['Day'].str.capitalize().str.strip()
# df['Task Title'] = df['Task Title'].fillna('')
# df['Details'] = df['Details'].fillna('')

# # 1. Basic stats
# total_days = df['Date'].nunique()
# total_tasks = len(df)
# tasks_with_number = df['Task Number'].notna().sum()
# avg_tasks_per_day = total_tasks / total_days

# # 2. Task frequency by weekday
# tasks_by_day = df['Day'].value_counts().sort_index()

# # 3. Most common keywords in titles & details
# all_text = ' '.join(df['Task Title'].tolist() + df['Details'].tolist()).lower()
# keywords = [word for word in all_text.split() if len(word) > 3]
# common_words = Counter(keywords).most_common(10)

# # 4. Days with most and fewest tasks
# task_counts = df.groupby(df['Date'].dt.strftime('%Y-%m-%d')).size()
# most_tasks_date = task_counts.idxmax(), task_counts.max()
# fewest_tasks_date = task_counts.idxmin(), task_counts.min()

# # Print report
# print("📝 === Yearly Task Summary Report ===")
# print(f"📅 Total days logged        : {total_days}")
# print(f"📌 Total tasks              : {total_tasks}")
# print(f"🔢 Tasks with numbers       : {tasks_with_number}")
# print(f"📈 Avg tasks per day        : {avg_tasks_per_day:.2f}")
# print(f"\n🗓️  Tasks by Weekday:")
# for day, count in tasks_by_day.items():
#     print(f"   {day:<10}: {count}")

# print("\n🔍 Top 10 common keywords:")
# for word, count in common_words:
#     print(f"   {word:<15}: {count}")

# print(f"\n📆 Most tasks on   : {most_tasks_date[0]} ({most_tasks_date[1]} tasks)")
# print(f"📆 Fewest tasks on : {fewest_tasks_date[0]} ({fewest_tasks_date[1]} tasks)")


# 📝 === Yearly Task Summary Report ===
# 📅 Total days logged        : 147
# 📌 Total tasks              : 809
# 🔢 Tasks with numbers       : 705
# 📈 Avg tasks per day        : 5.50

# 🗓️  Tasks by Weekday:
#    Firday    : 1
#    Friday    : 116
#    Fun       : 6
#    Monday    : 133
#    Saturday  : 25
#    Thursday  : 149
#    Tuesday   : 230
#    Tursday   : 3
#    Wednesday : 146

# 🔍 Top 10 common keywords:
#    meeting        : 187
#    from           : 101
#    order          : 100
#    font           : 96
#    live           : 96
#    issue          : 92
#    data           : 81
#    done           : 79
#    code           : 78
#    bulk           : 74

# 📆 Most tasks on   : 2024-02-18 (33 tasks)
# 📆 Fewest tasks on : 2024-02-08 (1 tasks)





import pandas as pd
from collections import Counter

# Load Excel (from the previous structured output)
df = pd.read_excel("Daily_Log_Analysis_Report.xlsx")

# Clean and normalize
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Day'] = df['Day'].str.capitalize().str.strip()

# Fill missing columns
for col in ['Main Notes', 'Sub Notes', 'Detailed Notes', 'Keywords']:
    if col in df.columns:
        df[col] = df[col].fillna('')
    else:
        df[col] = ''

# 1. Basic stats
total_days = df['Date'].nunique()
total_entries = len(df)
avg_tasks_per_day = total_entries / total_days if total_days > 0 else 0

# 2. Task frequency by weekday
tasks_by_day = df['Day'].value_counts().sort_index()

# 3. Most common keywords in all notes
all_text = ' '.join(df['Main Notes'].tolist() +
                    df['Sub Notes'].tolist() +
                    df['Detailed Notes'].tolist()).lower()

keywords = [word.strip('.,:;!?()[]{}') for word in all_text.split() if len(word) > 3]
common_words = Counter(keywords).most_common(10)

# 4. Days with most and fewest entries
task_counts = df.groupby(df['Date'].dt.strftime('%Y-%m-%d')).size()
most_tasks_date = task_counts.idxmax(), task_counts.max()
fewest_tasks_date = task_counts.idxmin(), task_counts.min()

# Print report
print("📝 === Yearly Daily Log Summary Report ===")
print(f"📅 Total unique days        : {total_days}")
print(f"📌 Total log entries        : {total_entries}")
print(f"📈 Avg entries per day      : {avg_tasks_per_day:.2f}")

print("\n🗓️  Entries by Weekday:")
for day, count in tasks_by_day.items():
    print(f"   {day:<10}: {count}")

print("\n🔍 Top 10 common keywords (from all notes):")
for word, count in common_words:
    print(f"   {word:<15}: {count}")

print(f"\n📆 Most entries on   : {most_tasks_date[0]} ({most_tasks_date[1]} entries)")
print(f"📆 Fewest entries on : {fewest_tasks_date[0]} ({fewest_tasks_date[1]} entries)")
