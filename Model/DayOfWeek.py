from enum import Enum


class DayOfWeek:

    class _DayOfWeek:
        def __init__(self, full_name: str, short_name: str, index: int):
            self.full_name = full_name
            self.short_name = short_name
            self.index = index

        def __str__(self) -> str:
            return self.full_name



    # Enums
    SUNDAY = _DayOfWeek("Sunday", "SUN", 0)
    MONDAY = _DayOfWeek("Monday", "MON", 1)
    TUESDAY = _DayOfWeek("Tuesday", "TUE", 2)
    WEDNESDAY = _DayOfWeek("Wednesday", "WED", 3)
    THURSDAY = _DayOfWeek("Thursday", "THU", 4)
    FRIDAY = _DayOfWeek("Friday", "FRI", 5)
    SATURDAY = _DayOfWeek("Saturday", "SAT", 6)


    # Map from short name to enum
    @classmethod
    def from_short_name(cls, short_name: str):
        short_name = short_name.upper()
        if short_name == 'SUN': return cls.SUNDAY
        elif short_name == 'MON': return cls.MONDAY
        elif short_name == 'TUE': return cls.TUESDAY
        elif short_name == 'WED': return cls.WEDNESDAY
        elif short_name == 'THU': return cls.THURSDAY
        elif short_name == 'FRI': return cls.FRIDAY
        elif short_name == 'SAT': return cls.SATURDAY
        else: raise Exception(f'Invalid short name for Day of Week: {short_name}')



