
# Laboratorio 2 - Sistema de Tipos con ANTLR

Pedro Guzmán - 22111
Gustavo Cruz - 22779

---

## Descripción General

En este laboratorio implementamos un sistema de tipos básico utilizando ANTLR para análisis semántico en Python. El objetivo fue:

* Extender una gramática ANTLR existente para incluir nuevas operaciones.
* Implementar validaciones de tipos con dos enfoques: Visitor y Listener.
* Validar y reportar errores semánticos relacionados con tipos.

---

## Gramática Extendida 

Se extendió la gramática original para incluir las siguientes nuevas operaciones:

1. **Módulo (%)**
   Calcula el residuo de la división entre dos enteros.

2. **Potencia (^)**
   Eleva un número (base) a la potencia de otro número (exponente), soportando enteros y flotantes.

3. **Operadores de comparación**
   Comparadores numéricos: `<`, `>`, `<=`, `>=`.

### Cambios importantes en la gramática

```antlr
expr:
    ...
    | expr op=('*'|'/') expr        # MulDiv
    | expr op=('+'|'-') expr        # AddSub
    | expr '%' expr                 # Mod
    | expr '^' expr                # Pow
    | expr op=('<' | '>' | '<=' | '>=') expr  # CompareContext
    | INT                          # Int
    | FLOAT                        # Float
    | STRING                       # String
    | BOOL                         # Bool
    | '(' expr ')'                 # Parens
    ;
```

---

## Sistema de Tipos

Se implementaron dos módulos principales para realizar la verificación de tipos:

* **Visitor:** `type_check_visitor.py`
  Visita los nodos del árbol y retorna el tipo inferido.
  Reporta errores levantando excepciones `TypeError`.

* **Listener:** `type_check_listener.py`
  Escucha la entrada y salida de cada regla.
  Mantiene un diccionario de tipos para los contextos y una lista de errores para reportar múltiples problemas a la vez.

### Validaciones realizadas

* Operaciones aritméticas `*`, `/`, `+`, `-` solo entre enteros y flotantes.
* Operación módulo `%` solo entre enteros.
* Potenciación `^` entre enteros o flotantes.
* Operadores comparativos (`<`, `>`, `<=`, `>=`) entre enteros o flotantes, retornando booleano.
* Las operaciones con tipos incompatibles generan errores reportados.

---

## Ejecución y Resultados

Se probó la implementación con dos archivos de prueba incluidos:

* `program_test_pass.txt`: Programa con tipos correctos que pasa la validación.
* `program_test_no_pass.txt`: Programa con errores de tipos que debe generar mensajes de error.

---

## Imágenes del proyecto

* `imagenes/1.jpg`: Entorno de desarrollo corriendo (Docker y generación de archivos con ANTLR).
* `imagenes/2.jpg`: Salida de la ejecución de `Driver.py` y `DriverListener.py` con los mensajes de validación de tipos.

---

## Uso del entorno Docker

Se incluye un `Dockerfile` que configura el entorno con ANTLR y Python. Para levantarlo y usarlo:

```bash
docker build --rm . -t lab2-image
docker run --rm -ti -v "$(pwd)/program":/program lab2-image
```

Dentro del contenedor:

1. Generar lexer y parser con Visitor y Listener:

```bash
antlr -Dlanguage=Python3 -visitor SimpleLang.g4
antlr -Dlanguage=Python3 -listener SimpleLang.g4
```

2. Ejecutar pruebas:

```bash
python3 Driver.py program_test_pass.txt
python3 Driver.py program_test_no_pass.txt
python3 DriverListener.py program_test_pass.txt
python3 DriverListener.py program_test_no_pass.txt
```

---

