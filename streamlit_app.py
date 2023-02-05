import streamlit as st 
from constant import *
import requests
import re
import io
import streamlit.components.v1 as components
from graph_builder import *
from streamlit_player import st_player
import webbrowser


def CV():
 

    with st.sidebar:
            components.html(embed_component['linkedin'],height=310)
    st.subheader('Summary')
    st.write(info['Brief'])



    st.markdown('# Skills ⚒️')

    tab1, tab2, tab3 = st.tabs(["Data Science Skills ⚒️", "Research Skills ⚒️", "Organizational Skills ⚒️"])

    with tab1:
        st.markdown('## Data Science Skills 🖥')
        def skill_tab():
            rows,cols = len(info['ds-skills'])//skill_col_size,skill_col_size
            skills = iter(info['ds-skills'])
            if len(info['ds-skills'])%skill_col_size!=0:
                rows+=1
            for x in range(rows):
                columns = st.columns(skill_col_size)
                for index_ in range(skill_col_size):
                    try:
                        columns[index_].button(next(skills))
                    except:
                        break
        with st.spinner(text="Loading section..."):
            skill_tab()

    with tab2:
        st.markdown('## Research Skills ☢')
        def skill_tab():
            rows,cols = len(info['research-skills'])//skill_col_size,skill_col_size
            skills = iter(info['research-skills'])
            if len(info['research-skills'])%skill_col_size!=0:
                rows+=1
            for x in range(rows):
                columns = st.columns(skill_col_size)
                for index_ in range(skill_col_size):
                    try:
                        columns[index_].button(next(skills))
                    except:
                        break
        with st.spinner(text="Loading section..."):
            skill_tab()

    with tab3:
        st.markdown('## Organizational Skills ✏')
        def skill_tab():
            rows,cols = len(info['Essential Skills'])//skill_col_size,skill_col_size
            skills = iter(info['Essential Skills'])
            if len(info['Essential Skills'])%skill_col_size!=0:
                rows+=1
            for x in range(rows):
                columns = st.columns(skill_col_size)
                for index_ in range(skill_col_size):
                    try:
                        columns[index_].button(next(skills))
                    except:
                        break
        with st.spinner(text="Loading section..."):
            skill_tab()






    ###### Education
    # st.subheader('Education 📖')

    # fig = go.Figure(data=[go.Table(
    #     header=dict(values=list(info['edu'].columns),
    #                 fill_color='paleturquoise',
    #                 align='left',height=65,font_size=20),
    #     cells=dict(values=info['edu'].transpose().values.tolist(),
    #                fill_color='lavender',
    #                align='left',height=40,font_size=15))])

    # fig.update_layout(width=750, height=400)
    # st.plotly_chart(fig)
    # st.subheader('Research Papers 📝')

    # def plot_bar():
        
    #     st.info('Comparing Brute Force approach with the algorithms')
    #     temp1 = rapid_metrics.loc[['Brute-Force_Printed','printed'],:].reset_index().melt(id_vars=['category'],value_vars=['precision','recall','f1_score'],var_name='metrics',value_name='%').reset_index()
        
    #     temp2 = rapid_metrics.loc[['Brute-Force_Handwritten','handwritten'],:].reset_index().melt(id_vars=['category'],value_vars=['precision','recall','f1_score'],var_name='metrics',value_name='%').reset_index()
        
    #     cols = st.columns(2)
        
    #     fig = px.bar(temp1, x="metrics", y="%", 
    #              color="category", barmode = 'group')
         
    #     cols[0].plotly_chart(fig,use_container_width=True)
        
    #     fig = px.bar(temp2, x="metrics", y="%", 
    #              color="category", barmode = 'group')
    #     cols[1].plotly_chart(fig,use_container_width=True)
        
        

    # def image_and_status_loader(image_list,index=0):
    #     if index==0:
    #         img = Image.open(image_list[0]['path'])
    #         st.image(img,caption=image_list[0]['caption'],width=image_list[0]['width'])
           
    #     else:
    #         st.success('C-Cube algorithm for printed prescriptions')
    #         rapid_metrics.loc[['Brute-Force_Printed','printed'],:].plot(kind='bar')
    #         cols = st.columns(3)
    #         for index_,items in enumerate(image_list[0]):
    #             cols[index_].image(items['path'],caption=items['caption'],use_column_width=True)
         
            
    #         st.success('3 step filtering algorithm for handwritten algorithms')
    #         cols = st.columns(3)
    #         for index_,items in enumerate(image_list[1]):
    #             cols[index_].image(items['path'],caption=items['caption'],use_column_width=True)
            
    #         plot_bar()
            
            
    st.markdown('# Publications')
    def paper_summary(index):
        st.markdown('<h5><u>'+paper_info['name'][index]+'</h5>',unsafe_allow_html=True)
        st.caption(paper_info['role'][index])
        st.caption(paper_info['journal'][index]+' , '+paper_info['publication'][index]+' , '+paper_info['year'][index])
        with st.expander('detailed description'):
            with st.spinner(text="Loading details..."):
                    st.write(paper_info['Summary'][index])
                    url = paper_info['links'][index]
                    if st.button('Link',key=index):
                        webbrowser.open_new_tab(url)


    paper_summary(0)
    paper_summary(1)



    st.sidebar.caption('Wish to connect?')
    st.sidebar.write('📧: Mohamedbadrelmaarif@gmail.com')
    pdfFileObj = open('pdfs/cv.pdf', 'rb')
    st.sidebar.download_button('download resume',
        pdfFileObj,
        file_name='Mohamed Fadlalla.pdf',
        mime='pdf')



        

        
        
    
    
