import streamlit as st

st.markdown("""
    <style>
    .st-emotion-cache-zq5wmm ezrtsby0 {
            visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

def web():

    st.title("try streamlit")

    st.divider()

    btn=st.button("Download")

    if btn:
        print("haii")
              
    select=st.selectbox("What your gender ?", options=("secret","Male","Female"))
    print(select)

if __name__=="__main__":
    web()



