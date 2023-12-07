'''
source model with any other model through content_object
'''
from typing import Optional
from pydantic import BaseModel



class TargetLabel(BaseModel):
    # content_type:Optional[str] = None
    # object_id: Optional[str] = None
    method_name:str

class Finder(TargetLabel):
    x: int
    y: int
    stage_x:float
    stage_y:float
    stage_z:float
 
class Classifier(TargetLabel):
    label: str

class Selector(TargetLabel):
    value: float
    label:Optional[str] = None


