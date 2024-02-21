'''
source model with any other model through content_object
'''
from typing import Optional
from pydantic import BaseModel
from .base_model import SmartscopeBaseModel



class TargetLabel(BaseModel):
    method_name:str

class DetailedTargetLabel(SmartscopeBaseModel, TargetLabel):
    # content_type:Optional[str] = None
    object_id: Optional[str] = None

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

class DetailedClassifier(DetailedTargetLabel, Classifier):

    class Meta(SmartscopeBaseModel.Meta):
        api_route='classes'


class Selector(TargetLabel):
    value: Optional[float] = None
    label:Optional[str] = None


