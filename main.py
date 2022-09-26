from concurrent.futures import process
import csv
import json
from typing import Dict
from Model.Course import Course
from Model.Section import Section

from util import *
from CONFIG import *



# * Logic to process a row from excel file,
# * which represents a section (or a range of sections) for a course
def process_row(i: int, row: List[str], result: Dict[str, Course]):
    if not is_valid_row( row ): return
    remove_newlines( row )

    if VERBOSE:
        print(f'Entry {i}: {row}')

    for course_code in get_course_codes( row[ CODE_COL_INDEX ] ):
        if course_code not in result:
            result[ course_code ] = Course( course_code, row[ COURSE_NAME_COL_INDEX ] )

        course = result[ course_code ]

        for section in Section.from_row( row ):
            if section.section in course.sections:
                raise Exception( f"Duplicate section {section.section} for course {course_code} ({course.course_name})" )
            course.sections[ section.section ] = section




# **********************
# * Main program
# **********************

result: Dict[str, Course] = dict()

# Parse
with open( CSV_FILE_PATH ) as csvfile:
    reader = csv.reader( csvfile, delimiter=CSV_DELIMITER )
    errors: List[str] = []

    for i, row in enumerate(reader):
        try:
            process_row( i, row, result )
        except Exception as e:
            errors.append( f'Entry {i+1}: {str(e)}' )
    
    if len(errors) > 0:
        print( '\n' + '\n'.join(errors) + "\n" )
        raise Exception( f"Found {len(errors)} errors. Please fix them before proceeding" )

    print("Parsing complete")


# Write a readable output for verification purpose
with open( OUTPUT_READABLE_FILE_PATH, 'a') as f:
    for course in result.values():
        f.write( str(course) + '\n')

    print("Wrote readable file to", OUTPUT_READABLE_FILE_PATH)


# Write a JSON output
with open( OUTPUT_JSON_FILE_PATH, 'w') as f:
    res = json.dumps({
        i: course.get_json_serializable(i) for i, course in enumerate( result.values() )
    }, indent=4)
    f.write(res)
    print("Wrote JSON file to", OUTPUT_JSON_FILE_PATH)