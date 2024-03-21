from dataclasses import dataclass
from dataclasses import asdict
from typing import List
import json

@dataclass
class DepartmentFacultyLink:
    name: str
    faculty_link: str

def read_json() -> List[DepartmentFacultyLink]:
    try:
        with open('./faculty_links.json', 'r') as file:
            data = json.load(file)
            return [DepartmentFacultyLink(**item) for item in data]
    except FileNotFoundError:
        print('Department faculty links file not found')
        return []

def write_json(data: List[DepartmentFacultyLink]) -> None:
    with open('./faculty_links.json', 'w') as file:
        json.dump([asdict(obj) for obj in data], file, indent=4)
