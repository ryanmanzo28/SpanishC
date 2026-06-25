from keywords import SPANISH_C_KEYWORD_MAP
from tokenizer import extract_spanish_keywords, tokenize_spanish_keywords


RUNTIME_CALL_IDENTIFIERS = {
    "principal",
    "imprimir",
    "imprimir_linea",
    "leer",
    "imprimir_error",
    "abrir_archivo",
    "cerrar_archivo",
    "reservar_memoria",
    "reservar_memoria_cero",
    "redimensionar_memoria",
    "liberar_memoria",
    "copiar_cadena",
    "concatenar_cadena",
    "comparar_cadena",
    "longitud_cadena",
    "salir",
}


def _next_nonspace_index(code: str, start: int) -> int:
    i = start
    n = len(code)
    while i < n and code[i].isspace():
        i += 1
    return i


def _is_function_like_use(code: str, token_end: int) -> bool:
    i = _next_nonspace_index(code, token_end)
    return i < len(code) and code[i] == "("


def _is_start_of_line(code: str, token_start: int) -> bool:
    i = token_start - 1
    while i >= 0 and code[i] in (" ", "\t", "\r"):
        i -= 1
    return i < 0 or code[i] == "\n"


def translate(code: str) -> str:
    tokens = tokenize_spanish_keywords(code)
    if not tokens:
        return code

    parts: list[str] = []
    last_index = 0

    for token in tokens:
        parts.append(code[last_index:token.start])
        replacement = SPANISH_C_KEYWORD_MAP.get(token.value, token.value)

        # Translate runtime helper names only when used like a call/declaration.
        if token.value in RUNTIME_CALL_IDENTIFIERS and not _is_function_like_use(code, token.end):
            replacement = token.value

        # Translate preprocessor aliases only at start of line.
        if replacement.startswith("#") and not _is_start_of_line(code, token.start):
            replacement = token.value

        parts.append(replacement)
        last_index = token.end

    parts.append(code[last_index:])
    return "".join(parts)


def main() -> None:
    filename = input("File to translate: ").strip()

    with open(filename, "r", encoding="utf-8") as file:
        code = file.read()

    found_keywords = extract_spanish_keywords(code)
    print("Spanish keywords found:", found_keywords)

    translated = translate(code)
    output = filename.replace(".sc", ".c")

    with open(output, "w", encoding="utf-8") as file:
        file.write(translated)

    print("Created:", output)
    return output


if __name__ == "__main__":
    main()
