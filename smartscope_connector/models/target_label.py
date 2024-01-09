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

    def set_stage_position(self, x=None, y=None, z=None):
        if x is not None:
            self.stage_x = x
        if y is not None:
            self.stage_y = y
        if z is not None:
            self.stage_z = z
 
class Classifier(TargetLabel):
    label: str

class Selector(TargetLabel):
    value: float
    label:Optional[str] = None


