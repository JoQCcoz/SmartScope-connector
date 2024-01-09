
import numpy as np
from datetime import datetime
from typing import List, Optional, Union
# from Smartscope.core.settings.worker import PLUGINS_FACTORY
from .base_model import SmartscopeBaseModel
from pydantic import Field, field_validator
from Smartscope.core.status import status
from ..Datatypes.querylist import QueryList
from .target_label import Finder, Classifier, Selector


class Target(SmartscopeBaseModel):
    
    number:int
    grid_id:str
    name: Optional[str] = None
    pixel_size: Optional[float] = None
    shape_x: Optional[int] = None
    shape_y: Optional[int] = None
    selected: bool = False
    status:Union[str,None] = None
    
    completion_time: Optional[datetime] = None
    targets: List = Field(default_factory=list)
    finders: List[Finder] = Field(default_factory=list)
    classifiers: List[Classifier] = Field(default_factory=list)
    selectors: List[Selector] = Field(default_factory=list)

    @field_validator('finders','classifiers','selectors', mode='before')
    @classmethod
    def validate_target_labels(cls, v):
        # print(f'Validating target labels, {v}')
        if v is None:
            return []
        return v

    @property
    def group(self):
        return self.grid_id.session_id.group

    @property
    def stage_coords(self) -> np.ndarray:
        finder = self.finders.first()
        return np.array([finder.stage_x, finder.stage_y])
    
    @property
    def coords(self) -> np.ndarray:
        finder = self.finders.first()
        return np.array([finder.x, finder.y])

    # def is_excluded(self):
    #     for selector in self.selectors.all():
    #         plugin = PLUGINS_FACTORY[selector.method_name]
    #         if selector.label in plugin.exclude:
    #             return True, selector.label
    #     return False, ''

    # def is_good(self):
    #     """
    #     Looks at the classification labels and 
    #     return if all the classifiers returned 
    #     the square to be good for selection

    #     Args:
    #         plugins (dict): Dictionnary or sub-section from the loaded pluging.yaml.
    #     Returns:
    #         boolean: Whether the target is good for selection or not.
    #     """
    #     for label in self.classifiers.all():
    #         if PLUGINS_FACTORY[label.method_name].classes[label.label].value < 1:
    #             return False
    #     return True

    def is_out_of_range(self) -> bool:
        return not self.finders.first().is_position_within_stage_limits()
    # def css_color(self, display_type, method):

    #     if method is None:
    #         return 'blue', 'target', ''

    #     # Must use list comprehension instead of a filter query to use the prefetched data
    #     # Reduces the amount of queries subsitantially.
    #     labels = list(getattr(self, display_type).all())
    #     label = [i for i in labels if i.method_name == method]
    #     if len(label) == 0:
    #         return 'blue', 'target', ''
    #     return PLUGINS_FACTORY[method].get_label(label[0].label)


