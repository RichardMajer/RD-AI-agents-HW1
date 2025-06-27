class Calculator:

    def compute_expression(self, expr: str) -> str:
        try:
            result = eval(expr, {"__builtins__": None}, {})
            return str(result)
        except Exception as e:
            return f"Chyba pri výpočte: {e}"
