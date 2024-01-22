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
#    } #Layout type 4 - set of dicts of elements
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

class SimpleUI:

    __INPUT_TYPES__ = [
    'str',
    'string',
    'char',
    'character',
    'text_input',
    'number',
    'int',
    'integer',
    'numeric',
    'num',
    'number',
    'number_input',
    'float',
    'double',
    'real',
    'date',
    'time',
    'datetime',
    'selectbox',
    'multiselect',
    'checkbox',
    'bool',
    'boolean',
    'radio',
    'file_uploader',
    'color_picker',
    'text_area',
    'file',
    'color',
    'password',
    'text',
    'textarea',
    'camera_input'
    ]


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

        for level in range(len(layout)):
            if isinstance(layout[level], Input):
                x = layout[level]._resolve_key(level)
                self._layoutkeys[x] = x
                layout[level].render()
            elif isinstance(layout[level], list):
                cols = columns(len(layout[level]))
                for e in range(len(layout[level])):
                    if isinstance(layout[level][e], Input):
                        with cols[e]:
                            x = layout[level][e]._resolve_key(level, e)
                            self._layoutkeys[x] = x
                            layout[level][e].render()


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

    def _parse_dict(self, _type: str, _conf: Union[Dict, List]):
        """
        Parses a layout dictionary.

        Args:
            layout: layout dictionary to parse.
        Returns:
            The parsed layout dictionary.
        """
        if _type in self.__INPUT_TYPES__:
            return Input({_type: _conf})
        else:
            raise ValueError(f"type {_type} is not valid.")

    def _parse_list(self, conf: Union[List, Tuple]):
        """
        Parses a layout list.

        Args:
            layout: layout config to parse.
        Returns:
            The parsed layout list.
        """
        if conf[0] in self.__INPUT_TYPES__:
            return Input(conf)
        else:
            raise ValueError(f"type {conf[0]} is not valid.")

    def _parse_layout(self, layout: Union[List, Tuple, Dict]):
        """
        Parses a layout.

        Args:
            layout: layout to parse.
        Returns:
            The parsed layout.
        """
        lay = []
        if isinstance(layout, list):
            #This parses inputs like this: [....]
            for level in range(len(layout)):
                if isinstance(layout[level], list):
                    #This parses inputs like this: [[...],[...],[...]]
                    if len(layout[level]) == 1:
                        if isinstance(layout[level][0], dict):
                            #This parses inputs like this: [[{...}]]
                            for k, v in layout[level][0].items():
                                lay.append(self._parse_dict(k, v))
                        elif isinstance(layout[level][0], list):
                            #This parses inputs like this: [[[]]]
                            lay.append(self._parse_list(layout[level][0]))
                    else:
                        c = []
                        for cols in range(len(layout[level])):
                            if isinstance(layout[level][cols], dict):
                                #This parses inputs like this: [[..., {...}, ....]]
                                if len(layout[level][cols]) == 1:
                                    for k, v in layout[level][cols].items():
                                        c.append(self._parse_dict(k, v))
                                else:
                                    raise ValueError(f"Invalid layout dimensions at level {level}.")
                            elif isinstance(layout[level][cols], list):
                                #This parses inputs like this: [[..., [...], ....]]
                                c.append(self._parse_list(layout[level][cols]))

                            elif isinstance(layout[level][cols], Input):
                                c.append(layout[level][cols])

                elif isinstance(layout[level], dict):
                    for k, v in layout[level].items():
                        c.append(self._parse_dict(k, v))

                lay.append(c)
