from openai_client import OpenAIClient
from tools.calculator import Calculator
from tools.extractor import Extractor

from openai.types.chat import ChatCompletionMessageParam


def main():
    client = OpenAIClient()
    calculator = Calculator()
    extractor = Extractor()

    messages_1: list[ChatCompletionMessageParam] = [
        {"role": "user",
         "content": "Napíš mi prosím iba jednoduchý matematický výraz na vypočítanie, napr. 2+2, bez vysvetlení alebo ďalšieho textu."}
    ]

    raw_expr = client.get_message_content(messages_1)
    print(f"🔢 Zadanie od LLM: {raw_expr}")

    clean_expr = extractor.extract_expression(raw_expr)
    print(f"🔢 Očisteny príklad: {clean_expr}")

    result = calculator.compute_expression(clean_expr)
    print(f"Výsledok: {result}")

    messages_2: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": "Si AI učiteľ, ktorý vie vysvetliť výpočty."},
        {"role": "user", "content": f"Príklad: {clean_expr}, Výsledok: {result}. Vysvetli to, prosím."}
    ]
    explanation = client.get_message_content(messages_2)
    print("Vysvetlenie od LLM:")
    print(explanation)


if __name__ == "__main__":
    main()
