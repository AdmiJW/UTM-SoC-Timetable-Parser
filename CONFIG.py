
# ! Configuration file
# ! Modify the value to your needs

# Print index and row for each parsed row. 
# Useful when you want to know which row in the error output.
VERBOSE = False

CSV_FILE_PATH = 'timetable.csv'
CSV_DELIMITER = ','

# Index mapping for the CSV file
NO_COL_INDEX = 0
CODE_COL_INDEX = 1
COURSE_NAME_COL_INDEX = 2
SECTION_COL_INDEX = 3
PROGRAM_COL_INDEX = 4
CAPACITY_COL_INDEX = 5
# Inclusive
TIME_START_COL_INDEX = 6
TIME_END_COL_INDEX = 9
LECTURER_COL_INDEX = 10


# Outputs a readable file of compiled schedule
OUTPUT_READABLE_FILE_PATH = 'output.txt'
OUTPUT_JSON_FILE_PATH = 'schedule.json'