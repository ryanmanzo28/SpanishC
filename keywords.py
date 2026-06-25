"""Spanish-C keyword and identifier mappings."""

from __future__ import annotations

# Source-of-truth mapping used by both tokenizer and translator.
SPANISH_C_KEYWORD_MAP: dict[str, str] = {
    # Core types and qualifiers
    "vacio": "void",
    "entero": "int",
    "caracter": "char",
    "flotante": "float",
    "doble": "double",
    "largo": "long",
    "corto": "short",
    "firmado": "signed",
    "sin_signo": "unsigned",
    "constante": "const",
    "volatil": "volatile",
    "restringido": "restrict",
    "en_linea": "inline",
    "tipo_de": "typeof",
    "tipo_de_sin_calif": "typeof_unqual",

    # Control flow and expressions
    "si": "if",
    "sino": "else",
    "mientras": "while",
    "hacer": "do",
    "para": "for",
    "retornar": "return",
    "romper": "break",
    "continuar": "continue",
    "ir_a": "goto",
    "tamano_de": "sizeof",

    # Switch/case
    "seleccionar": "switch",
    "caso": "case",
    "predeterminado": "default",

    # Storage classes
    "automatico": "auto",
    "registro": "register",
    "estatico": "static",
    "externo": "extern",

    # Compound/user-defined types
    "estructura": "struct",
    "union": "union",
    "enumeracion": "enum",
    "definir_tipo": "typedef",
    "typedef": "typedef",

    # Boolean/null and modern constants
    "booleano": "bool",
    "verdadero": "true",
    "falso": "false",
    "nulo": "NULL",
    "nulo_ptr": "nullptr",

    # C11/C23 keywords
    "alinear": "_Alignas",
    "alineacion": "_Alignof",
    "atomo": "_Atomic",
    "sin_retorno": "_Noreturn",
    "estatico_assert": "_Static_assert",
    "hilo_local": "_Thread_local",
    "generico": "_Generic",
    "complejo": "_Complex",
    "imaginario": "_Imaginary",
    "asegurar": "static_assert",
    "hilo_local_c23": "thread_local",
    "const_expresion": "constexpr",

    # Preprocessor directives
    "incluir": "#include",
    "definir": "#define",
    "desdefinir": "#undef",
    "si_definido": "#ifdef",
    "si_no_definido": "#ifndef",
    "si_pp": "#if",
    "sino_pp": "#else",
    "sino_si_pp": "#elif",
    "fin_si": "#endif",
    "error": "#error",
    "advertencia": "#warning",
    "linea": "#line",
    "pragma": "#pragma",

    # Program entry and common stdio helpers
    "principal": "main",
    "imprimir": "printf",
    "imprimir_linea": "puts",
    "leer": "scanf",
    "imprimir_error": "fprintf",
    "abrir_archivo": "fopen",
    "cerrar_archivo": "fclose",

    # Common memory/string/runtime helpers
    "reservar_memoria": "malloc",
    "reservar_memoria_cero": "calloc",
    "redimensionar_memoria": "realloc",
    "liberar_memoria": "free",
    "copiar_cadena": "strcpy",
    "concatenar_cadena": "strcat",
    "comparar_cadena": "strcmp",
    "longitud_cadena": "strlen",
    "salir": "exit",
}

SPANISH_C_KEYWORDS: set[str] = set(SPANISH_C_KEYWORD_MAP.keys())
