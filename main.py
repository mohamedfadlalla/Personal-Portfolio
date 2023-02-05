from streamlit_app import CV
import streamlit as st 
from coco import main
from my_styles import * 
st.set_page_config(page_title='Mohamed Fadlalla\'s portfolio' ,layout="wide",page_icon='👨‍🔬')
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write('# Mohamed Fadlalla')

st.write('This website serves as my portfolio and showcases one of my key works, which was completed during my internship at FRIEDRICH University. During my time there, I was tasked with data visualization for their database containing 400,000 entries, and I successfully carried out this project to a high standard. This work serves as an example of my skills and experience in data visualization and big data analysis.')



if __name__=="__main__":
    cv, coco = st.tabs(['Portfolio', ' FRIEDRICH university internship'])
    with cv:
        CV()
    with coco:
        main()

    st.markdown(footer,unsafe_allow_html=True)
