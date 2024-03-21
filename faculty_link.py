from dataclasses import dataclass
from dataclasses import asdict
from typing import List
import json

@dataclass
class FacultyLink:
    department: str
    link: str

def read_json() -> List[FacultyLink]:
    try:
        with open('./faculty_links.json', 'r') as file:
            data = json.load(file)
            return [FacultyLink(**item) for item in data]
    except FileNotFoundError:
        print('Faculty links file not found')
        return []

def write_json(data: List[FacultyLink]) -> None:
    with open('./faculty_links.json', 'w') as file:
        json.dump([asdict(obj) for obj in data], file, indent=2)
