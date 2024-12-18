#shiny run --reload app.py
from shiny.express import ui

ui.page_opts(fillable = True)

with ui.layout_column_wrap(fill=False):
    with ui.value_box():
        "Value box"
        "$1,000,000"

    with ui.value_box():
        "Value box"
        "$1,000,000"

with ui.card():
    "Card that fills remaining space..."