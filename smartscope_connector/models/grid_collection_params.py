from .base_model import SmartscopeBaseModel
from pydantic import Field

class GridCollectionParams(SmartscopeBaseModel):
    uid:str = Field(alias='params_id')
    atlas_x:int = 3
    atlas_y:int = 3
    square_x:int = 1
    square_y:int = 1
    squares_num:int = 3
    holes_per_square:int = 3  # If -1 means all
    bis_max_distance:int = 3  # 0 means not BIS
    min_bis_group_size: int = 1
    afis: bool = False
    target_defocus_min:float = -2.0
    target_defocus_max:float = -2.0
    step_defocus:float = 0.0  # 0 deactivates step defocus
    drift_crit:float = -1.0
    tilt_angle:float = 0.0
    save_frames:bool = True
    force_process_from_average:bool = False
    offset_targeting:bool = True
    offset_distance:float = -1.0
    zeroloss_delay:int = -1
    hardwaredark_delay:int = -1
    coldfegflash_delay:int = -1
    multishot_per_hole:bool = False

    class Meta(SmartscopeBaseModel.Meta):
        api_route = 'gridcollectionparams'