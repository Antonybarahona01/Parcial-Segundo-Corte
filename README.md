# Parcial Segundo Corte
Resolucion de 3 ejercicios usando antlr4 con lenguaje objetivo python3
--

# Integrante
- Antony Barahona

# 1. Instrucciones para Ejecutar la Calculadora de Números Complejos

## Prerrequisitos

1. **Kali Linux**: Asegúrese de estar utilizando un entorno Kali Linux o cualquier distribución compatible de Linux.
2. **Python 3**: Debe tener instalado Python 3.
   - Para verificar, ejecute:
     ```bash
     python3 --version
     ```
   - Si no está instalado, puede hacerlo con:
     ```bash
     sudo apt install python3
     ```
4. **ANTLR 4.13.2**: Necesita descargar la última versión de ANTLR.
   - Descargue el archivo `.jar` de ANTLR 4.13.2 desde [ANTLR Releases](https://www.antlr.org/download.html).
   - Coloca el archivo descargado en la carpeta que prefiera, como `~/Descargas/`.

5. **Instalación de la biblioteca `antlr4-python3-runtime` para Python 3**:
   - Ejecute el siguiente comando para instalar la versión 4.13.2:
     ```bash
     pip install antlr4-python3-runtime==4.13.2
     ```

## Estructura del Proyecto

Asegúrese de tener los siguientes archivos en una carpeta:
- `OperacionesComplejas.g4`: Archivo de gramática para la calculadora.
- `main.py`: Archivo principal de la calculadora.
- `input.txt`: Archivo con las operaciones que se desean ejecutar.

## Generar los Archivos Necesarios con ANTLR

Para generar el lexer, el parser y el visitor, ejecute el siguiente comando en la terminal desde la carpeta donde tienes el archivo `OperacionesComplejas.g4`:

```bash
java -jar /home/antony_barahona/Descargas/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor OperacionesComplejas.g4
```

Este comando generará los siguientes archivos:

- OperacionesComplejasLexer.py
- OperacionesComplejasParser.py
- OperacionesComplejasVisitor.py

Crear el Archivo de Entrada input.txt
El archivo input.txt debe contener las operaciones con números complejos que deseas ejecutar. A continuación se muestra un ejemplo del contenido que puedes colocar en input.txt:

go
Copiar código
(3 + 2i) + (1 + 4i)
(5 - 3i) * (2 + 2i)
(6 + 2i) / (2 + 1i)
Cada línea es una operación entre dos números complejos.

Ejecutar la Calculadora
Con todos los archivos generados y el archivo input.txt listo, ejecuta el archivo main.py utilizando el siguiente comando:

bash
Copiar código
python3 main.py
Este comando procesará las operaciones del archivo input.txt y mostrará el resultado de cada una en la terminal. Por ejemplo, para las operaciones mencionadas anteriormente, los resultados podrían ser algo similar a:

yaml
Copiar código
El resultado de la operación es: 4 + 6j
El resultado de la operación es: 16 + 4j
El resultado de la operación es: 4.0 + 1.0j

