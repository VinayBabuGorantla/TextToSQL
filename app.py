from dotenv import load_dotenv
load_dotenv() # Load all the environment variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and SQL Query as response
# def get_gemini_response(question,prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt,question])
#     return response.text

# Corrected get_gemini_response function
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    
    # Concatenate the prompt and question into a single string
    prompt_text = prompt[0] + "\n" + question
    
    response = model.generate_content(prompt_text)  # Send a single string, not a list
    return response.text


# Function to retrieve query from SQL DB
def read_sql_query(sql,db):
    connect=sqlite3.connect(db)
    cursor=connect.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connect.commit()
    connect.close()
    for row in rows:
        print(row)
    return rows

# Define Your Prompt
prompt=[
"""You are an expert in converting English questions to SQL query!  
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.

For example:
Example 1 - "How many entries of records are present?",  
The SQL command will be something like this:  
SELECT COUNT(*) FROM STUDENT;

Example 2 - "Tell me all the students studying in Data Science class?",  
The SQL command will be something like this:  
SELECT * FROM STUDENT WHERE CLASS="Data Science";
"""
]

# Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)


