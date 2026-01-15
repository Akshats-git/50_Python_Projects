import csv
import matplotlib.pyplot as plt
from collections import defaultdict

FILENAME = "weather_logs.csv"

def plot_weather_data():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:   
                dates.append(row['Date'])
                temps.append(float(row['Temperature']))
                conditions[row['Condition']] += 1
            except ValueError:
                continue
    
    if not dates:
        print("No valid data to plot.")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_weather_data()