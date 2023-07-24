import pickle
import numpy as np

load_model = pickle.load(open("D:/DataSci/heart_disease_model.sav","rb"))
# inp=(6,148,72,35,0,33.6,0.627,50)
inpt =(64,1,3,110,211,0,0,144,1,1.8,1,0,2)
cnv_inp=np.asarray(inpt)
print(type(cnv_inp),cnv_inp.shape)
rshp=cnv_inp.reshape(1,-1)
predict = load_model.predict(rshp)
print(predict)