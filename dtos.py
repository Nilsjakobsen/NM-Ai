from pydantic import BaseModel
from typing import Dict, Optional, List


class RaceCarPredictRequestDto(BaseModel):
    did_crash: bool
    elapsed_time_ms: int
    distance: int
    velocity: Dict[str, int]  
    coordinates: Dict[str, int] # add
    sensors: Dict[str, Optional[int]]  

class RaceCarPredictResponseDto(BaseModel):
    """Response model returned from the prediction endpoint."""

    actions: List[str]
    """
    The actions the game should perform.

    Valid actions are:
    - ``ACCELERATE``
    - ``DECELERATE``
    - ``STEER_LEFT``
    - ``STEER_RIGHT``
    - ``NOTHING``
    """
