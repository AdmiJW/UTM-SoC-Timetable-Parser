from __future__ import annotations
import re

# Represents a time for a class (UTM Format)
# Since UTM likes to represent hours in 02, 03...
class Time:

    CODES = {
        1: (7, 8),
        2: (8, 9),
        3: (9, 10),
        4: (10, 11),
        5: (11, 12),
        6: (12, 13),
        7: (13, 14),
        8: (14, 15),
        9: (15, 16),
        10: (16, 17),
        11: (17, 18),
        12: (18, 19),
        13: (19, 20),
        14: (20, 21),
    }

    
    def __init__(self, start_time: int, end_time: int):
        self.start_time = start_time
        self.end_time = end_time


    def __str__(self):
        return f'{self.start_time}:00-{self.end_time}:00'

    


    # Map from code to enum
    # The code can be in format "02", "03", "04"
    # or a range, like "02-04", provided it is not space separated
    @staticmethod
    def from_code(code: str)-> Time:
        # Single time code
        if code.isdigit():
            code = int(code)
            if code not in Time.CODES: raise Exception(f'Invalid code for Time: {code}')
            return Time( *Time.CODES[code] )

        if re.search("^\d{2}-\d{2}$", code) is None: 
            raise Exception(f'Invalid code for Time: {code}')

        # Time range
        start, end = map(int, code.split('-') )

        if start not in Time.CODES or end not in Time.CODES: 
            raise Exception(f'Invalid code for Time: {code}')
            
        return Time( Time.CODES[start][0], Time.CODES[end][1] )

    


