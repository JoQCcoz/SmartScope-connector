from .base_model import SmartscopeBaseModel

class HoleType(SmartscopeBaseModel):
    name: str
    hole_size: float
    hole_spacing: float

    class Meta(SmartscopeBaseModel.Meta):
        api_route = 'holetypes'
        uid_alias = 'holetype_id'


    @property
    def pitch(self):
        return self.hole_size + self.hole_spacing