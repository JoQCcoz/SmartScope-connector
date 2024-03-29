from typing import get_args, get_origin, List, Dict
import inspect
from ..Datatypes.querylist import QueryList
from ..models.base_model import SmartscopeBaseModel


def parse_single(obj:Dict, output_type:SmartscopeBaseModel) -> SmartscopeBaseModel:
    return output_type.model_validate(obj)

def parse_many(results:List[Dict]|Dict,output_type:SmartscopeBaseModel) -> List[SmartscopeBaseModel]:
    if isinstance(results,dict):
        results = results['results']
    for i,item in enumerate(results):
        results[i] = output_type.model_validate(item)
    return QueryList(results)

def parse_output(func):

    def wrapper_many(output_type:SmartscopeBaseModel,*args,**kwargs) -> List[SmartscopeBaseModel]:
        results = func(output_type=output_type,*args,**kwargs)
        if isinstance(results,dict):
            results = results['results']
        for i,item in enumerate(results):
            results[i] = output_type.model_validate(item)
        return QueryList(results)
        
    def wrapper_single(_,output_type:SmartscopeBaseModel, *args, **kwargs) -> SmartscopeBaseModel:
        output = func(output_type=output_type,*args,**kwargs)
        return output_type.model_validate(output)
    
    signature = inspect.signature(func)
    assert any([signature.return_annotation is SmartscopeBaseModel,
               get_origin(signature.return_annotation) is QueryList and get_args(signature.return_annotation)[0] is SmartscopeBaseModel]), \
               'Function does not have the proper return type, It should be SmartscopeBaseModel or List[SmartscopeBaseModel]'

    if get_origin(signature.return_annotation) is QueryList:
        return wrapper_many
    
    return wrapper_single

def parse_multiple(func):

    def wrapper(output_types:List[SmartscopeBaseModel],*args,**kwargs) -> Dict[str,SmartscopeBaseModel]:
        results = func(output_types=output_types,*args,**kwargs)
        for output_type in output_types:
            if (obj:=results[output_type.__name__.lower()]) is not None:
                results[output_type.__name__.lower()] = output_type.model_validate(obj)
        return results
    
    return wrapper