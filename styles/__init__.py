import lvgl as lv

from . import styles

def apply_styles(obj, style_key=None, style_set=styles.default_style_set, include_self=True, recurse=True):
    if include_self:
        if style_key is not None:
            key = style_key
        elif hasattr(obj, "style_key") and obj.style_key is not None:
            key = obj.style_key
        else:
            key = type(obj)
        for selector, style in style_set[key].items():
            obj.add_style(style, selector)
    if recurse:
        for idx in range(obj.get_child_cnt()):
            child = obj.get_child(idx)
            apply_styles(child, style_set=style_set, include_self=True)


class Theme(lv.theme_t):

    def __init__(self, disp=None, style_set=styles.default_style_set, base_theme=None):
        super().__init__()

        self.style_set = style_set
        if base_theme is None:
            # This theme is based on active theme (material)
            base_theme = lv.theme_get_from_obj(lv.scr_act())

        # This theme will be applied only after base theme is applied
        self.set_parent(base_theme)

        # Set the "apply" callback of this theme to our custom callback
        self.set_apply_cb(self.apply)

        if disp is None:
            disp = lv.disp_get_default()
        # Activate this theme on display
        disp.set_theme(self)
    
    def apply(self, theme, obj):
        apply_styles(obj, style_set=self.style_set, recurse=False)