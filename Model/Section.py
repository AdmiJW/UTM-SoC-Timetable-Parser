from __future__ import annotations
from re import S
from typing import List

from util import *
from CONFIG import *
from Model.Class import Class


# Model for a Section in a Course
#
# program: Which program is this section for? SECR? SECJ? SECV?
# capacity: Maximum capacity for the section
# lecturer: Lecturer that teaches this section
# classes: List of classes. See Class.py
class Section:

    def __init__(
        self,
        section: int,
        program: str,
        capacity: int,
        lecturer: str,
    ):
        self.section = section
        self.program = program
        self.capacity = capacity
        self.lecturer = lecturer
        self.classes: List[Class] = []


    def __str__(self) -> str:
        res = f'Section {self.section} ({self.lecturer}) ({self.capacity} students) ({self.program})\n'
        for cls in self.classes:
            res += '\t' + str(cls)
        return res


    # Returns a dictionary that is able to be serialized into JSON
    def get_json_serializable(self, id: int):
        return {
            'id': id,
            'section': self.section,
            'program': self.program,
            'lecturer': self.lecturer,
            'capacity': self.capacity,
            'times': {
                i: cls.get_json_serializable(i) for i, cls in enumerate( self.classes )
            }
        }

    

    # * Parses a row from the csv file to return a list of Sections
    # * Recall: Some rows may represent multiple sections: Like section '01-46' represent sections 1, 2, 3, ..., 46
    @staticmethod
    def from_row(row: List[str])-> List[Section]:
        res = []

        sections = get_section( row[ SECTION_COL_INDEX ] )
        program = row[ PROGRAM_COL_INDEX ]
        capacity = int( row[ CAPACITY_COL_INDEX ] ) if row[ CAPACITY_COL_INDEX ] != '' else 0
        lecturer = row[ LECTURER_COL_INDEX ]

        for section in sections:
            s = Section(section, program, capacity, lecturer)
            # Parse time columns and add to classes
            for time in row[ TIME_START_COL_INDEX : TIME_END_COL_INDEX + 1 ]:
                cls = Class.from_str(time)
                if cls is not None: s.classes.append(cls)
            # Combine classes
            s.classes = Class.combine_classes(s.classes)

            res.append(s)

        return res
