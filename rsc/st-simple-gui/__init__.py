from __future__ import annotations


from typing import Union, Optional, List, Tuple, Dict



__version__ = "0.0.1"




# types
# str, int, float, bool, Type, Tuple, List, Dict, Set
# You can use a tuple of types to indicate that the value can be one of several types.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#









class SimpleGui:
    def __init__(self, layout: Union[List, Tuple, Dict],layouconfig: Optional[Union[List, Tuple, Dict]] = None, **kwargs):
        self._layout = layout
        self._layoutkeys = {}

        self.kwargs = kwargs



    def _resolve_key(self, key: str,level: int )->str:
        return f"{level}-{key}"

