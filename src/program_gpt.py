from .application.fapes_gpt import GPT
import os
from dotenv import load_dotenv

def main ():
    #Carregando em memoria as variaveis do .env
    load_dotenv()

    #Buscando o dado em memoria
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # Instanciando a classe do GPT
    gpt = GPT(OPENAI_API_KEY=OPENAI_API_KEY)
    # Processando o arquivo 
    pdf_path = "G:/IFES/fapesGPT/editais/bolsas_ic/Edital_Fapes_nº_04.2024_-_Programa_Nossa_Bolsa_-_(2º_semestre).pdf"  # Replace with actual PDF path
    gpt.pre_process(pdf_path=pdf_path)

    #Enviando a questão para o GPT
    answer = gpt.send_question("O Rafael Emerick poderá tentar uma bolsa?")
    print (answer)

if __name__ == "__main__":
    main()