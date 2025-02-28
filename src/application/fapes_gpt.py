from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader


class GPT:
    """
    Class responsavel por conectar no chat gpt
    """
    def __init__(self, OPENAI_API_KEY:str = None) -> None:
        """
        Inicializa a classe

        Args:
            OPENAI_API_KEY (str): a chave do GPT.            
        """
        self.OPENAI_API_KEY = OPENAI_API_KEY
        self.chain = None    


    def send_question(self, question:str)->str:
        """
        Envia a questão para o GPT

        Args:
            question: questão a ser enviada
        
        Returns:
            str: resposta do gpt
        """
        
        return self.chain(question)

    # Realiza o pre-processamento do texto
    def pre_process(self,pdf_path:str):
        
        try:
            context = self.__extract_text_from_pdf(pdf_path)
            prompt =  self.__create_prompt()
            self.__create_chain(context=context, prompt=prompt)
        except ValueError:
            print ("Error: {error}".format(ValueError))

    def __create_chain(self, context, prompt):
        model = ChatOpenAI(model_name="gpt-4o-mini")
        chain = (
            {"context": lambda x: context, "question": RunnablePassthrough()}
            | prompt
            | model
        )
        return chain

    def __create_prompt():
        template = """Answer the question based only on the following context:
        {context}
        Question: {question}
        """
        return ChatPromptTemplate.from_template(template)

    def __extract_text_from_pdf(self,pdf_path:str)-> str:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text 
    
    def __chunkify_txt(self,txt):

        text_splitter = RecursiveCharacterTextSplitter(
            separator= "\n",
            chunk_size= 1000,
            chunk_overlap= 200,
            length_function= len
        )
        
        chunks = text_splitter.split_text(txt)

        return chunks

    def __get_vector(self, chunks):
        embeddings = OpenAIEmbeddings()

        vectorstore = FAISS.from_texts(texts= chunks, embedding = embeddings)

        return vectorstore