import datetime

entry = input("What did you learn today? ").strip()
rating = input("Rate your productivity (1-5):").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

journal_entry = f"\n{date_str}\n{entry}"

if rating:
    journal_entry += f"\nProductivity Rating: {rating}\n"

journal_entry += "-" * 40 + "\n"

with open("learning_journal.txt", "a") as f:
    f.write(journal_entry)
    print("Entry has been successfully logged.")