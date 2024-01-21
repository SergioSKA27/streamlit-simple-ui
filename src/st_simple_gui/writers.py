from typing import Dict, List, Optional, Set, Tuple, Union
from streamlit import write,markdown,text,title,header,subheader,caption,code,latex




class Writer:
    def __init__(self,writerconfig: Union[List, Tuple, Dict,Set,str] = None, **kwargs):
        self._writerconfig = writerconfig
        self.kwargs = kwargs


    def render_write(self,*args,**kwargs):
        write(*args,**kwargs)

    def render_markdown(self,body,**kwargs):
        markdown(body=body,**kwargs)

    def render_text(self,body,**kwargs):
        text(body=body,**kwargs)

    def render_title(self,body,**kwargs):
        title(body,**kwargs)

    def render_header(self,body,**kwargs):
        header(body,**kwargs)

    def render_subheader(self,body,**kwargs):
        subheader(body,**kwargs)

    def render_caption(self,body,**kwargs):
        caption(body,**kwargs)

    def render_code(self,_code: str, language: Optional[str]='python',linenumbers: Optional[bool]=False):
        code(_code,language=language,line_numbers=linenumbers)

    def render_latex(self,body,**kwargs):
        latex(body,**kwargs)
