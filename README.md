# Car Rental Application

## Overview

The Car Rental Application is responsible for tracking the start and end of a rental session. It generates events when a rental car is collected by the customer and when the car is returned. Each rental session is limited to 24 hours.

## Record Format

The application generates events in JSON format, with fields including **"type"**, **"id"**, **"timestamp"**, and **"comments"**.

## Sample Output File

The provided sample output file contains example events. Additional events can be added if needed.

## Objective

The task is to develop an application that parses the output file and generates a single summary record for each session. The summary record should include:

- **Session ID**
- **Session start time**
- **Session end time**
- **Session duration** (in hours and minutes)
- Boolean flag indicating if the car was **returned later than expected**
- Boolean flag indicating if the car was **damaged on return**

## Running the Application

### Environment Setup:

- Ensure you have Python installed on your system.

### Executing the Program:

1. Run the Python script **`car-rental.py`** using a Python interpreter.
2. The script will read the input file, process the events, generate summary records, and store them in an output file.

### Input File:

- The input file **`sample-output.json`** contains the events. You can extend this file with additional events.

### Output File:

- The summary records will be stored in **`summary_output.txt`**.

### Cloning the Repository:

To access the summary output file, you can clone this Git repository using the following command:

```bash
git clone https://github.com/anss276/Car-Rental.git
```

### Assumptions:

- It is assumed that the input file will always be in the specified JSON format.
- The application currently handles records with 'START' and 'END' events. Other event types are not considered.

## Questions:

- Should the application account for timezone differences when calculating session durations?
- What should the application do if an event is missing a required field (e.g., 'type', 'id', 'timestamp')?

## Handling Large Inputs:

- The solution efficiently handles large input files by processing records one by one.

## Future Iterations

Possible future improvements include:

- Adding error handling for unexpected input formats.
- Enhancing performance for extremely large input files.
- Implementing a user interface for easier interaction.

## Accessing the GitHub Actions Workflow

To view and run the GitHub Actions workflow for this project, follow these steps:

1. Go to the "Actions" tab at the top of the repository.
2. In the left sidebar, you'll find a list of workflows. Click on "Car Rental Workflow" to access the workflow details.
3. Here, you can view the workflow runs, check their statuses, and explore individual job logs.

Alternatively, you can access the following path to view the workflow for this project: **`.github/workflows/car_rental_workflow.yml`**
