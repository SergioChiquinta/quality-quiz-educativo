import random
import os
import sys

questions = [
    {
        "question": "¿Cuánto es 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "¿Cuál es la capital de Perú?",
        "options": ["Lima", "Cusco", "Arequipa", "Trujillo"],
        "answer": "Lima"
    },
    {
        "question": "¿Qué lenguaje se usa para páginas web?",
        "options": ["HTML", "Excel", "Paint", "Word"],
        "answer": "HTML"
    }
]

def show_welcome():
    print("=================================")
    print("        QUIZ EDUCATIVO")
    print("=================================")
    print("Responde las preguntas escribiendo el texto exacto.")
    print("=================================")

def calculate_level(score):
    if score == 0:
        return "Necesita reforzamiento"
    elif score == 1:
        return "Nivel básico"
    elif score == 2:
        return "Nivel intermedio"
    elif score == 3:
        return "Nivel avanzado"
    else:
        return "Nivel no definido"

def calculate_message(score):
    if score == 0:
        return "Debes estudiar más los temas."
    elif score == 1:
        return "Vas mejorando, pero aún falta práctica."
    elif score == 2:
        return "Buen trabajo, sigue practicando."
    elif score == 3:
        return "Excelente resultado."
    else:
        return "Resultado inválido."

def run_quiz():
    score = 0
    random.shuffle(questions)

    for item in questions:
        print("\nPregunta:")
        print(item["question"])

        for option in item["options"]:
            print("- " + option)

        try:
            user_answer = input("Tu respuesta: ")

            if user_answer.lower() == item["answer"].lower():
                print("Correcto")
                score = score + 1
            else:
                print("Incorrecto. La respuesta correcta era: " + item["answer"])
        except:
            print("Ocurrió un error al leer la respuesta.")

    print("\nResultado final:")
    print("Puntaje:", score, "de", len(questions))
    print("Nivel:", calculate_level(score))
    print("Mensaje:", calculate_message(score))

show_welcome()
run_quiz()