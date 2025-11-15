rain_sum = 0.0
wind_sum = 0.0
count = 0

while True:
    data = input()
    parts = data.split()
    rain = float(parts[0])
    if rain == -1.0:
        break
    wind = float(parts[1])
    rain_sum += rain
    wind_sum += wind
    count += 1

if count > 0:
    avg_rain = rain_sum / count
    avg_wind = wind_sum / count
    severity = (avg_rain * 10) + avg_wind
    print(f"The average rain is {avg_rain:.1f} inches")
    print(f"The average wind is {avg_wind:.1f} mph")
    print(f"The weather severity for these {count} readings is: {severity:.1f}")
