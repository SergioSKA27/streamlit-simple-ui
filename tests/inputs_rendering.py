from src.st_simple_gui import Inputs

#This is a test file to check if all the inputs are rendering correctly
#Using different types of inputs to construct the layout
a = Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}})
a.render()

alist = Inputs({'str': ['uno', 'default_value', {'key': 'values'}]})
alist.render()

b = Inputs({'int': {'label': 'uno', 'value': 1, 'kwargs': {'key': 'intval'}}})
b.render()
bl = Inputs({'int': ['uno', 1, {'key': 'intvals'}]})
bl.render()

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

#---------------------------------------------------------------
# This features are only available in Inputs class not in SimpleGui to use this import Inputs class
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
#-----------------------------------------------------------------

x = Inputs(['color_picker','Hi','#00FFAA',{'key':'colorvallist'}])
x.render()
y = Inputs(['text','uno','xd',{'key':'textvallist'}])
y.render()

z = Inputs(['file_uploader','uno','png',{'key':'filevallist'}])
z.render()
