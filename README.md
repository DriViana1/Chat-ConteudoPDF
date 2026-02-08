# 📚 Sistema de Busca Inteligente com RAG para Apoio ao TCC

## 📌 Visão Geral

Durante a elaboração de um Trabalho de Conclusão de Curso (TCC), é comum lidar com uma grande quantidade de artigos científicos e documentos em PDF. À medida que o volume de material cresce, torna-se cada vez mais desafiador localizar informações relevantes, correlacionar ideias entre diferentes textos e responder perguntas específicas com agilidade.

Diante desse cenário, este projeto propõe o desenvolvimento de um sistema de busca inteligente baseado em Inteligência Artificial, utilizando a abordagem RAG (Retrieval-Augmented Generation). O sistema interpreta documentos PDF, organiza seus conteúdos em um banco vetorial e permite a interação por meio de um chat capaz de gerar respostas contextualizadas e fundamentadas exclusivamente nos documentos carregados.

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é auxiliar estudantes e pesquisadores na etapa de revisão bibliográfica, oferecendo uma ferramenta capaz de:

✅ Carregar e processar documentos PDF contendo artigos científicos ou textos relevantes.
✅ Indexar os conteúdos por meio de busca vetorial, permitindo recuperação eficiente de informações.
✅ Utilizar um modelo de linguagem (LLM) para gerar respostas contextualizadas com base nos documentos.
✅ Disponibilizar um chat interativo para consultas em linguagem natural.
✅ Facilitar a análise, comparação e correlação de informações entre múltiplos documentos.

## 🧠 Arquitetura da Solução

O sistema foi desenvolvido utilizando a arquitetura RAG (Retrieval-Augmented Generation), composta pelas seguintes etapas:
Ingestão de Documentos
Upload de arquivos PDF.
Extração e segmentação do texto.
Vetorização e Armazenamento
Transformação dos textos em embeddings.
Armazenamento no banco vetorial ChromaDB.
Busca por Similaridade
Recuperação dos trechos mais relevantes com base na pergunta do usuário.
Geração de Respostas
Utilização do modelo LLaMA 3 (Hugging Face) para gerar respostas baseadas exclusivamente nos documentos recuperados.

 ## 🧩 Componentes do Sistema

O projeto é composto por três principais módulos:

📄 API de Carga de Documentos
Responsável pelo upload e processamento dos PDFs.

💬 API de Chat
Permite a interação com o usuário por meio de perguntas em linguagem natural.

🛠️ Página Administrativa
Executa os processos de:
Vetorização dos documentos
Armazenamento no banco vetorial
Busca por similaridade

## 🚀 Execução do Projeto
📦 Dependências

Crie e ative um ambiente virtual:

´´´virtualenv venv´´´
´´´venv/Scripts/activate´´´
´´´pip install -r requirements.txt´´´

▶️ Execução do Serviço

Para iniciar a aplicação:

´´´streamlit run Load_data_store.py´´´

🛠️ ## Tecnologias Utilizadas

Python 3.13
Streamlit – Interface web interativa
LangChain – Orquestração do fluxo RAG
Hugging Face (LLaMA 3) – Modelo de linguagem
ChromaDB – Banco de dados vetorial
PDF Loader – Extração de texto dos PDFs

 ##🔧 Melhorias Futuras

Algumas melhorias planejadas para evoluir o projeto:

🔹 Otimização do tempo de carregamento da página inicial no Streamlit.
🔹 Interface mais moderna e interativa.
🔹 Filtros avançados para busca (por autor, data, tema).
🔹 Indicação explícita das fontes utilizadas em cada resposta.
🔹 Controle de versões dos documentos carregados.

 ##🎓 Contexto Acadêmico

Este projeto foi desenvolvido com foco acadêmico, servindo como apoio direto à elaboração de um Trabalho de Conclusão de Curso (TCC) na área de Engenharia de Software, explorando conceitos de:
Inteligência Artificial
Processamento de Linguagem Natural (NLP)
Recuperação de Informação
Sistemas de Busca Inteligente
