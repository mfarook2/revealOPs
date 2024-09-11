import streamlit as st
import pandas as pd
from io import StringIO
import requests
import csv

# Define column headers
logs_headers = ["Date", "Time", "Severity", "Facility", "Source", "Message",""]
raw_logs_headers = ["Raw Log"]
debugging_headers = ["Root Cause"]

# Create sample data
tmp_logs_data = [
    ["2024-01-01", "12:00:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:01:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
    ["2024-01-01", "12:02:00", "ERROR", "SYSLOG", "Router3", "Interface down"],
    ["2024-01-01", "12:03:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:04:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
    ["2024-01-01", "12:05:00", "ERROR", "SYSLOG", "Router3", "Interface down"],
    ["2024-01-01", "12:06:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:07:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
    ["2024-01-01", "12:08:00", "ERROR", "SYSLOG", "Router3", "Interface down"],
    ["2024-01-01", "12:09:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:10:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
    ["2024-01-01", "12:11:00", "ERROR", "SYSLOG", "Router3", "Interface down"],
    ["2024-01-01", "12:12:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:13:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
    ["2024-01-01", "12:14:00", "ERROR", "SYSLOG", "Router3", "Interface down"],
    ["2024-01-01", "12:15:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:16:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
    ["2024-01-01", "12:17:00", "ERROR", "SYSLOG", "Router3", "Interface down"],
    ["2024-01-01", "12:18:00", "INFO", "SYSLOG", "Router1", "Interface up"],
    ["2024-01-01", "12:19:00", "WARNING", "SYSLOG", "Router2", "High CPU usage"],
]

raw_logs_data = [
    ["<190>Jan  1 12:00:00 Router1 %SYS-5-CONFIG_I: Configured from console"],
    ["<189>Jan  1 12:01:00 Router2 %SYS-3-CPU_HOG: CPU utilization 99%"],
    ["<188>Jan  1 12:02:00 Router3 %LINK-3-UPDOWN: Interface down"],
    ["<190>Jan  1 12:03:00 Router1 %SYS-5-CONFIG_I: Configured from console"],
    ["<189>Jan  1 12:04:00 Router2 %SYS-3-CPU_HOG: CPU utilization 99%"],
    ["<188>Jan  1 12:05:00 Router3 %LINK-3-UPDOWN: Interface down"],
    ["<190>Jan  1 12:06:00 Router1 %SYS-5-CONFIG_I: Configured from console"],
    ["<189>Jan  1 12:07:00 Router2 %SYS-3-CPU_HOG: CPU utilization 99%"],
    ["<188>Jan  1 12:08:00 Router3 %LINK-3-UPDOWN: Interface down"],
    ["<190>Jan  1 12:09:00 Router1 %SYS-5-CONFIG_I: Configured from console"],
   ]

debugging_data = [
    ["Root cause 1"],
    ["Root cause 2"],
    ["Root cause 3"],
    # ... (rest of the data)
]

def read_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Add CSS for tab border and grey background
st.markdown("""
    <style>
    .css-1vqmvru {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        background-color: #80a9ba; /* Grey color */
    }
    </style>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Logs", "Raw Logs", "Root Cause"])

# Add data to each tab
with tab1:
    st.write("**Logs**")
    file_path = 'https://raw.githubusercontent.com/mfarook2/revealOPs/test/version_1/data/summary.csv?raw=true'
    response = requests.get(file_path)
    #logs_data = read_data_from_file(file_path)
    if response.status_code == 200:
        logs_data = pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
    #logs_data = pd.read_csv(file_path)
    #print(logs_data)
    st.table(pd.DataFrame(logs_data, columns=logs_headers,))

with tab2:
    st.write("**Raw Logs**")
    st.table(pd.DataFrame(raw_logs_data, columns=raw_logs_headers))

with tab3:
    st.write("**Debugging**")
    st.table(pd.DataFrame(debugging_data, columns=debugging_headers))
