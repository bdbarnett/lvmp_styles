#!/opt/bin/lv_micropython -i

# SPDX-FileCopyrightText: 2023 Brad Barnett
#
# SPDX-License-Identifier: MIT

import display_driver
import lvgl as lv
import styles

my_theme = styles.Theme()

btn = lv.btn(lv.scr_act())
btn.set_size(lv.pct(20), lv.pct(20))
btn.center()
label = lv.label(btn)
label.set_text("Button")
label.center()
