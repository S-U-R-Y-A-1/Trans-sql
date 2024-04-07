from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text




def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name aiml_student and has the following columns - Roll_number,name,AI_Mark,TOC_Mark,DBMS_Mark,PA_Mark,HCI_Mark,total_mark
      \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM aiml_student ;
    \nExample 2 - Tell me all the students who scored less than 70 in AI ?, 
    the SQL command will be something like this SELECT * FROM aiml_student where AI_Mark <70 ; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]
prompt1=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name ds_student and has the following columns - Roll_number,name,BI_Mark,DA_Mark,DSA_Mark,OS_Mark,ML_Mark,total_mark
      \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM ds_student ;
    \nExample 2 - Tell me all the students who scored less than 70 in BI ?, 
    the SQL command will be something like this SELECT * FROM aiml_student where BI_Mark <70 ; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="SQL WITH NLP")
st.header("STUDENT MARKS DATABASE")
if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

def disable():
    st.session_state["disabled"] = True
def enable():
    st.session_state["disabled"] = False
st.text('USE "AIM" FOR AI & ML AND "DS" FOR DATA SCIENCE')
department=st.text_input(
    "Department", 
    disabled=st.session_state.disabled, 
    on_change=disable,
    key="dept"
)
refresh=st.button("Change Department")
question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    if department=="AIM":
        response=get_gemini_response(question,prompt)
    if department=="DS":
        response=get_gemini_response(question,prompt1)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)






if refresh:
    enable()
    st.rerun()
    
    
    
    



