import pickle
import streamlit as st

loaded_model = pickle.load(open('detector_model.pkl', 'rb'))
loaded_vect = pickle.load(open('vectorizer.pkl', 'rb'))
def main():
  st.subheader('Nicolas Agreda')
  st.title("Fake News Detection")
  input_text = st.text_area("Enter the news text here", height=400)
  if st.button("Submit"):
      if input_text.strip() != "":
          val_pkl = loaded_vect.transform([input_text]).toarray()
          test_pred = loaded_model.predict(val_pkl)
          if test_pred == 0:
              print("Fake News!")
              st.error("Fake News!")
          else:
              print("Real News")
              st.balloons()
              st.success("Real News")

if __name__ == "__main__":
    main()