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
#{'type': {'name': 'text', 'value': 'default_value', 'kwargs': {'key': 'value', etc}} dict
# {'type': ['label_name','default_value', {'key': 'value'}]}  dict 2
#['type','label_name','default_value', {'key': 'value'}] list
# str, int, float, bool, Type, Tuple, List, Dict, Set
# ('label_name','text','default_value', {'key': 'value'}) tuple

class Inputs:

    __TYPES__ = [
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
    'textarea'
    ]

    def __init__(self,inputconfig: Union[List, Tuple, Dict, Type],value: Optional[Type]=None,**kwargs):
        self._type: Union[str, int, float, bool, Type, Tuple, List, Dict, Set] = None
        self._label: Optional[str] = None
        self._value: Optional[Union[str, int, float, bool, Type, Tuple, List, Dict, Set]] = None
        self._kwargs: Optional[Dict] = {}

        if isinstance(inputconfig, dict) and value is None:
            if any([key in inputconfig for key in self.__TYPES__]):
                self._type = list(inputconfig.keys()).pop()
                if isinstance(inputconfig[self._type], dict):

                    if 'label' in inputconfig[self._type]:
                        self._label = inputconfig[self._type]['label']

                    if 'kwargs' in inputconfig[self._type]:
                        self._kwargs = inputconfig[self._type]['kwargs']


                    if 'value' in inputconfig[self._type]:
                        self._value = inputconfig[self._type]['value']

                elif isinstance(inputconfig[self._type], list):
                    if len(inputconfig[self._type]) == 1:
                        self._label = inputconfig[self._type][0]
                        self._value = None
                        self._kwargs = {}

                    elif len(inputconfig[self._type]) == 2:
                        self._label = inputconfig[self._type][0]
                        self._value = inputconfig[self._type][1]
                        self._kwargs = {}
                    elif len(inputconfig[self._type]) == 3:
                        self._label = inputconfig[self._type][0]
                        self._value = inputconfig[self._type][1]
                        self._kwargs = inputconfig[self._type][2]
                    elif len(inputconfig[self._type]) > 4:
                        raise TypeError(f"Too many items in inputconfig: {inputconfig[self._type]}")
                    else:
                        raise TypeError(f"Invalid inputconfig: {inputconfig}")
            else:
                raise TypeError(f"No type in inputconfig: {inputconfig}")

        elif isinstance(inputconfig, list) and value is None:
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
            self._value = value
            self._kwargs = {}




    def render(self):
        if self._type == 'str' or self._type == 'string' or self._type == 'char' or self._type == 'character' or self._type == 'text_input':
            return self.render_text_input(self._label, self._value, **self._kwargs)

        elif (self._type == 'number' or self._type == 'int' or self._type == 'integer'
                or self._type == 'numeric' or self._type == 'num' or self._type == 'number' or
                        self._type == 'float' or self._type == 'double' or self._type == 'real' or self._type == 'number_input'):
            return self.render_number_input(self._label, self._value, **self._kwargs)

        elif self._type == 'date' or self._type == 'datetime':
            return self.render_date_input(self._label, self._value, **self._kwargs)

        elif self._type == 'time':
            return self.render_time_input(self._label, self._value, **self._kwargs)

        elif self._type == 'selectbox':
            return self.render_selectbox(self._label, self._value, **self._kwargs)

        elif self._type == 'multiselect':
            return self.render_multiselect(self._label, self._value, **self._kwargs)

        elif self._type == 'checkbox' or self._type == 'bool' or self._type == 'boolean':
            return self.render_checkbox(self._label, self._value, **self._kwargs)

        elif self._type == 'radio':
            return self.render_radio(self._label, self._value, **self._kwargs)

        elif self._type == 'file_uploader' or self._type == 'file':
            return self.render_file_uploader(self._label, self._value, **self._kwargs)

        elif self._type == 'color_picker':
            return self.render_color_picker(self._label, self._value, **self._kwargs)

        elif self._type == 'text_area' or self._type == 'textarea' or self._type == 'text':
            return self.render_text_area(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, list) or self._type == list:
            return self.render_selectbox(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, tuple) or self._type == tuple:
            return self.render_multiselect(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, dict) or self._type == dict:
            return self.render_radio(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, str) or self._type == str:
            return self.render_text_input(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, int) or self._type == int:
            return self.render_number_input(self._label, self._value, **self._kwargs)

        elif isinstance(self._type, float) or self._type == float:
            return self.render_number_input(self._label, self._value, **self._kwargs)
        else:
            raise TypeError(f"Invalid type: {self._type}")

    def render_text_input(self, label: str, value: str, **kwargs):
        if label is None:
           label = ""
        if value is None:
            value = ""
        return text_input(label, value, **kwargs)

    def render_number_input(self, label, value, **kwargs):
        if not isinstance(value, (int, float)):
            if (self._type == 'number' or self._type == 'int' or
                    self._type == 'integer' or self._type == 'numeric' or
                    self._type == 'num' or self._type == 'number' or self._type == 'number_input'):
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
        if label is None:
            label = ""
        if value is None:
            value = 'today'
        return date_input(label, value, **kwargs)

    def render_time_input(self, label, value, **kwargs):
        if label is None:
            label = ""
        if value is None:
            value = 'now'
        return time_input(label, value, **kwargs)

    def render_selectbox(self, label, options, **kwargs):
        if label is None:
            label = ""
        if options is None:
            options = []
        return selectbox(label, options, **kwargs)

    def render_multiselect(self, label, options, **kwargs):
        if label is None:
            label = ""
        if options is None:
            options = []
        return multiselect(label, options, **kwargs)

    def render_checkbox(self, label, value, **kwargs):
        if label is None:
            label = ""
        if value is None:
            value = False
        return checkbox(label, value, **kwargs)

    def render_radio(self, label, options, **kwargs):
        if label is None:
            label = ""
        if options is None:
            options = []
        return radio(label, options, **kwargs)

    def render_file_uploader(self, label, _type, **kwargs):
        if label is None:
            label = ""

        return file_uploader(label, _type, **kwargs)

    def render_color_picker(self, label, value, **kwargs):
        if label is None:
            label = ""
        return color_picker(label, value, **kwargs)

    def render_text_area(self, label, value, **kwargs):
        """
        Renders a text area input field with the specified label and initial value.

        Parameters:
        - label (str): The label for the input field.
        - value (str): The initial value for the input field.
        - **kwargs: Additional keyword arguments to customize the text area.

        Returns:
        - str: The value entered in the text area.
        """
        if label is None:
            label = ""
        if value is None:
            value = ""
        return text_area(label, value, **kwargs)

    def render_password(self, label, value, **kwargs):
        """
        Renders a password input field with the specified label and initial value.

        Parameters:
        - label (str): The label for the input field.
        - value (str): The initial value for the input field.
        - **kwargs: Additional keyword arguments to customize the text area.

        Returns:
        - str: The value entered in the text area.
        """
        if label is None:
            label = ""
        if value is None:
            value = ""
        return text_input(label, value,type='password', **kwargs)
