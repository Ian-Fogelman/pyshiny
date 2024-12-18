#shiny run --reload df_app.py
from shiny import App, render, ui
import pandas as pd
import shiny


app_ui = ui.page_fluid(
    ui.output_data_frame("my_table")

)

def server(input, output, session):
    @output
    @render.data_frame
    def my_table():
        df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 30, 35]
        })
        df = pd.read_csv("customers-100.csv")
        return df

app = shiny.App(app_ui, server)