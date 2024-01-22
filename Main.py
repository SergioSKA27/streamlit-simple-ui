import streamlit as st
from src.st_simple_gui import Input, SimpleUI, Writer

st.warning('hi')


a = Input({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}})

b = Input({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}})

bfloat = Input({'float': {'label': 'uno', 'value': 1.0, 'kwargs': {'key': 'floatval'}}})

c = Input({'bool': {'label': 'uno', 'value': True, 'kwargs': {'key': 'boolval'}}})

d = Input({'date': {'label': 'uno', 'value': 'today', 'kwargs': {'key': 'dateval'}}})

dtime = Input({'time': {'label': 'uno', 'value': 'now', 'kwargs': {'key': 'timeval'}}})

e = Input({'selectbox': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'selectval'}}})

f = Input({'multiselect': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'multiselectval'}}})

n = SimpleUI([[a,b],
                [c,d],
                [e,f]
                ])

with n() as layout:
    st.write(layout)


k = SimpleUI([
        [Input([],['a','b','c']),Input({},['a','b','c'])],
        [Input((),['a','b','c']),Input(1,1)],
        [Input(list,['a','b','c']),Input(str,'')]
        ])

with k() as l2:
    st.write(l2)

j = SimpleUI([Input({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}}),
            Input({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}})])


with j() as l3:
    st.write(l3)



Writer()
