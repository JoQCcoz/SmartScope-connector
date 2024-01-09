from pathlib import Path
from pydantic import Field
# from ..settings import worker
from .base_model import SmartscopeBaseModel

class Microscope(SmartscopeBaseModel):
    name: str
    location: str
    voltage:int
    spherical_abberation: float
    cold_FEG: bool = False
    aperture_control: bool = False
    vendor: str = 'TFS'
    loader_size: int = 12
    worker_hostname: str = 'localhost'
    executable: str = 'smartscope.py'
    # SerialEM connection
    serialem_IP: str
    serialem_PORT: int = 48888
    windows_path: str = 'X:\\\\auto_screening\\'
    scope_path:str = '/mnt/scope'

    class Meta:
        api_route = 'microscopes'
        uid_alias = 'microscope_id'


    @property
    def lock_file(self) -> Path:
        return f'{self.uid}.lock'

    # @property
    # def isLocked(self):
    #     if self.lockFile.exists():
    #         return True
    #     return False

    # @property
    # def isPaused(self):
    #     return Path(settings.TEMPDIR, f'paused_{self.microscope_id}').exists()
