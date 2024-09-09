import streamlit as st
import pandas as pd

# Define column headers
logs_headers = ["Date", "Time", "Severity", "Facility", "Source", "Message"]
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
    file_path = 'https://github.com/mfarook2/revealOPs/edit/test/version_1/data/summary.csv'  # Replace with your file path
    logs_data = read_data_from_file(file_path)
    #print(logs_data)
    st.table(pd.DataFrame(logs_data, columns=logs_headers,))

with tab2:
    st.write("**Raw Logs**")
    st.table(pd.DataFrame(raw_logs_data, columns=raw_logs_headers))

with tab3:
    st.write("**Debugging**")
    st.table(pd.DataFrame(debugging_data, columns=debugging_headers))
