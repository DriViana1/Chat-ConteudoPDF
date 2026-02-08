import streamlit as st
from dotenv import load_dotenv 
from pages.admin_utils import *
#Página de Upload de arquivos PDF da Ferramenta de classificação de tickets

def main():
    load_dotenv()
    st.set_page_config(page_title="Dump files")
    st.title("Upload pdf files")
    
    pdf = st.file_uploader("Only PDF's", type=["pdf"])
    
    if pdf is not None:
        with st.spinner("Wait"):
            st.write("Read PDF File is done")
            text = read_pdf(pdf)
            
            #Chunks
            st.write("Split file in chunks")
            chuncks = split_text(text)
            
            st.write("Create embeddings")
            emb = create_embeddings(chuncks)
            
            push_toChroma(chuncks)
        st.success("Sucession process!")
        
if __name__=="__main__":
    main()