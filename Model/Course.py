
from typing import Dict

from Model.Section import Section


class Course:

    def __init__(
        self,
        course_code: str,
        course_name: str
    ):
        self.course_name = course_name
        self.course_code = course_code
        self.sections: Dict[int, Section] = dict()



    def __str__(self):
        res = f'{self.course_code}: {self.course_name}\n'
        for section in self.sections.values():
            res += "\t" + str(section).replace('\t', '\t\t') + '\n'
        return res

    
    def get_json_serializable(self, id: int):
        return {
            'id': id,
            'name': self.course_name,
            'code': self.course_code,
            'sections': {
                i: section.get_json_serializable(i) for i, section in enumerate( self.sections.values() )
            }
        }