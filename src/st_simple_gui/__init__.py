from __future__ import annotations

from typing import  Dict, List, Optional, Tuple, Union

from streamlit import columns, session_state

from .inputs import Inputs

from contextlib import contextmanager

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
        self._layoutvars = {}


        if isinstance(self._layout, list):
            if isinstance(self._layout[0], list):
                if isinstance(self._layout[0][0], Inputs):
                    self.basic_render(self._layout)
            elif isinstance(self._layout[0], Inputs):
                self.basic_render(self._layout)




    def _resolve_key(self, key: str,level: int)->str:
        return f"{level}-{key}"


    def basic_render(self, layout: Union[List, Tuple]):
    #The most basic rendering layout is a list of lists of elements. Each element in the list is rendered in its own column.
        try:
            for level in range(len(layout)):
                cols = columns(len(layout[level]))
                for e in range(len(layout[level])):
                    if isinstance(layout[level][e], Inputs):
                        with cols[e]:
                            x = layout[level][e]._resolve_key(level, e)
                            self._layoutkeys[x] = x
                            layout[level][e].render()

        except Exception as e:
            for level in range(len(layout)):
                if isinstance(layout[level], Inputs):
                    layout[level].render()

    def sync_session_state(self):
        ns = {}
        for k in self._layoutkeys:
            ns[k] = session_state.get(k)

        self._layoutvars = ns

    @contextmanager
    def __call__(self):
        if self._layoutvars == {}:
            self.sync_session_state()
        yield self._layoutvars
