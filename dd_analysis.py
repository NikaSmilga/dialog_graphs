import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid


# To see a beautiful interactive table, run with `streamlit run <filepath>`
# To group the table properly, open Columns (right-hand sidebar), drag first `id_and_goal`,
# then goal type column (`open_goal` or `durec_goal_1`) to Row Groups.
# Then one row in a table will correspond to one dialog. Dialog is represented as a sequence
# of goals/dialog acts/etc. Eacg row is clickable, so you take a closer look at each goal and
# the corresponding utterances.

def build_table(data: pd.DataFrame) -> None:
    """Creates an interactive streamlit-AgGrid table.

    Args:
        data: Pandas dataframe with the data to be put into the streamlit table.
    """

    builder = GridOptionsBuilder.from_dataframe(data)
    builder.configure_side_bar()
    builder.configure_pagination(
        paginationAutoPageSize=False, paginationPageSize=50)
    builder.configure_default_column(
        groupable=True, value=True, enableRowGroup=True, editable=True)
    go = builder.build()
    AgGrid(data, gridOptions=go)


data_durec = pd.read_csv('dialog_data/processed/durec_fin.tsv', sep='\t')
data_open = pd.read_csv('dialog_data/processed/open_fin.tsv', sep='\t')
del data_durec['Unnamed: 0']
del data_open['Unnamed: 0']
st.set_page_config(page_title="DD goals", layout="wide")
st.title("Daily dialog goal analysis")

build_table(data_durec)
build_table(data_open)
