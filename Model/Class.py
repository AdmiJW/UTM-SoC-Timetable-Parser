from __future__ import annotations
from typing import List

from Model.DayOfWeek import DayOfWeek
from Model.Time import Time



class Class:

    def __init__( self, day: DayOfWeek, time: Time, venue: str ):
        self.day = day
        self.time = time
        self.venue = venue


    def __str__(self):
        return f'{ str(self.day):10} { str(self.time):15} {self.venue}\n'


    # Returns a dictionary that is able to be serialized into JSON
    def get_json_serializable(self, id: int):
        return {
            'id': id,
            'dayOfWeek': self.day.index,
            'beginTime': self.time.start_time,
            'endTime': self.time.end_time,
            'venue': self.venue
        }



    # * Returns a Class instance initialized from the string inside a cell.
    # * Format: "<DayOfWeek> <Time/TimeRange> [Venue]"
    # * Example: "WED 02-04 BK1"
    @staticmethod
    def from_str(row: str) -> Class:
        if row == '': return None

        split = row.split(maxsplit=2)
        day = DayOfWeek.from_short_name( split[0] )
        time = Time.from_code( split[1] )
        venue = split[2] if len(split) > 2 else ''

        return Class(day, time, venue)
        
    

    # * Combines multiple classes that are continuous into a single Class instance
    @staticmethod
    def combine_classes(classes: List[Class]) -> List[Class]:
        res: List[Class] = []

        # Sort by ASCENDING day of week, ASCENDING start time, DESCENDING end time
        sorted_classes = sorted( classes, key=lambda c: (c.day.index, c.time.start_time, -c.time.end_time) )

        # Combine classes that are continuous
        for cls in sorted_classes:
            # Case 1: Not continuous. Append new copy of Class to the result
            if len(res) == 0 or not Class._is_continuous(res[-1], cls):
                res.append( Class(cls.day, cls.time, cls.venue) )
            # Case 2: Continuous. Update the previous class to reflect this new one
            else:
                if res[-1].venue != cls.venue: raise Exception('Continuous class session found, but venue mismatch')
                res[-1].time.end_time = cls.time.end_time

        return res


    # * Helper method
    # * Returns whether clsA can be combined with clsB (clsA.end_time == clsB.start_time, same day)
    # * Assumption: If clsA and clsB are on the same day, then clsA start time is always before clsB start time
    # * Throws exception if clsA and clsB overlap
    @staticmethod
    def _is_continuous(clsA: Class, clsB: Class) -> bool:
        if clsA.day != clsB.day: return False
        if clsB.time.end_time < clsA.time.start_time: raise Exception('Class B start before class A ends: ' + str(clsA) + ' ' + str(clsB))
        return clsA.time.end_time == clsB.time.start_time