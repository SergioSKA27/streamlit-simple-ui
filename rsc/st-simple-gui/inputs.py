from typing import Dict, List, Optional, Set, Tuple, Type, Union

from streamlit import (
    checkbox,
    color_picker,
    date_input,
    file_uploader,
    multiselect,
    number_input,
    radio,
    selectbox,
    text_area,
    text_input,
    time_input,
)
from streamlit.runtime.state import WidgetCallback


class Inputs:
    def __init__(self,inputconfig: Union[List, Tuple, Dict, Type,Set], on_change: Optional[WidgetCallback]=None,**kwargs):

        if isinstance(inputconfig, dict):
            #{'type': {'name': 'text', 'value': 'default_value', 'kwargs': {'key': 'value', etc}} dict
            # {'type': ['label_name','default_value', {'key': 'value'}]}  dict 2
            #['type','label_name','default_value', {'key': 'value'}] list
            # str, int, float, bool, Type, Tuple, List, Dict, Set
            # ('label_name','text','default_value', {'key': 'value'}) tuple

            if 'type' in inputconfig:
                self._type = inputconfig['type']
                if isinstance(inputconfig['type'], dict):

                    if 'label_name' in inputconfig:
                        self._label = inputconfig['label_name']
                    else:
                        self._label = None

                    if 'kwargs' in inputconfig:
                        self._kwargs = inputconfig['kwargs']
                    else:
                        self._kwargs = {}

                    if 'value' in inputconfig:
                        self._value = inputconfig['value']
                    else:
                        self._value = None
                elif isinstance(inputconfig['type'], list):
                    if len(inputconfig['type']) == 1:
                        self._label = inputconfig['type'][0]
                        self._value = None
                        self._kwargs = {}
                    elif len(inputconfig['type']) == 2:

                        self._label =inputconfig['type'][0]
                        self._value = None
                        self._kwargs = {}
                    elif len(inputconfig['type']) == 3:
                        self._label = inputconfig['type'][0]
                        self._value = inputconfig['type'][1]
                        self._kwargs = {}
                    elif len(inputconfig['type']) == 4:
                        self._label = inputconfig['type'][0]
                        self._value = inputconfig['type'][1]
                        self._kwargs = inputconfig['type'][2]
                    elif len(inputconfig['type']) > 4:
                        raise TypeError(f"Too many items in inputconfig: {inputconfig}")
                    else:
                        raise TypeError(f"Invalid inputconfig: {inputconfig}")
            else:
                raise TypeError(f"No type in inputconfig: {inputconfig}")

        elif isinstance(inputconfig, list):
            if len(inputconfig) == 1:
                self._type = inputconfig[0]
                self._label = None
                self._value = None
                self._kwargs = {}
            if len(inputconfig) == 2:
                self._type = inputconfig[0]
                self._label = inputconfig[1]
                self._value = None
                self._kwargs = {}
            if len(inputconfig) == 3:
                self._type = inputconfig[0]
                self._label = inputconfig[1]
                self._value = inputconfig[2]
                self._kwargs = {}
            elif len(inputconfig) == 4:
                self._type = inputconfig[0]
                self._label = inputconfig[1]
                self._value = inputconfig[2]
                self._kwargs = inputconfig[3]
            elif len(inputconfig) > 4:
                raise TypeError(f"Too many items in inputconfig: {inputconfig}")
            else:
                raise TypeError(f"Invalid inputconfig: {inputconfig}")
        else:
            self._type = inputconfig
            self._label = None
            self._value = None
            self._kwargs = {}



    def render(self):
        if self._type == 'str' or self._type == 'string' or self._type == 'char' or self._type == 'character' or self._type == 'text_input':
            return self.render_text_input(self._label, self._value, **self._kwargs)

        elif (self._type == 'number' or self._type == 'int' or self._type == 'integer'
                or self._type == 'numeric' or self._type == 'num' or self._type == 'number' or
                        self._type == 'float' or self._type == 'double' or self._type == 'real' or self._type == 'number_input'):
            return self.render_number_input(self._label, self._value, **self._kwargs)

        elif self._type == 'date':
            return self.render_date_input(self._label, self._value, **self._kwargs)

        elif self._type == 'time' or self._type == 'datetime':
            return self.render_time_input(self._label, self._value, **self._kwargs)

        elif self._type == 'selectbox':
            return self.render_selectbox(self._label, self._value, **self._kwargs)

        elif self._type == 'multiselect':
            return self.render_multiselect(self._label, self._value, **self._kwargs)

        elif self._type == 'checkbox' or self._type == 'bool' or self._type == 'boolean':
            return self.render_checkbox(self._label, self._value, **self._kwargs)

        elif self._type == 'radio':
            return self.render_radio(self._label, self._value, **self._kwargs)

        elif self._type == 'file_uploader':
            return self.render_file_uploader(self._label, self._value, **self._kwargs)

        elif self._type == 'color_picker':
            return self.render_color_picker(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, list):
            return self.selectbox(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, tuple):
            return self.multiselect(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, dict):
            return self.checkbox(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, set):
            return self.radio(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, str):
            return self.text_input(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, int):
            return self.number_input(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, float):
            return self.number_input(self._label, self._value, **self._kwargs)
        elif isinstance(self._type, bool):
            return self.checkbox(self._label, self._value, **self._kwargs)
        else:
            raise TypeError(f"Invalid type: {self._type}")

    def render_text_input(self, label: str, value: str="", **kwargs):
        if label is None:
            label = ""
        if value is None:
            value = ""
        return text_input(label, value, **kwargs)

    def render_number_input(self, label, value, **kwargs):
        if not isinstance(value, (int, float)):
            if self._type == 'number' or self._type == 'int' or self._type == 'integer' or self._type == 'numeric' or self._type == 'num' or self._type == 'number' or self._type == 'number_input':
                if isinstance(value, str):
                    value = int(value)
            elif self._type == 'float' or self._type == 'double' or self._type == 'real':
                if isinstance(value, str):
                    value = float(value)
            elif isinstance(self._type, int):
                if isinstance(value, str):
                    value = int(value)
            elif isinstance(self._type, float):
                if isinstance(value, str):
                    value = float(value)
        if label is None:
            label = ""
        return number_input(label, value, **kwargs)

    def render_date_input(self, label, value, **kwargs):
        return date_input(label, value, **kwargs)

    def render_time_input(self, label, value, **kwargs):
        return time_input(label, value, **kwargs)

    def render_selectbox(self, label, options, **kwargs):
        return selectbox(label, options, **kwargs)

    def render_multiselect(self, label, options, **kwargs):
        return multiselect(label, options, **kwargs)

    def render_checkbox(self, label, value, **kwargs):
        return checkbox(label, value, **kwargs)

    def render_radio(self, label, options, **kwargs):
        return radio(label, options, **kwargs)

    def render_file_uploader(self, label, type, **kwargs):
        return file_uploader(label, type, **kwargs)

    def render_color_picker(self, label, value, **kwargs):
        return color_picker(label, value, **kwargs)

    def render_text_area(self, label, value, **kwargs):
        return text_area(label, value, **kwargs)
