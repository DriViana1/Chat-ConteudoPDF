import streamlit as st
from dotenv import load_dotenv 
import warnings, os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import HuggingFacePipeline
from fastapi.responses import StreamingResponse
from starlette.background import BackgroundTask
from typing import Optional, Union
import aiohttp
import torch


load_dotenv()
token=os.environ.get('HUGGING_FACE_TOKEN')
directory=r"ChatbotWebsite\chromadb"

embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(embedding_function=embeddings_model, persist_directory=directory)
hb_llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Meta-Llama-3-8B",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "top_k": 50,
        "temperature": 0.1,
    },
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = hb_llm.to(device)

custom_prompt=ChatPromptTemplate.from_messages([
    ("system", """Você é um assistente de documentos.
    - Se a resposta não estiver no contexto, diga que não sabe. Responda sempre em português."""),
    
    ("human", "Contexto: {context}\n\nPergunta: {question}")
])

rag_chain= RetrievalQA.from_chain_type(
    llm=hb_llm,
    chain_type='stuff',
    retriever=vector_store.as_retriever(top_k=3),
    chain_type_kwargs={
        'verbose':True,
        'prompt':custom_prompt}
)

def get_responses(question):
    result=rag_chain.invoke({'query':question})
    response_text=result['result']
    answer_start=response_text.find('Answer:')+len('Answer')
    answer=response_text[answer_start:].strip()
    return answer

async def cleanup_response(
    response: Optional[aiohttp.ClientResponse],
    session: Optional[aiohttp.ClientSession],
):
    if response:
        response.close()
    if session:
        await session.close()
          

def main():
    st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}

            </style>""".format(
            padding_top=1, padding_bottom=1
        ),
        unsafe_allow_html=True,
    )
    st.header("DocBot?")
    initial_message='Olá, sou um Bot de documentos, se você salvou um arquivo pdf, eu posso te ajudar a encontrar informações'
    
    if 'messages' not in st.session_state.keys():
        st.session_state.messages=[{'role':'Assistant', 'content':initial_message}]
                    
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

   
    def clear_chat_history():
        st.session_state.messages=[{'role':'Assistant', 'content':initial_message}]
    st.button('Limpar Conversas', on_click=clear_chat_history)
    
    if prompt := st.chat_input():
        if prompt.strip() != "":            
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message('user'):
                st.markdown(prompt)
            
            if st.session_state.messages[-1]['role'] != 'assistant':
                with st.chat_message('assistant'):
                    with st.spinner('Vamos lá'):
                        response=get_responses(prompt)
                        placeholder=st.empty()
                        full_response=response
                        placeholder.markdown(full_response)
                message = {"role": "user", "content": full_response}
                st.session_state.messages.append(message)
            
                    
        st.write(response)
    
        st.session_state.messages.append({"role": "assistant", "content": response})    

if __name__=='__main__':
    main()
    