import pytest
from Smartscope.core.models.base_model import SmartscopeBaseModel

from ..decorators import parse_output


def test_parse_output():
    class MockModel(SmartscopeBaseModel):
        x:int
    
    @parse_output
    def mock_get_API(url, output_type:MockModel) -> SmartscopeBaseModel:
        return dict(x=1)
    
   
    assert isinstance(mock_get_API(url='bla',output_type=MockModel), MockModel)

    with pytest.raises(AssertionError, match='proper return type'):
        @parse_output
        def wrong_mock_get_API(url, output_type:MockModel)-> None:
            return dict(x=1)

# def test_decorator():

#     def function(x=1):
#         return x*x

#     def test_decorator(func, init=1):
#         def wrapper(*args,**kwargs):
#             kwargs['x'] += init
#             return func(*args,**kwargs)
#         return wrapper
        
#     result = test_decorator(func=function, init=4)(x=1)
#     assert result == 25