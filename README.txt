
#run app
source .venv/bin/activate
streamlit run webapp/app.py --server.port 8502

#run api
source .venv/bin/activate
uvicorn serving.api:app --reload --host 0.0.0.0 --port 8080


              precision    recall  f1-score   support

           0       0.86      0.87      0.87       973
           1       0.93      0.90      0.92       979
           2       0.89      0.79      0.84      1030
           3       0.74      0.80      0.77      1023
           4       0.82      0.84      0.83       933
           5       0.83      0.81      0.82      1015
           6       0.89      0.92      0.90       996
           7       0.87      0.85      0.86       994
           8       0.91      0.93      0.92      1017
           9       0.89      0.92      0.90      1040

    accuracy                           0.86     10000
   macro avg       0.86      0.86      0.86     10000
weighted avg       0.86      0.86      0.86     10000


