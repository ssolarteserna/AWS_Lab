import json
import random
from datetime import datetime, timedelta
import os

# Constants
NUM_FILES = 5  # Number of JSON files to generate
MEASUREMENTS_PER_FILE = 10 #Number of measurements per file
SENSOR_IDS = ["THS-001", "THS-002", "THS-003", "THS-004", "THS-005"]

# Predefined locations for each sensor_id (fixed)
sensor_locations = {
    sensor_id: {
        "latitude": round(random.uniform(-90.0, 90.0), 6),
        "longitude": round(random.uniform(-180.0, 180.0), 6)
    } for sensor_id in SENSOR_IDS
}

def generate_random_timestamp(start_time, used_timestamps):
    """Generate a unique timestamp that hasn't been used before."""
    while True:
        random_minutes = random.randint(0, 10000)
        timestamp = (start_time + timedelta(minutes=random_minutes)).isoformat() + "Z"
        if timestamp not in used_timestamps:
            used_timestamps.add(timestamp)
            return timestamp

def generate_measurement(sensor_id, used_timestamps):
    """Generate one random measurement for a given sensor."""
    measurement = {
        "sensor_id": sensor_id,
        "timestamp": generate_random_timestamp(datetime.utcnow(), used_timestamps),
        "temperature": round(random.uniform(0, 40), 1),
        "humidity": round(random.uniform(50, 80), 1),
        "location": sensor_locations[sensor_id],
        "battery_level": random.randint(1, 100)
    }
    return measurement

def generate_json_file(file_index):
    """Generate a JSON file with random measurements."""
    used_timestamps = set()  # Track timestamps to avoid duplicates
    measurements = []
    
    for _ in range(MEASUREMENTS_PER_FILE):
        sensor_id = random.choice(SENSOR_IDS)
        measurement = generate_measurement(sensor_id, used_timestamps)
        measurements.append(measurement)
    
    data = {"measurements": measurements}

    # Write JSON to file
    filename = f"measurements_{file_index + 1}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Generated {filename}")

def main():
    # Create output folder if needed
    output_dir = "json_measurements"
    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)
    
    for i in range(NUM_FILES):
        generate_json_file(i)

if __name__ == "__main__":
    main()
