import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle
# import pyautogui # for reset button: pip install pyautogui

# load the model.pkl
path = r'./log_model.pkl'
with open(path, "rb") as f:
	model = pickle.load(f)

# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache()

# 7 variables
# variables - pregnant, insulin, bmi, age, glucose, bp, pedigree
# sample data - 6, 148, 72, 35, 0, 33.6, 0.627, 50, 1

def prediction(pregnant, insulin, bp, age, bmi):
	# Making predictions
	prediction = model.predict([[pregnant, insulin, bp, age, bmi]])
	if prediction == 0:
		pred = 0
	else:
		pred = 1
	return pred

# putting the app related codes in main()
def main():
	# -- Set page config
    apptitle = 'DSSI Submission'
    st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
    st.title('Logistic Regression Model For Diabetes')
	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
    html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">A diabetes prediction app</h1> 
       </div> <br/>"""

    #display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    # let us make infrastructure to provide inputs
    # we will add the inputs to side bar
    st.sidebar.info('Provide input using the panel')
    st.info('Click Assess button below')

    pregnant = st.sidebar.slider('pregnant', 0, 10, 5)
    st.write('input pregnant', pregnant)

    insulin = st.sidebar.slider('insulin', 0, 800, 75)
    st.write('input insulin', insulin)

    bp = st.sidebar.slider('bp', 0, 125, 70)
    st.write('input bp', bp)

    age = st.sidebar.slider('age', 0, 120, 50)
    st.write('input age', age)

    bmi = st.sidebar.slider('bmi', 0, 70, 32)
    st.write('input bmi', bmi)

    # assessment button
    if st.button("Predict"):    
        assessment = prediction(pregnant, insulin, bp, age, bmi)
        if assessment == 0:
            st.success('**Predicition says:** You have a low chance of diabetes!!')
        else:
            st.error('**Predicition says:** You have a high chance of diabetes!!')

if __name__ == '__main__':
	main()