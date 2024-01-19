from __future__ import annotations
from .inputs import Inputs

from typing import Union, Optional, List, Tuple, Dict

from streamlit import columns


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


    def basic_render(self, layout: Union[List, Tuple]):
    #The most basic rendering layout is a list of lists of elements. Each element in the list is rendered in its own column.
        try:
            for level in range(len(layout)):
                cols = columns(len(layout[level]))
                for e in range(len(layout[level])):
                    if isinstance(layout[level][e], Inputs):
                        with cols[e]:
                            layout[level][e].render()
        except Exception as e:
            for level in range(len(layout)):
                if isinstance(layout[level], Inputs):
                    layout[level].render()
