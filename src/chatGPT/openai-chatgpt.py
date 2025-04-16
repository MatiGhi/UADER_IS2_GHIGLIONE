import openai
import os
import sys
from dotenv import load_dotenv
import readline

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

history_file = ".chat_history"

if os.path.exists(history_file):
    readline.read_history_file(history_file)

convers_mode = "--convers" in sys.argv

convers_buffer = []

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

            messages = [
                 {"role": "system", "content": context},
                 {"role": "user", "content": usertask}
            ]

            if convers_mode:
                 messages.extend(convers_buffer)

            messages.append({"role": "user", "content": userquery})

            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=messages,
                    temperature=1,
                    max_tokens=4096,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                chat_response = response.choices[0].message.content.strip()
                print("chatGPT:", chat_response)

                if convers_mode: 
                     convers_buffer.append({"role": "user", "content": userquery})
                     convers_buffer.append({"role": "assistant", "content": chat_response})

            except Exception as api_error:
                print("Ocurrió un error al invocar la API:", api_error)

        except Exception as processing_error:
                print("Ocurrió un error al invocar la API:", processing_error)

    except Exception as input_error:
                print("Ocurrió un error al invocar la API:", input_error)

if __name__ == "__main__":
    main()
