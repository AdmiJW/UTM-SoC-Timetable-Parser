
from typing import List, Sequence
from CONFIG import *
import re


# *  A section can be either a single section (01, 02...)
# *  or a range of sections (01-03, 05-07...)
# *
# *  Returns None if invalid section
# *  Otherwise returns a Sequence of int that iterates over sections
def get_section(section: str) -> Sequence[int]:
    if section.isdigit(): return [ int(section) ]
    if re.search('^\d{2}-\d{2}$', section) is None: return None
    start, end = map(int, section.split('-'))
    return range(start, end + 1)




# * As long as the course code contains AAAA0000 where A is uppercase letter and 0 is digit, then it is valid
# * and will be extracted
def get_course_codes(code: str) -> Sequence[str]:
    res = re.findall('[A-Z]{4}\d{4}', code)
    if len(res) == 0: return None
    return res





# *  Checks used:
# *      1. All 4 columns [No, Code, Course Name, Section] cannot be empty
# *      2. 'No' column must be a number
# *      3. 'Code' column must be a valid course code
# *      4. 'Section' column must be a valid section
def is_valid_row( row: List[str] ) -> bool:
    if '' in ( row[NO_COL_INDEX], row[CODE_COL_INDEX], row[COURSE_NAME_COL_INDEX], row[SECTION_COL_INDEX] ): return False
    if not row[NO_COL_INDEX].isdigit(): return False
    if get_course_codes( row[CODE_COL_INDEX] ) is None: return False
    if get_section( row[SECTION_COL_INDEX] ) is None: return False
    return True



# * Remove unnecessary \n characters
# * In some rows, the whitespace character is important, and will be replaced with a space
# * Otherwise the space character will be removed entirely
def remove_newlines(row : List[str]):
    row[ NO_COL_INDEX ] = row[ NO_COL_INDEX ].replace('\n', '')
    row[ CODE_COL_INDEX ] = row[ CODE_COL_INDEX ].replace('\n', '')
    row[ COURSE_NAME_COL_INDEX ] = row[ COURSE_NAME_COL_INDEX ].replace('\n', ' ')
    row[ SECTION_COL_INDEX ] = row[ SECTION_COL_INDEX ].replace('\n', '')
    row[ PROGRAM_COL_INDEX ] = row[ PROGRAM_COL_INDEX ].replace('\n', '')
    row[ CAPACITY_COL_INDEX ] = row[ CAPACITY_COL_INDEX ].replace('\n', '')
    row[ LECTURER_COL_INDEX ] = row[ LECTURER_COL_INDEX ].replace('\n', '')
    for i in range(TIME_START_COL_INDEX, TIME_END_COL_INDEX + 1):
        row[i] = row[i].replace('\n', ' ')