import streamlit as st
from PIL import Image
import numpy as np
import keras
from keras.preprocessing import image


# Reading Image
def detect(IMG):
	CNN = keras.models.load_model("maskmodel")
	test_image = image.load_img(IMG, target_size=(150,150))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = CNN.predict(test_image)
	return result




def main():
	st.title('Mask Detector By Muhammad Hanan Asghar')
	st.set_option('deprecation.showfileUploaderEncoding', False)
	hide_menu_style = """
        	<style>
        	#MainMenu {visibility: hidden;}
 		footer {visibility: hidden;}       
		</style>
        	"""
	st.markdown(hide_menu_style, unsafe_allow_html=True)
	
	# Side bar
	activities = ["Home","About"]
	choice = st.sidebar.selectbox("Pick Something Fun", activities)

	if choice == "Home":
		st.write("Using Computer Vision with Python")
		image_file = st.file_uploader("Upload Image", type=['jpeg', 'png', 'jpg'])
		if image_file is not None:
			if st.button("Process"):
				try:
					det = detect(image_file)
					if round(int(det)) == 1:
						st.success(f"Found No Mask on Face")
					elif round(int(det)) == 0:
						st.success(f"Found Mask on Face")
				except:
					st.warning("Error in Processing the Image")
	elif choice == "About":
		st.write("Hi, My Name is Muhammad Hanan Asghar.I make this project if you want to get the source files of this project then go to this URL : ")
		github_url = """
			<a href="https://github.com/MuhammadHananAsghar" target='_blank'>Muhammad Hanan Asghar</a>
		"""
		st.markdown(github_url, unsafe_allow_html=True)

if __name__ == "__main__":
	main()
