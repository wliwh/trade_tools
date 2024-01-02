import streamlit as st
import numpy as np
import pandas as pd
import datetime as dtime
now_date = dtime.date.today()

st.title("信号汇总")
st.caption(now_date,divider=True)