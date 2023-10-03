# SPDX-FileCopyrightText: 2023 Brad Barnett
#
# SPDX-License-Identifier: MIT

import lvgl as lv
from . import style_defs as sd

DEFAULT = 0
ROUND = 1

style_set1 = {
    DEFAULT:  {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.panel_style,
    },
    ROUND:  {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.round_panel_style,
    },
    lv.animimg: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.arc: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.arc_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.DEFAULT | lv.PART.INDICATOR: sd.arc_indicator_style,
        lv.STATE.DEFAULT | lv.PART.KNOB: sd.knob_default_style,
        lv.STATE.FOCUSED | lv.PART.KNOB: sd.knob_focused_style,
        lv.STATE.EDITED | lv.PART.KNOB: sd.knob_edited_style,
    },
    lv.bar: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.btn: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.btn_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.PRESSED | lv.PART.MAIN: sd.btn_pressed_style,
        lv.STATE.CHECKED | lv.PART.MAIN: sd.btn_checked_style,
    },
    lv.btnmatrix: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.btn_matrix_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.DEFAULT | lv.PART.ITEMS: sd.bm_btn_unchecked_style,
        lv.STATE.CHECKED | lv.PART.ITEMS: sd.bm_btn_checked_style,
        lv.STATE.FOCUSED | lv.PART.ITEMS: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.ITEMS: sd.edited_style,
        lv.STATE.EDITED | lv.PART.ITEMS: sd.focus_key_style,
    },
    lv.calendar: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.obj_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.empty_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.empty_style,
    },
    lv.calendar_header_arrow: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.calendar_header_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.empty_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.empty_style,
    },
    lv.calendar_header_dropdown: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.canvas: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.chart: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.checkbox: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.colorwheel: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.arc_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.DEFAULT | lv.PART.KNOB: sd.obj_default_style,
        lv.STATE.FOCUSED | lv.PART.KNOB: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.KNOB: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.KNOB: sd.edited_style,
    },
    lv.dropdown: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.file_explorer: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.gif: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.ime_pinyin: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.img: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.img_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.imgbtn: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.keyboard: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.label: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.label_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.led: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.line: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.list: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.list_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.menu: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.menu_cont: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.menu_page: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.menu_section: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.menu_separator: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.meter: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.meter_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.msgbox: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.obj: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.obj_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.qrcode: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.roller: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.obj_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.DEFAULT | lv.PART.SELECTED: sd.roller_selected_style,
        lv.STATE.FOCUSED | lv.PART.SELECTED: sd.focused_style,
        lv.STATE.EDITED | lv.PART.SELECTED: sd.edited_style,
    },
    lv.slider: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.slider_default_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.DEFAULT | lv.PART.INDICATOR: sd.slider_indicator_style,
        lv.STATE.DEFAULT | lv.PART.KNOB: sd.knob_default_style,
        lv.STATE.FOCUSED | lv.PART.KNOB: sd.knob_focused_style,
        lv.STATE.EDITED | lv.PART.KNOB: sd.knob_edited_style,
    },
    lv.spangroup: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.spinbox: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.spinner: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.switch: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.switch_unchecked_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
        lv.STATE.CHECKED | lv.PART.INDICATOR: sd.switch_checked_style,
        lv.STATE.DEFAULT | lv.PART.KNOB: sd.knob_default_style,
        lv.STATE.FOCUSED | lv.PART.KNOB: sd.knob_focused_style,
        lv.STATE.EDITED | lv.PART.KNOB: sd.knob_edited_style,
    },
    lv.table: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.tabview: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.tabview_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.textarea: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.textarea_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.tileview: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
    lv.win: {
        lv.STATE.DEFAULT | lv.PART.MAIN: sd.empty_style,
        lv.STATE.FOCUSED | lv.PART.MAIN: sd.focused_style,
        lv.STATE.FOCUS_KEY | lv.PART.MAIN: sd.focus_key_style,
        lv.STATE.EDITED | lv.PART.MAIN: sd.edited_style,
    },
}

default_style_set = style_set1