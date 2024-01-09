from typing import Optional
from pathlib import Path
from pydantic import Field
# from django.utils import timezone
from datetime import datetime
from .base_model import SmartscopeBaseModel

class AutoloaderGrid(SmartscopeBaseModel):

    position: int
    name: str
    session_id: str
    holetype_id:str
    meshSize:str
    meshMaterial:str
    hole_angle:Optional[float]
    mesh_angle:Optional[float]
    quality:Optional[str]
    notes:Optional[str]
    status: Optional[str]
    start_time: Optional[datetime]
    last_update: Optional[datetime]
    params_id: Optional[str]

    class Meta(SmartscopeBaseModel.Meta):
        api_route = 'grids'
        uid_alias = 'grid_id'

    # @property
    # def atlas(self):
    #     query = self.atlasmodel_set.all()
    #     return query

    # @property
    # def squares(self):
    #     return self.squaremodel_set.all()

    # @property
    # def count_acquired_squares(self):
    #     return self.squaremodel_set.filter(status='completed').count()

    # @property
    # def holes(self):
    #     return self.holemodel_set.all()

    # @property
    # def count_acquired_holes(self):
    #     return self.holemodel_set.filter(status='completed').count()

    # @property
    # def high_mag(self):
    #     return self.highmagmodel_set.all()

    # @property
    # def end_time(self):
    #     try:
    #         hole = self.highmagmodel_set.order_by('-completion_time').first()

    #         if hole is None:
    #             raise
    #         logger.debug(f'End time: {self.grid_id}, hole:{hole.hole_id}, {hole.completion_time}')
    #         return hole.completion_time
    #     except:
    #         return self.last_update

    # @property
    # def time_spent(self):
    #     timeSpent = self.end_time - self.start_time
    #     logger.debug(f'Time spent: {self.grid_id}, {timeSpent}')
    #     return timeSpent

    
    # @property
    # def protocol(self):
    #     return Path(self.directory , 'protocol.yaml')


    @property
    def directory(self):
        return f'{self.position}_{self.name}'
    #     wd = self.parent.directory
    #     return os.path.join(wd, self_wd)

    # class Meta(BaseModel.Meta):
    #     unique_together = ('position', 'name', 'session_id')
    #     db_table = "autoloadergrid"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if not self.grid_id and self.position is not None and self.name is not None:
    #         self.grid_id = generate_unique_id(extra_inputs=[str(self.position), self.name])

    # def save(self, export=False, *args, **kwargs):
    #     if self.status != 'complete':
    #         self.last_update = timezone.now()
    #     super().save(*args, **kwargs)
    #     if export:
    #         self.session_id.export()
    #     return self

    # def __str__(self):
    #     return f'{self.position}_{self.name}'
