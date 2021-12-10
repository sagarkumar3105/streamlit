import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#@st.cache(suppress_st_warning=True)
def getFile():
    f=st.file_uploader("Upload your csv file here", type="csv")
    return f
file=getFile()
b=st.button("Click to proceed")
if(b):
    if(file):
        df=pd.read_csv(file)
        st.write(df)
        st.write("Shape of your data is: "+str(df.shape))
        
        x=np.arange(0,4*np.pi,0.1)
        y=np.sin(x)
       
        fig, ax = plt.subplots()
        ax.plot(x,y)
        st.pyplot(fig)

    
