import json
from datetime import datetime

# Step 1: Read and Parse Input File
with open('sample-output.json', 'r') as file:
    records = json.load(file)

# Define an in-memory database to store summary records
database = {}

# Step 2-4: Process Events and Generate Summary Records
#Processes records one by one to ensure efficiency in handling large inputs
for record in records:
    event_type = record['type']
    session_id = record['id']
    timestamp = int(record['timestamp'])
    comments = record.get('comments', '')

    # Create a new entry in the database if session_id is not already present
    if session_id not in database:
        database[session_id] = {'start_time': None, 'end_time': None, 'comments': ''}

    # Check the event type and update the database accordingly
    if event_type == 'START':
        database[session_id]['start_time'] = timestamp
        database[session_id]['comments'] = comments
    elif event_type == 'END':
        database[session_id]['end_time'] = timestamp
        
        # Only apply comments for END events
        if comments:
            database[session_id]['comments'] = comments

# Step 5: Generate Summary Records
summary_records = []
for session_id, data in database.items():
    start_time = None
    end_time = None

    if data['start_time'] is not None:
        start_time = datetime.fromtimestamp(data['start_time'])

    if data['end_time'] is not None:
        end_time = datetime.fromtimestamp(data['end_time'])

    # Calculate the duration of the rental session in hours and minutes
    if start_time is not None and end_time is not None:
        duration_seconds = (end_time - start_time).total_seconds()
        duration_hours = int(duration_seconds // 3600)
        duration_minutes = int((duration_seconds % 3600) // 60)
        duration = "{} hours {} minutes".format(duration_hours, duration_minutes)
    else:
        duration = None

    # Check if the car was returned later than expected (more than 24 hours)
    car_returned_later = duration is not None and duration_seconds > (24 * 3600)
    
    # Check if the car was damaged on return (applies only to END events)
    car_damaged = bool(data['comments']) and data['end_time'] is not None  

    summary_record = {
        'id': session_id,
        'start_time': start_time,
        'end_time': end_time,
        'duration': duration,
        'car_returned_later': car_returned_later,
        'car_damaged': car_damaged
    }
    summary_records.append(summary_record)

# Step 6: Store Summary Records (In-memory database is already populated)

# Step 7: Write Summary Records to File
with open('summary_output.txt', 'w') as output_file:
    for record in summary_records:
        output_file.write("Session ID: {}\n".format(record['id']))
        output_file.write("Start Time: {}\n".format(record['start_time']))
        output_file.write("End Time: {}\n".format(record['end_time']))
        output_file.write("Duration: {}\n".format(record['duration']))
        output_file.write("Car Returned Later Than Expected: {}\n".format(record['car_returned_later']))
        output_file.write("Car Damaged on Return: {}\n".format(record['car_damaged']))
        output_file.write("\n")
