# Лабораторная работа №1
# Вариант 14
# Язык: (abc)^n d e^m, n >= 0, m >= 0


def finite_automaton(word):
    state = "q0"

    # Таблица переходов
    transitions = {
        "q0": {
            "a": "q2",
            "d": "q1"
        },

        "q1": {
            "e": "q1"
        },

        "q2": {
            "b": "q3"
        },

        "q3": {
            "c": "q0"
        }
    }


    final_state = "q1"

    print("\nПоследовательность состояний:")
    print(state, end="")

    for symbol in word:

        if symbol in transitions.get(state, {}):
            state = transitions[state][symbol]
        else:
            print(" -> нет перехода", end="")
            return False

        print(" -> " + state, end="")

    print()

    return state == final_state


def main():
    print("Лабораторная работа №1")
    print("Вариант 14")
    print("Язык: (abc)^n d e^m, n >= 0, m >= 0")

    word = input("\nВведите слово: ")

    if finite_automaton(word):
        print("\nРезультат: слово ПРИНАДЛЕЖИТ языку.")
    else:
        print("\nРезультат: слово НЕ ПРИНАДЛЕЖИТ языку.")


main()