from datetime import datetime
from typing import Optional, List
from pydantic import Field, field_validator

from Smartscope.lib.Datatypes.models import generate_unique_id
from Smartscope.core.status import status

from .base_model import SmartscopeBaseModel
from .square import SquareModel
from .extra_property_mixin import ExtraPropertyMixin





# from Smartscope.core.svg_plots import drawAtlas

class AtlasModel(SmartscopeBaseModel, ExtraPropertyMixin):
    name:str
    grid_id: str
    uid:Optional[str]
    pixel_size: Optional[float] = None
    binning_factor: Optional[float] = None
    shape_x: Optional[int] = None
    shape_y: Optional[int] = None
    stage_z: Optional[float] = None
    status: Optional[str] = None
    completion_time: Optional[datetime] = None
    targets: List[SquareModel] = Field(default_factory=list)

    class Meta(SmartscopeBaseModel.Meta):
        api_route = 'atlas'
        uid_alias = 'atlas_id'

    # aliases

    # @property
    # def group(self):
    #     return self.grid_id.session_id.group

    # @ property
    # def alias_name(self):
    #     return 'Atlas'

    # @property
    # def prefix(self):
    #     return 'Atlas'

    # @ property
    # def api_viewset_name(self):
    #     return 'atlas'

    # @ property
    # def targets_prefix(self):
    #     return 'square'

    # @ property
    # def id(self):
    #     return self.atlas_id

    # @ property
    # def parent(self):
    #     return self.grid_id

    # @ parent.setter
    # def set_parent(self, parent):
    #     self.grid_id = parent

    # @ property
    # def targets(self):
    #     # return self.squaremodel_set.all()

    # @cached_model_property(key_prefix='svg', extra_suffix_from_function=['method'], timeout=3600)
    # def svg(self, display_type, method):
    #     from .square import SquareModel
        
    #     targets = list(SquareModel.display.filter(atlas_id=self.atlas_id))
    #     return drawAtlas(self,targets , display_type, method)

    # class Meta(BaseModel.Meta):
    #     unique_together = ('grid_id', 'name')
    #     db_table = 'atlasmodel'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if not self.atlas_id:
    #         self.name = f'{self.grid_id.name}_atlas'
    #         self.atlas_id = generate_unique_id(extra_inputs=[self.name[:20]])
    #     self.raw = os.path.join('raw', f'{self.name}.mrc')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     return self

    # def __str__(self):
    #     return self.name
