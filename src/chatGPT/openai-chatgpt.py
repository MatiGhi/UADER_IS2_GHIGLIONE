import openai
import os
from dotenv import load_dotenv
import readline

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

history_file = ".chat_history"

if os.path.exists(history_file):
    readline.read_history_file(history_file)

def main():

    try:
        user_input = input("Ingrese su consulta: ").strip()

        try:
            if not user_input:
                print("La consulta está vacía. Intente nuevamente")
                return
            
            readline.add_history(user_input)
            readline.write_history_file(history_file)
            
            userquery = f"You: {user_input}"
            print(userquery)

            context = "Sos un asistente útil que responde con claridad y precisión."
            usertask = "Responder preguntas del usuario de manera informativa."

            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[
                        {"role": "system", "content": context},
                        {"role": "user", "content": usertask},
                        {"role": "user", "content": userquery}
                    ],
                    temperature=1,
                    max_tokens=4096,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                print("chatGPT:", response.choices[0].message.content.strip())

            except Exception as api_error:
                print("Ocurrió un error al invocar la API:", api_error)

        except Exception as processing_error:
                print("Ocurrió un error al invocar la API:", processing_error)

    except Exception as input_error:
                print("Ocurrió un error al invocar la API:", input_error)

if __name__ == "__main__":
    main()
