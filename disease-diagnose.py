import numpy as np
import joblib
import pandas as pd
# Load the saved model
loaded_model = joblib.load('rf_model.pkl')

# Assuming you have test data X_test
# predictions = loaded_model.predict(X_test)
df_s = pd.read_csv('./Symptom-severity.csv')
# Remove Hyphen
df_s['Symptom']=df_s['Symptom'].str.replace('_',' ')

def predict(s1,s2,s3,s4='vomiting',s5='vomiting',s6='vomiting',s7='vomiting'):
    l = [s1,s2,s3,s4,s5,s6,s7]
    print(l)
    
    x= np.array(df_s['Symptom'])
    y= np.array(df_s['weight'])
    for i in range(len(l)):
        for j in range(len(x)):
            if l[i]==x[j]:
                l[i]=y[j]
    res = [l]
    pred = loaded_model.predict(res)
    print(pred[0])
predict('itching' ,'skin rash', 'nodal skin eruptions')