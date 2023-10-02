# SPDX-FileCopyrightText: 2023 Brad Barnett
#
# SPDX-License-Identifier: MIT

import lvgl as lv

empty_style = lv.style_t()

label_style = lv.style_t()
label_style.set_text_color(lv.color_white())
label_anim=lv.anim_t()
label_anim.set_repeat_delay(3000)
label_anim.set_repeat_count(-1)
label_style.set_anim(label_anim)

panel_style = lv.style_t()
panel_style.set_bg_color(lv.palette_darken(lv.PALETTE.GREY, 1))
panel_style.set_bg_grad_dir(lv.GRAD_DIR.VER)
panel_style.set_pad_all(0)
panel_style.set_margin_top(0)
panel_style.set_margin_bottom(0)
panel_style.set_margin_left(0)
panel_style.set_margin_right(0)
panel_style.set_transform_pivot_x(lv.pct(50))
panel_style.set_transform_pivot_y(lv.pct(50))
panel_style.set_clip_corner(True)
panel_style.set_radius(0)

round_panel_style = lv.style_t()
round_panel_style.set_bg_color(lv.palette_darken(lv.PALETTE.GREY, 1))
round_panel_style.set_bg_grad_dir(lv.GRAD_DIR.VER)
round_panel_style.set_pad_all(0)
round_panel_style.set_margin_top(0)
round_panel_style.set_margin_bottom(0)
round_panel_style.set_margin_left(0)
round_panel_style.set_margin_right(0)
round_panel_style.set_transform_pivot_x(lv.pct(50))
round_panel_style.set_transform_pivot_y(lv.pct(50))
round_panel_style.set_clip_corner(True)
round_panel_style.set_radius(lv.RADIUS_CIRCLE)

obj_default_style = lv.style_t()
obj_default_style.set_bg_color(lv.palette_darken(lv.PALETTE.GREY, 2))
obj_default_style.set_outline_width(2)
obj_default_style.set_outline_pad(0)
obj_default_style.set_outline_color(lv.color_black())
obj_default_style.set_text_color(lv.color_white())
# obj_default_style.set_outline_opa(lv.OPA._50)

focused_style = lv.style_t()
focused_style.set_outline_color(lv.palette_main(lv.PALETTE.YELLOW))

focus_key_style = lv.style_t()
focus_key_style.set_outline_color(lv.palette_main(lv.PALETTE.RED))

edited_style = lv.style_t()
edited_style.set_outline_color(lv.palette_main(lv.PALETTE.GREEN))

img_default_style = lv.style_t()
img_default_style.set_img_recolor_opa(lv.OPA._100)
img_default_style.set_img_recolor(lv.color_white())

roller_selected_style = lv.style_t()
roller_selected_style.set_bg_color(lv.palette_main(lv.PALETTE.GREY))

slider_default_style = lv.style_t()
slider_default_style.set_bg_color(lv.color_black())

meter_style = lv.style_t()
meter_style.set_bg_grad_color(lv.color_white())
meter_style.set_bg_grad_color(lv.palette_main(lv.PALETTE.GREY))
meter_style.set_bg_grad_dir(lv.GRAD_DIR.VER)

slider_indicator_style = lv.style_t()
slider_indicator_style.set_bg_color(lv.palette_darken(lv.PALETTE.BLUE, 3))

arc_default_style = lv.style_t()
arc_default_style.set_arc_color(lv.color_black())
arc_default_style.set_pad_all(15)

arc_indicator_style = lv.style_t()
arc_indicator_style.set_arc_color(lv.color_white())

calendar_header_style = lv.style_t()
calendar_header_style.set_bg_color(lv.color_black())
calendar_header_style.set_bg_opa(lv.OPA._100)

list_style = lv.style_t()
list_style.set_bg_color(lv.palette_lighten(lv.PALETTE.GREY, 1))
list_style.set_pad_all(0)


btn_matrix_style = lv.style_t()
btn_matrix_style.set_bg_color(lv.palette_lighten(lv.PALETTE.GREY, 2))

bm_btn_unchecked_style = lv.style_t()
bm_btn_unchecked_style.set_bg_color(lv.palette_lighten(lv.PALETTE.GREY, 3))
bm_btn_unchecked_style.set_text_color(lv.color_black())

bm_btn_checked_style = lv.style_t()
bm_btn_checked_style.set_bg_color(lv.palette_darken(lv.PALETTE.BLUE, 3))
bm_btn_checked_style.set_text_color(lv.color_white())
bm_btn_checked_style.set_bg_opa(lv.OPA._100)

textarea_style = lv.style_t()
textarea_style.set_bg_color(lv.color_black())

tabview_style = lv.style_t()
tabview_style.set_bg_color(lv.palette_darken(lv.PALETTE.GREY, 4))

tabview_btns_style = lv.style_t()
tabview_btns_style.set_bg_color(lv.palette_lighten(lv.PALETTE.GREY, 1))

switch_unchecked_style = lv.style_t()
switch_unchecked_style.set_bg_color(lv.palette_darken(lv.PALETTE.GREY, 3))

switch_checked_style = lv.style_t()
switch_checked_style.set_bg_color(lv.palette_darken(lv.PALETTE.BLUE, 3))
switch_checked_style.set_text_color(lv.color_white())
switch_checked_style.set_bg_opa(lv.OPA._100)


btn_default_style = lv.style_t()
btn_default_style.set_radius(lv.RADIUS_CIRCLE)
btn_default_style.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
btn_default_style.set_bg_grad_dir(lv.GRAD_DIR.VER)
btn_default_style.set_border_color(lv.color_white())
btn_default_style.set_border_opa(lv.OPA._50)
btn_default_style.set_border_width(1)
btn_default_style.set_shadow_width(10)
btn_default_style.set_shadow_ofs_y(5)
btn_default_style.set_shadow_opa(lv.OPA._50)
btn_default_style.set_bg_img_recolor_opa(lv.OPA._100)
btn_default_style.set_bg_img_recolor(lv.color_white())

btn_focused_style = lv.style_t()
btn_focused_style.set_bg_color(lv.palette_main(lv.PALETTE.RED))

btn_pressed_style = lv.style_t()
btn_pressed_style.set_transform_width(-1)
btn_pressed_style.set_transform_height(-1)

knob_default_style = lv.style_t()
knob_default_style.set_radius(lv.RADIUS_CIRCLE)
knob_default_style.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
knob_default_style.set_bg_grad_dir(lv.GRAD_DIR.VER)
knob_default_style.set_border_color(lv.color_white())
knob_default_style.set_border_opa(lv.OPA._50)
knob_default_style.set_border_width(1)
knob_default_style.set_shadow_width(10)
knob_default_style.set_shadow_ofs_y(5)
knob_default_style.set_shadow_opa(lv.OPA._50)

knob_focused_style = lv.style_t()
knob_focused_style.set_bg_color(lv.palette_main(lv.PALETTE.RED))

knob_edited_style = lv.style_t()
knob_edited_style.set_bg_color(lv.palette_main(lv.PALETTE.GREEN))
