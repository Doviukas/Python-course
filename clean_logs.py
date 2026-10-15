import csv

input_file = 'environmental_raw.txt'
output_file = 'environmental_clean.csv'

corrupted_count = 0
valid_rows = []

print("Starting log cleaning process...")

with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    
    # Read header if present, or process line by line depending on your format
    for row in reader:
        # Basic validation: ensure row has the expected number of columns and isn't empty
        if not row:
            continue
        try:
            # Example check: ensure fields can be parsed correctly
            # Adjust based on your specific homework requirements if needed
            valid_rows.append(row)
        except Exception as e:
            corrupted_count += 1

# Write the cleaned data to the output CSV
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(valid_rows)

print(f"Cleaning complete! Skipped {corrupted_count} corrupted lines.")
print(f"Output saved to {output_file}")
def celsius_converter(f_temp):
    try:
        celsius = (float(f_temp) - 32) * 5.0 / 9.0
        return round(celsius, 2)
    except (ValueError, TypeError):
        return None

def parse_and_clean(line):
    if not line.strip():
        return None
    
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 5:
        return None
        
    timestamp, station_id, temp_f, humidity, sensor_status = parts
    
    if temp_f in ["ERROR", "N/A"] or sensor_status != "ACTIVE":
        return None
        
    temp_c = celsius_converter(temp_f)
    if temp_c is None:
        return None
        
    return f"{timestamp}, {station_id}, {temp_c}, {humidity}, {sensor_status}\n"

input_file = "environmental_raw.txt"
output_file = "environmental_clean.csv"

corrupted_count = 0

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    outfile.write("Timestamp,StationID,Temp(C),Humidity(%),Sensor_Status\n")
    for line in infile:
        cleaned_line = parse_and_clean(line)
        if cleaned_line:
            outfile.write(cleaned_line)
        else:
            corrupted_count += 1

print(f"Cleaning complete. Skipped corrupted lines: {corrupted_count}")