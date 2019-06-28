# -*- coding:utf-8 -*-

from mako.template import Template

tpl = '''
    ## -*- coding: utf-8 -*- 
    <%
    
       name = {'a':'world','b':'baby', 'c':u'哈哈哈'}
    %>
    % for i in name:
        hello, ${name}
    % endfor
'''

print Template(tpl, input_encoding='utf-8').render()
