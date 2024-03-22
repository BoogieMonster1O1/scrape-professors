from dataclasses import dataclass
from dataclasses import asdict
from typing import List
import json

@dataclass
class FacultyProfile:
    department: str
    name: str
    designation: str
    teaching_exp: int
    research_exp: int
    industry_exp: int
    date_of_joining: str
    email: str
    link: str

def read_json() -> List[FacultyProfile]:
    try:
        with open('./faculty_profiles.json', 'r') as file:
            data = json.load(file)
            return [FacultyProfile(**item) for item in data]
    except FileNotFoundError:
        print('Faculty profiles file not found')
        return []

def write_json(data: List[FacultyProfile]) -> None:
    with open('./faculty_profiles.json', 'w') as file:
        json.dump([asdict(obj) for obj in data], file, indent=2)

def write_org_mode(data: List[FacultyProfile]) -> None:
    department_dict = {}
    for profile in data:
        if profile.department not in department_dict:
            department_dict[profile.department] = []
        department_dict[profile.department].append(profile.name)
    
    org_output = f"* H-index\n"
    for department, faculty_list in department_dict.items():
        org_output += f"- {department}\n"
        for faculty in faculty_list:
            org_output += f"  - [ ] {faculty}\n"
    
    with open("faculty.org", 'w') as file:
        file.write(org_output)


def write_csv(data: List[FacultyProfile]) -> None:
    with open('./faculty_profiles.csv', 'w') as file:
        file.write("Department,Name,RVCE Link\n")
        for profile in data:
            file.write(f"{profile.department},{profile.name},{profile.link}\n")
