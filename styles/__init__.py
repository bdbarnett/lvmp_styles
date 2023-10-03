import lvgl as lv

from . import styles

def add_styles(obj, style_key=None, style_set=styles.default_style_set):
    if style_key is not None:
        key = style_key
    elif hasattr(obj, "style_key") and obj.style_key is not None:
        key = obj.style_key
    else:
        key = type(obj)
    for selector, style in style_set[key].items():
        obj.add_style(style, selector)

def add_styles_to_children(cont, style_key=None, style_set=styles.default_style_set, include_self=True):
    if include_self:
        add_styles(cont, style_key=style_key, style_set=style_set)
    for idx in range(cont.get_child_cnt()):
        child = cont.get_child(idx)
        add_styles_to_children(cont=child, style_set=style_set, include_self=True)
