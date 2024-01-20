import streamlit as st
from src.st_simple_gui import Inputs, SimpleGui

st.warning('hi')


a = Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}})

b = Inputs({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}})

bfloat = Inputs({'float': {'label': 'uno', 'value': 1.0, 'kwargs': {'key': 'floatval'}}})

c = Inputs({'bool': {'label': 'uno', 'value': True, 'kwargs': {'key': 'boolval'}}})

d = Inputs({'date': {'label': 'uno', 'value': 'today', 'kwargs': {'key': 'dateval'}}})

dtime = Inputs({'time': {'label': 'uno', 'value': 'now', 'kwargs': {'key': 'timeval'}}})

e = Inputs({'selectbox': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'selectval'}}})

f = Inputs({'multiselect': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'multiselectval'}}})

n = SimpleGui([[a,b],
                [c,d],
                [e,f]
                ])

with n() as layout:
    st.write(layout)


k = SimpleGui([
        [Inputs([],['a','b','c']),Inputs({},['a','b','c'])],
        [Inputs((),['a','b','c']),Inputs(1,1)],
        [Inputs(list,['a','b','c']),Inputs(str,'')]
        ])

with k() as l2:
    st.write(l2)

j = SimpleGui([Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}}),
            Inputs({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}})])


with j() as l3:
    st.write(l3)
