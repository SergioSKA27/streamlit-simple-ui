import streamlit as st
from src.st_simple_gui import Inputs

st.warning('hi')


a = Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}})

st.write((a._type,a._label,a._value,a._kwargs))
a.render()


b = Inputs({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}})
b.render()

bfloat = Inputs({'float': {'label': 'uno', 'value': 1.0, 'kwargs': {'key': 'floatval'}}})
bfloat.render()


c = Inputs({'bool': {'label': 'uno', 'value': True, 'kwargs': {'key': 'boolval'}}})
c.render()

d = Inputs({'date': {'label': 'uno', 'value': 'today', 'kwargs': {'key': 'dateval'}}})
d.render()

dtime = Inputs({'time': {'label': 'uno', 'value': 'now', 'kwargs': {'key': 'timeval'}}})
dtime.render()

e = Inputs({'selectbox': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'selectval'}}})
e.render()

f = Inputs({'multiselect': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'multiselectval'}}})
f.render()

g = Inputs({'radio': {'label': 'uno', 'value': [1,2,3], 'kwargs': {'key': 'radioval'}}})
g.render()


h = Inputs({'file_uploader': {'label': 'uno', 'value': 'png', 'kwargs': {'key': 'fileval'}}})
h.render()

i = Inputs({'color_picker': {'label': 'uno', 'value': '#00FFAA', 'kwargs': {'key': 'colorval'}}})
i.render()

j = Inputs({'text': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'textval'}}})
j.render()


k = Inputs([],[1,2,3,4]) # render as selectbox
k.render()

ll = Inputs((),[1,2,3,4]) # render  a multiselect
ll.render()

m = Inputs({},[1,2,3,4]) # render  a radio
m.render()

n = Inputs('', 'Hi') # render  a text input
n.render()

o = Inputs(1, 2) # render  a number input
o.render()
p = Inputs(1.0, 2.0) # render  a number input float
p.render()


r = Inputs(list, [1,2,3,4,5])
r.render()

s = Inputs(tuple, [1,2,3,4,5])
s.render()

t = Inputs(dict, [1,2,3,4,5])
t.render()

u = Inputs(str, 'Hi there')
u.render()

v = Inputs(int, 1)
v.render()

w = Inputs(float, 1.0)
w.render()
