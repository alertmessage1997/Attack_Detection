import streamlit as st
from keras.models import load_model


MODEL_PATH = 'model_cls.h5'
classifier= load_model(MODEL_PATH)

def welcome():
    return "Welcome All"

def predict_note_authentication(src_bytes,dst_bytes,duration,dst_host_srv_count,count,dst_host_count,service,flag,dst_host_srv_serror_rate,srv_serror_rate,serror_rate,dst_host_serror_rate,logged_in,num_root,num_compromised,dst_host_same_srv_rate,same_srv_rate,srv_rerror_rate,rerror_rate,dst_host_srv_rerror_rate):
       
    prediction=classifier.predict([[src_bytes,dst_bytes,duration,dst_host_srv_count,count,dst_host_count,service,flag,dst_host_srv_serror_rate,srv_serror_rate,serror_rate,dst_host_serror_rate,logged_in,num_root,num_compromised,dst_host_same_srv_rate,same_srv_rate,srv_rerror_rate,rerror_rate,dst_host_srv_rerror_rate]])
    print(prediction)
    return prediction



def main():
    st.title("Be Alert and Safe")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Attach Detection </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    src_bytes = st.number_input("src_bytes",format="%.5f")
    dst_bytes = st.number_input("dst_bytes",format="%.5f")
    duration = st.number_input("duration",format="%.5f")
    dst_host_srv_count = st.number_input("dst_host_srv_count",format="%.5f")
    count = st.number_input("count",format="%.5f")
    dst_host_count = st.number_input("dst_host_count",format="%.5f")
    service = st.number_input("service",format="%.5f")
    flag = st.number_input("flag",format="%.5f")
    dst_host_srv_serror_rate = st.number_input("dst_host_srv_serror_rate",format="%.5f")
    srv_serror_rate = st.number_input("srv_serror_rate",format="%.5f")
    serror_rate = st.number_input("serror_rate",format="%.5f")
    dst_host_serror_rate = st.number_input("dst_host_serror_rate",format="%.5f")
    logged_in = st.number_input("logged_in",format="%.5f")
    num_root = st.number_input("num_root",format="%.5f")
    num_compromised = st.number_input("num_compromised",format="%.5f")
    dst_host_same_srv_rate = st.number_input("dst_host_same_srv_rate",format="%.5f")
    same_srv_rate = st.number_input("same_srv_rate",format="%.5f")
    srv_rerror_rate = st.number_input("srv_rerror_rate",format="%.5f")
    rerror_rate = st.number_input("rerror_rate",format="%.5f")
    dst_host_srv_rerror_rate = st.number_input("dst_host_srv_rerror_rate",format="%.5f")
    
    result=0
    if st.button("Predict"):
        result=predict_note_authentication(src_bytes,dst_bytes,duration,dst_host_srv_count,count,
                                           dst_host_count,service,flag,dst_host_srv_serror_rate,srv_serror_rate,
                                           serror_rate,dst_host_serror_rate,logged_in,num_root,num_compromised,dst_host_same_srv_rate,
                                           same_srv_rate,srv_rerror_rate,rerror_rate,dst_host_srv_rerror_rate)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets have your own house")
        st.text("Built your dreams")

if __name__=='__main__':
    main()