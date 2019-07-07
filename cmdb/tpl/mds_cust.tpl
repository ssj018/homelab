## -*- coding: utf-8 -*-
<%! from ansiblecmdb.util import to_bool %>

<%def name="var_cols(cols_visible=None, cols_exclude=None)">
  <%

  cols = [
    {"title": "Name",          "id": "name",          "func": col_name,           "sType": "string", "visible": True},]
  # Include only given columns if -c / --columns is given
  if cols_visible is not None:
    cols = list(filter(lambda col: col["id"] in cols_visible, cols))

  # Remove columns that should be excluded if --exclude-cols is given
  if cols_exclude is not None:
    cols = list(filter(lambda col: col["id"] not in cols_exclude, cols))

  return cols
  %>
</%def>