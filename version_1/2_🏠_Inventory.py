import streamlit as st
import pandas as pd

# Page Configuration 
st.set_page_config(
    page_title= "Inventory",
    page_icon= "🏠"
)

df = pd.DataFrame(
    {
        "node_id": ["Node-1", "Node-2", "Node-3", "Node-4"],
        "ip_address": ["192.10.0.1", "192.10.0.2","192.10.0.3", "192.10.0.4"],
        "admin_status": ["up", "up", "up", "up"],
        "op_state":["up", "up", "up", "up"]
    }
)

st.dataframe(
    df,
    column_config={
        "node_id": "Node ID",
        "ip_address": "IP Address",
        "admin_status": "Admin State",
        "op_state": "Operational State"
    },
    hide_index=True,
)