# Análisis de la gramática ANTLR y archivo Driver en Python

Este documento explica el funcionamiento de una gramática escrita en ANTLR y cómo se conecta con un archivo driver en Python para analizar código fuente. También se comenta el propósito de cada elemento en la gramática .g4.

---

## ¿Qué es ANTLR?

ANTLR (Another Tool for Language Recognition) es una herramienta para construir analizadores léxicos y sintácticos que permite definir lenguajes de programación o DSLs mediante gramáticas.

---

## Link al video

(video)[https://youtu.be/3V1PrzTtGcA]

---

## Estructura de una gramática .g4

Un archivo .g4 define la sintaxis y los tokens del lenguaje. Sus principales secciones son:

### 1. Encabezado

```antlr
grammar MiniLang;
```

Define el nombre de la gramática. ANTLR lo usa para generar archivos como MiniLangLexer, MiniLangParser, etc.

---

### 2. Reglas del Parser (sintácticas)

```antlr
prog: stat+ ;
stat: expr NEWLINE          # printExpr
    | ID '=' expr NEWLINE   # assign
    | NEWLINE               # blank ;
expr: expr ('*'|'/') expr   # MulDiv
    | expr ('+'|'-') expr   # AddSub
    | INT                   # int
    | ID                    # id
    | '(' expr ')'          # parens ;
```

Estas reglas definen la estructura del lenguaje, como sentencias, expresiones, operadores, etc. Se escriben en minúscula. 

---

### 3. Reglas Léxicas (tokens)

```antlr
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;
NEWLINE : '\r'? '\n' ;
WS : [ \t]+ -> skip ;
```

Estas reglas identifican los símbolos básicos del lenguaje (números, operadores, identificadores, espacios, etc.). Se escriben en mayúscula (ID, INT, etc.).

---

### 4. Uso de # en ANTLR

```antlr
stat: expr NEWLINE          # printExpr
```

El símbolo # sirve para nombrar una alternativa dentro de una regla, lo que permite que ANTLR cree nodos con nombres específicos en el árbol de sintaxis. Esto facilita el trabajo con listeners o visitors.

---

## Funcionamiento del archivo Driver (main.py)

Este archivo en Python se encarga de:

1. Leer el archivo fuente del usuario
2. Tokenizar el contenido
3. Analizar la sintaxis
4. Construir el árbol de análisis (parse tree)

```python
input_stream = FileStream(argv[1])
lexer = MiniLangLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = MiniLangParser(stream)
tree = parser.prog()
```

### ¿Qué hace cada línea?

- FileStream: lee el archivo de entrada
- MiniLangLexer: convierte el texto en tokens
- CommonTokenStream: almacena los tokens generados
- MiniLangParser: analiza la secuencia de tokens
- parser.prog(): aplica la regla inicial prog y retorna el árbol

> Este archivo no evalúa ni ejecuta el código. Solo genera el árbol de sintaxis.

---

## Listener (MiniLangListener)

ANTLR genera una clase llamada MiniLangListener con métodos vacíos como:

```python
def enterAssign(self, ctx): pass
def exitAssign(self, ctx): pass
```

Se puede  extender esta clase para:

- Evaluar expresiones
- Asignar variables
- Imprimir resultados

Y luego usar un ParseTreeWalker para recorrer el árbol y ejecutar lógica:

```python
walker = ParseTreeWalker()
walker.walk(MyCustomListener(), tree)
```

---

## Conclusión

| Elemento | Función |
|---------|---------|
| .g4 | Define el lenguaje: tokens + reglas gramaticales |
| #nombre | Asigna un nombre a una alternativa de producción |
| MiniLangLexer | Lexer generado por ANTLR que convierte texto en tokens |
| MiniLangParser | Parser generado que construye el árbol de sintaxis |
| MiniLangListener | Clase base para recorrer el árbol de forma estructurada |
| main.py | Script que analiza el código fuente y construye el árbol sintáctico |

Estos componentes permiten construir intérpretes, analizadores o compiladores personalizados de forma modular con ANTLR.
