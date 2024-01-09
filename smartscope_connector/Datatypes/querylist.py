from typing import Optional, Any, List,Dict, Iterable
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

class QueryList(list):
    #List of Pydantic models

    def first(self) -> Optional[Any]:
        if len(self) > 0:
            return self[0]
        
    def dump_all(self, exclude_unset=True, exclude_none=False) -> List[Dict]:
        return [obj.model_dump(exclude_unset=exclude_unset, exclude_none=exclude_none) for obj in self]
    
    def dump_uids(self) -> List[str]:
        uids = [obj.uid for obj in self]
        logger.debug(f'Dumping {len(self)} uids: {uids}')
        return uids
    
    def set_fields(self, **fields) -> None:
        for obj in self:
            for field, value in fields.items():
                setattr(obj, field, value)