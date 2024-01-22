from __future__ import annotations

from typing import  Dict, List, Optional, Tuple, Union

from streamlit import columns, session_state

from .inputs import Input

# trunk-ignore(ruff/F401)
from .writers import Writer

from contextlib import contextmanager




__version__ = "0.0.1"




# types
# str, int, float, bool, Type, Tuple, List, Dict, Set
# You can use a tuple of types to indicate that the value can be one of several types.
#
#
#
#
#All layouts are based on a base list then it can contain any
#-------------------------------------------------------
# layout = [
#     [
#        Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}}),
#      Inputs({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}}),
#      ... any other element of streamlit including custom elements
#    ],
#     [
#       Inputs({'float': {'label': 'uno', 'value': 1.0, 'kwargs': {'key': 'floatval'}}}),
#      Inputs({'bool': {'label': 'uno', 'value': True, 'kwargs': {'key': 'boolval'}}}),
#      ... any other element of streamlit including custom elements
#    ],
#     [
#       Inputs({'date': {'label': 'uno', 'value': 'today', 'kwargs': {'key': 'dateval'}}}),
#      Inputs({'time': {'label': 'uno', 'value': 'now', 'kwargs': {'key': 'timeval'}}})
#      ],
#        ... Buttons, Selectbox,and any other element of streamlit including custom elements
#    ] #Layout type 1 - list of lists of elements*you can use any iterable of iterables of elements
#-------------------------------------------------------
# layout = [
#    Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}}),# Includes any Input type see Inputs class for more info
#    Inputs({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}}),
#    ... any other element of streamlit including custom elements
#    ] #Layout type 2 - list of elements*you can use any iterable of elements
#-------------------------------------------------------
# layout = {
#     'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}},
#    'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}},
#   ... any other element of streamlit including custom elements
#   } #Layout type 3 - dict of elements
#
# layout = {
#       {
#        'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}},
#       'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}
#       },
#       {
#       'float': {'label': 'uno', 'value': 1.0, 'kwargs': {'key': 'floatval'}},
#       'bool': {'label': 'uno', 'value': True, 'kwargs': {'key': 'boolval'}}
#       },
#      ... any other element of streamlit including custom elements
#    } #Layout type 4 - dict of dicts of elements

class SimpleUI:

    def __init__(self, layout: Union[List, Tuple, Dict],layouconfig: Optional[Union[List, Tuple, Dict]] = None, **kwargs):
        self._layout = layout
        self._layoutkeys = {}
        self.kwargs = kwargs
        self._layoutvars = {}


        if isinstance(self._layout, list):
            if isinstance(self._layout[0], list):
                if isinstance(self._layout[0][0], Input):
                    self.basic_render(self._layout)
            elif isinstance(self._layout[0], Input):
                self.basic_render(self._layout)





    def basic_render(self, layout: Union[List, Tuple]):
    #The most basic rendering layout is a list of lists of elements. Each element in the list is rendered in its own column.
        try:
            for level in range(len(layout)):
                cols = columns(len(layout[level]))
                for e in range(len(layout[level])):
                    if isinstance(layout[level][e], Input):
                        with cols[e]:
                            x = layout[level][e]._resolve_key(level, e)
                            self._layoutkeys[x] = x
                            layout[level][e].render()

        except Exception as e:
            for level in range(len(layout)):
                if isinstance(layout[level], Input):
                    x = layout[level]._resolve_key(level)
                    self._layoutkeys[x] = x
                    layout[level].render()

    def sync_session_state(self):
        """
        Synchronizes the session state with the layout variables.
        This method updates the layout variables with the values stored in the session state.
        It iterates over the layout keys and retrieves the corresponding values from the session state.
        The updated layout variables are then stored in the `_layoutvars` attribute.
        Returns:
            None
        """
        ns = {}
        for k in self._layoutkeys:
            ns[k] = session_state.get(k)
        self._layoutvars = ns


    @contextmanager
    def __call__(self):
        """
        Context manager that synchronizes the session state and yields the layout variables.
        If the layout variables are empty, it synchronizes the session state before yielding.
        """
        if self._layoutvars == {}:
            self.sync_session_state()

        yield self._layoutvars

    def __getitem__(self, item: str):
        """
        Returns the layout variable corresponding to the given key.
        Args:
            item: key of the layout variable to return.
        Returns:
            The layout variable corresponding to the given key.
        """
        if self._layoutvars == {}:
            self.sync_session_state()

            if item in self._layoutvars or any([item in v.split('-') for v in self._layoutvars.keys()]):
                return self._layoutvars[item]
            else:
                raise KeyError(f"Layout variable {item} does not exist.")
