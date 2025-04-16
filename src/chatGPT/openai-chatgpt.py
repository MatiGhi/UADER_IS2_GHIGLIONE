import os
import sys
import readline
import openai
from dotenv import load_dotenv

# Cargar API Key desde archivo .env
load_dotenv()

# Obtenemos la OPENAI Api Key desde las Variables de Entorno
openai.api_key = os.getenv("OPEN_API_KEY")

# Archivo donde se guarda el historial de entradas del usuario
history_file = ".chat_history"

# Si el archivo de historial existe, lo cargamos (permite usar flecha)
if os.path.exists(history_file):
    readline.read_history_file(history_file)

# Verificamos si el programa se está ejecutando en modo conversación (--convers)
convers_mode = "--convers" in sys.argv

# Inicializamos el buffer de conversación (si se usa --convers)
# Este buffer contiene tanto las consultas del usuario como las respuestas de chatGPT
convers_buffer = []

def main():
    """Función principal que gestiona la interacción con el usuario y la API"""
    try:
        # PRIMER BLOQUE try/except: Captura la entrada del usuario
        user_input = input("Ingrese su consulta: ").strip()

        try:
            # SEGUNDO BLOQUE try/except: Validación del input

            # Si el input está vacío, salimos del flujo
            if not user_input:
                print("La consulta está vacía. Intente nuevamente")
                return
            
            # Guardar input en historial
            readline.add_history(user_input)
            readline.write_history_file(history_file)
            
            # Mostramos el input con el prefijo requerido por la consigna
            userquery = f"You: {user_input}"
            print(userquery)

            # Definimos el contexto inicial del asistente
            context = "Sos un asistente útil que responde con claridad y precisión."
            usertask = "Responder preguntas del usuario de manera informativa."

            # Lista base de mensajes que incluye contexto y propósito
            messages = [
                 {"role": "system", "content": context},
                 {"role": "user", "content": usertask}
            ]

            # Si estamos en modo conversación, agregamos el historial previo
            if convers_mode:
                 messages.extend(convers_buffer)

            # Agregamos la nueva consulta actual del usuario
            messages.append({"role": "user", "content": userquery})

            try:
                # TERCER BLOQUE try/except: Llamada a la API de ChatGPT
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=messages,
                    temperature=1,
                    max_tokens=4096,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                # Procesamos la respuesta y la mostramos
                chat_response = response.choices[0].message.content.strip()
                print("chatGPT:", chat_response)

                # Si estamos en modo conversación, guardamos pregunta y respuesta en el buffer
                if convers_mode: 
                     # Guardar pregunta y respuesta en el buffer
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
