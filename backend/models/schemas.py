from pydantic import BaseModel
from typing import List

class MasteryRequest(BaseModel):
    student_id: str
    concept_id: str
    is_correct: bool
    response_time: float
