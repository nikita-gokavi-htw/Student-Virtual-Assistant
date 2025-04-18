from typing import Dict, Any, Set
from datetime import date
import uuid

class Course:
    def __init__(self, name: str, max_capacity: int, course_type: str,
                 difficulty_level: str = None, materials_required: Set[str] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.max_capacity = max_capacity
        self.course_type = course_type
        self.difficulty_level = difficulty_level
        self.materials_required = materials_required or set()
        self.students = set()  # Set of student IDs
        self.teacher_id = None
        self.attendance = {}  # Dictionary mapping dates to sets of present student IDs
        self.grades = {}  # Dictionary mapping student IDs to their grades
        self.validate()

    def validate(self):
        """Validate course data"""
        # TODO: Implement the validate method
        # 1. Validate that name is a non-empty string
        # 2. Validate that max_capacity is a positive integer
        # 3. Validate that course_type is either 'math' or 'art'
        # 4. For math courses:
        #    - Validate that difficulty_level is one of: 'beginner', 'intermediate', 'advanced'
        # 5. For art courses:
        #    - Validate that materials_required is a set
        #    - Validate that all materials are strings
        pass

    def take_attendance(self, date: date, present_student_ids: Set[str]):
        """Record attendance for a specific date"""
        # TODO: Implement the take_attendance method
        # 1. Validate that present_student_ids is a set
        # 2. Validate that all IDs in present_student_ids are strings
        # 3. Check that number of present students doesn't exceed enrolled students
        # 4. Verify all present students are enrolled in the course
        # 5. Record the attendance for the given date
        pass

    def assign_grade(self, student_id: str, grade: float):
        """Assign a grade to a student"""
        # TODO: Implement the assign_grade method
        # 1. Check if student is enrolled in the course
        # 2. Validate that grade is a number
        # 3. Validate that grade is between 0 and 100
        # 4. Assign the grade to the student
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Convert course data to dictionary"""
        # TODO: Implement the to_dict method
        # 1. Create a dictionary with the course's basic information:
        #    - id, name, course_type, max_capacity, current enrollment, teacher_id
        # 2. For math courses: include difficulty_level
        # 3. For art courses: include materials_required as a list
        # 4. Return the dictionary
        pass