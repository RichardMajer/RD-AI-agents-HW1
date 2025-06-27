import re


class Extractor:

    def extract_expression(self, text: str) -> str:
        allowed_chars = re.findall(r"[0-9+\-*/().]", text)
        return "".join(allowed_chars)
