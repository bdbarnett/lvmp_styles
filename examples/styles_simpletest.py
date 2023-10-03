#!/opt/bin/lv_micropython -i

# SPDX-FileCopyrightText: 2023 Brad Barnett
#
# SPDX-License-Identifier: MIT

import display_driver
import lvgl as lv
import styles

class MyCont(lv.obj):
    style_key = styles.styles.DEFAULT
    def __init__(self, parent):
        super().__init__(parent)

def set_cont2_style(event):
    target = event.get_target_obj()
    checked = target.has_state(lv.STATE.CHECKED)
    if checked:
        cont2.style_key = styles.styles.ROUND
    else:
        cont2.style_key = styles.styles.DEFAULT
    styles.add_styles_to_children(cont2)

scr = lv.scr_act()

cont1 = lv.obj(scr)
cont1.set_size(lv.pct(50), lv.pct(100))
cont1.align(lv.ALIGN.LEFT_MID, 0, 0)
btn1 = lv.btn(cont1)
btn1.set_size(100, 100)
btn1.center()
btn1.add_event(lambda e: styles.add_styles_to_children(cont1), lv.EVENT.SHORT_CLICKED, None)
label1 = lv.label(btn1)
label1.set_text("Press Once")
label1.center()

cont2 = MyCont(scr)
cont2.set_size(lv.pct(50), lv.pct(100))
cont2.align(lv.ALIGN.RIGHT_MID, 0, 0)
btn2 = lv.btn(cont2)
btn2.set_size(100, 100)
btn2.center()
btn2.add_flag(lv.obj.FLAG.CHECKABLE)
btn2.add_event(set_cont2_style, lv.EVENT.SHORT_CLICKED, None)
label2 = lv.label(btn2)
label2.set_text("Press Twice")
label2.center()
