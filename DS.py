	# import the streamlit library
import pickle
from pathlib import Path

import streamlit as st
from PIL import Image

st.title("The Banking Cibil App")

# image = Image.open('C:\\Users\\vella\\PycharmProjects\\DS\\unsplash.jpg')
#
# st.image(image, caption='Sunrise by the mountains')

video_file = open('C:\\Users\\vella\\PycharmProjects\\DS\\bank.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

Age = st.number_input("Age of the customer")

# TAKE HEIGHT INPUT
# radio button to choose height format
Gender = st.radio('Gender: ',
				('Male', 'Female', 'Trans'))

Emptype=st.selectbox("EmpType:",['Private','Govt'])

	# compare status value

if( Gender== 'Male'):
# take height input in centimeters
	malesal = st.number_input('sal in between 50 to 100 thousand')

	try:
		avgsal = (malesal / (12))
	except:
		st.text("Enter sal greater than 10000")

elif(Gender == 'Female'):
# take height input in meters
	femalesal = st.number_input('eneter sal of both husband and wife')

	try:
		avgsal = (femalesal / (12))
	except:
		st.text("Enter sal greater than 10000")
else:
	st.text("Trans gender not eleigible")

# check if the button is pressed or not
if(st.button('Calculate Cibil')):

	# print the BMI INDEX
	st.text("Your avg sal is {}.".format(avgsal))

	# give the interpretation of BMI index
	if(avgsal < 3):
		st.error("You are Extremely uneleigible")
	elif(avgsal >= 3 and avgsal < 6):
		st.warning("You need to improve cibil ")
	elif(avgsal >=6  and avgsal < 100):
		st.success("you are eligible")
	else:
		st.text("no proper information")






