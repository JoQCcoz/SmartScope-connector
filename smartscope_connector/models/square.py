from typing import List
from pydantic import Field     
from .target import Target
from .hole import HoleModel
from .extra_property_mixin import ExtraPropertyMixin

class SquareModel(Target, ExtraPropertyMixin):

    area:float
    atlas_id: str
    targets: List[HoleModel] = Field(default_factory=list)

    class Meta(Target.Meta):
        api_route = 'squares'
        uid_alias = 'square_id'

    # aliases

    # @property
    # def alias_name(self):
    #     return f'Area {self.number}'

    # @property
    # def api_viewset_name(self):
    #     return 'squares'

    # @property
    # def prefix(self):
    #     return 'Square'

    # @property
    # def targets_prefix(self):
    #     return 'hole'

    # @property
    # def id(self):
    #     return self.square_id

    # @property
    # def parent(self):
    #     return self.atlas_id

    # @parent.setter
    # def set_parent(self, parent):
    #     self.atlas_id = parent
    # # endaliases

    # @property
    # def parent_stage_z(self):
    #     return self.parent.stage_z

    # @property
    # def targets(self):
    #     return self.holemodel_set.all()


    # # @cached_model_property(key_prefix='svg', 
    # # extra_suffix_from_function=['method'], timeout=3600)
    # def svg(self, display_type, method):
    #     from .hole import HoleModel
    #     from Smartscope.core.svg_plots import drawSquare

    #     holes = list(HoleModel.display.filter(square_id=self.square_id))
    #     sq = drawSquare(self, holes, display_type, method)
        
    #     return sq

    # @property
    # def has_queued(self):
    #      return self.holemodel_set(manager='just_holes').\
    #         filter(status='queued').exists()

    # @property
    # def has_completed(self):
    #     return self.holemodel_set(manager='just_holes').\
    #         filter(status='completed').exists()

    # @property
    # def has_active(self):
    #     return self.holemodel_set(manager='just_holes').\
    #         filter(status__in=['acquired', 'processed', 'targets_picked', 'started']).\
    #         exists()


    # @property
    # def initial_quality(self):
    #     try:
    #         from .change_log import ChangeLog
    #         return ChangeLog.objects\
    #             .get(grid_id=self.grid_id, line_id=self.hole_id, column_name='quality')\
    #             .initial_value
    #     except:
    #         return self.quality

    # @property
    # def extracted_file(self):
    #     logger.debug('Getting extracted file')

    # class Meta(BaseModel.Meta):
    #     # TODO
    #     # unique_together = ('name', 'atlas_id')
    #     db_table = 'squaremodel'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if not self.square_id:
    #         self.name = f'{self.grid_id.name}_square{self.number}'
    #         self.square_id = generate_unique_id(extra_inputs=[self.name[:20]])
    #     self.raw = os.path.join('raw', f'{self.name}.mrc')

    # def save(self, *args, **kwargs):

    #     super().save(*args, **kwargs)
    #     return self

    # def __str__(self):
    #     return self.name
