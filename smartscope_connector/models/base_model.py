from typing import Dict, Any, Optional, Union
from pydantic import BaseModel, field_validator, model_validator

class SmartscopeBaseModel(BaseModel):

    uid: Optional[Union[int,str]]

    class Meta:
        api_route = 'NotImplemented'
        uid_alias = 'NotImplemented'

        

    @classmethod
    @property
    def api_route(cls):
        assert cls.Meta.api_route != 'NotImplemented', f"Add the metaclass with api route to {cls.__name__} \nclass Meta:\n\tapi_route='route'\n"
        return cls.Meta.api_route
    
    @classmethod
    @property
    def uid_alias(cls):
        assert cls.Meta.uid_alias != 'NotImplemented', f"Add the metaclass with api route to {cls.__name__} \nclass Meta:\n\tapi_route='route'\n"
        return cls.Meta.uid_alias
    
    @model_validator(mode='before')
    @classmethod
    def uid_validator(cls,data:Dict) -> Dict[str,Any]:
        uid= data.pop(cls.Meta.uid_alias, None)
        data['uid'] = uid
        return data
