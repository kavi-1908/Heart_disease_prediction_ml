import numpy as np
import streamlit as st
import pickle 

load_model = pickle.load(open("D:\DataSci\streamlit\heart_disease\heart_disease_model.sav","rb" ))

def heart_disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    #inpt =(64,1,3,110,211,0,0,144,1,1.8,1,0,2)
    input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    cnv_inp=np.asarray(input)
    print(type(cnv_inp),cnv_inp.shape)
    rshp=cnv_inp.reshape(1,-1)
    predict = load_model.predict(rshp)
    if(predict == 1):
        return "go to nearest hospital"
    else:
        return "u r safe now "
    
    
def main():
    st.title("Heart disease prediction ")
    
    # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
    age = st.text_input("Age ")
    sex = st.text_input("sex ")
    cp = st.text_input("cp ")
    trestbps = st.text_input("trestbps")
    chol = st.text_input("chol ")
    fbs = st.text_input("fbs")
    restecg	= st.text_input("restecg")
    thalach	= st.text_input("thalach")
    exang =st.text_input("exang")
    oldpeak = st.text_input("oldpeak")
    slope = st.text_input("slope")
    ca =st.text_input("ca")
    thal = st.text_input("thal")
    
    diagonastic = ""
    
    if st.button(" click "):
        diagonastic = heart_disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    st.success(diagonastic)
    
if __name__ == '__main__':
    main()
    
    
    
