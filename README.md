# SpanishC

A small Spanish-C transpiler toolkit.

It does 2 core things:
- Finds Spanish-C keywords in source code.
- Translates Spanish-C keywords into standard C keywords.

Keyword coverage is centralized in `keywords.py` and shared by tokenizer + translator.
It includes:
- core C keywords/types/control-flow
- preprocessor aliases
- common runtime/library aliases (for example `imprimir` -> `printf`)

The translator is token-aware, so it only replaces real code tokens and does not modify:
- comments
- string literals
- char literals
- partial identifier names (example: `entero_variable` stays unchanged)

Runtime/library aliases are context-aware:
- translated when used as callable identifiers (example: `imprimir(...)`)
- not translated when used as plain variable names (example: `entero imprimir = 1;`)

## Project Files

- `tokenizer.py`
	- Token scanner for Spanish-C keywords.
	- Exposes:
		- `extract_spanish_keywords(code: str) -> list[str]`
		- `tokenize_spanish_keywords(code: str) -> list[Token]`

- `thing.py`
	- Spanish-C to C translator.
	- Reads a source file, prints detected Spanish keywords, writes translated `.c` output.

- `main.py`
	- Compile-and-run wrapper.
	- Calls `thing.main()` to transpile, then compiles generated C with `gcc`, then runs the executable.

## Requirements

- Python 3.10+
- GCC installed and available in PATH

## Run

From the project folder:

```bash
python3 main.py
```

Then follow prompts:
1. `File to translate:` enter your Spanish-C source file (example: `program.sc`)
2. `Enter additional gcc arguments (comma separated):` optional (example: `-Wall,-O2`)

Translator-only mode (no compile/run):

```bash
python3 thing.py
```

## Output

- Prints all recognized Spanish keywords found in the provided source.
- Writes translated C file next to source:
	- `program.sc` -> `program.c`
- Compiles and runs the translated program when using `python3 main.py`.

Optional manual compile/run (if using `python3 thing.py`):

```bash
gcc program.c -o program && ./program
```

## Example

Input (`example.sc`):

```c
entero principal() {
		entero entero_variable = 5;
		// si this comment should stay in Spanish
		imprimir("si");
		si (entero_variable > 0) {
				retornar 0;
		}
		retornar 1;
}
```

Translation behavior:
- `entero` -> `int`
- `si` -> `if`
- `retornar` -> `return`
- `entero_variable` unchanged
- `// si ...` unchanged
- `"si"` unchanged

## Notes

- Translation currently uses simple keyword mapping from `thing.py`.
- If your source file does not end with `.sc`, output filename replacement may not behave as expected.
