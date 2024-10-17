# Parcial Segundo Corte

# Integrante
- Antony Barahona

# Prerrequisitos

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

# 1. Instrucciones para Ejecutar la Calculadora de Números Complejos

## Estructura del Proyecto

Asegúrese de tener los siguientes archivos en una carpeta:
- `OperacionesComplejas.g4`: Archivo de gramática para la calculadora.
- `main.py`: Archivo principal de la calculadora.
- `input.txt`: Archivo con las operaciones que se desean ejecutar.

## Generar los Archivos Necesarios con ANTLR

Para generar el lexer, el parser y el visitor, ejecute el siguiente comando en la terminal desde la carpeta donde tienes el archivo `OperacionesComplejas.g4`:

```bash
java -jar /ruta/a/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor OperacionesComplejas.g4
```

### Este comando generará los siguientes archivos:

- `OperacionesComplejasLexer.py`
- `OperacionesComplejasParser.py`
- `OperacionesComplejasVisitor.py`

### Crear el Archivo de Entrada input.txt
El archivo input.txt debe contener las operaciones con números complejos que desea ejecutar. A continuación se muestra un ejemplo del contenido que puede colocar en input.txt:

```bash
(3 + 2i) + (1 + 4i)
(5 - 3i) * (2 + 2i)
(6 + 2i) / (2 + 1i)
```
Cada línea es una operación entre dos números complejos.

### Ejecutar la Calculadora
Con todos los archivos generados y el archivo input.txt listo, ejecute el archivo main.py utilizando el siguiente comando:

```bash
python3 main.py
```
Este comando procesará las operaciones del archivo input.txt y mostrará el resultado de cada una en la terminal. Por ejemplo, para las operaciones mencionadas anteriormente, los resultados deberias ser algo similar a:

```bash
El resultado de la operación es: 4 + 6j
El resultado de la operación es: 16 + 4j
El resultado de la operación es: 4.0 + 1.0j
```

# 2. Instrucciones para Ejecutar El Programas Con Funciones Map y Filter

## Estructura del Proyecto

Asegúrese de tener los siguientes archivos en una carpeta:
- `Funciones.g4`: Archivo de gramática para el programa.
- `main.py`: Archivo principal.
- `input.txt`: Archivo con las operaciones que se desean ejecutar.

## Generar los Archivos Necesarios con ANTLR

Para generar el lexer, el parser y el visitor, ejecute el siguiente comando en la terminal desde la carpeta donde tienes el archivo `Funciones.g4`:

```bash
java -jar /ruta/a/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Funciones.g4
```

### Este comando generará los siguientes archivos:

- `FuncionesLexer.py`
- `FuncionesParser.py`
- `FuncionesVisitor.py`

### Crear el Archivo de Entrada input.txt
El archivo input.txt debe contener las operaciones con números complejos que desea ejecutar. A continuación se muestra un ejemplo del contenido que puede colocar en input.txt:

```bash
map(x + 2, [1, 2, 3, 4])
filter(x > 3, [1, 2, 3, 4, 5, 6])
map(x * 2, [5, 10, 15])
filter(x <= 4, [2, 3, 4, 5, 6])
```

### Ejecutar el programa
Con todos los archivos generados y el archivo input.txt listo, ejecute el archivo main.py utilizando el siguiente comando:

```bash
python3 main.py
```
Este comando procesará las operaciones del archivo input.txt y mostrará el resultado de cada una en la terminal. Por ejemplo, para las operaciones mencionadas anteriormente, los resultados deberias ser algo similar a:

```bash
Resultado de map: [3, 4, 5, 6]
Resultado de filter: [4, 5, 6]
Resultado de map: [10, 20, 30]
Resultado de filter: [2, 3, 4]
```

# 3. Instrucciones para Ejecutar El Programas Transformada de Fourier

## Estructura del Proyecto

Asegúrese de tener los siguientes archivos en una carpeta:
- `fourier.g4`: Archivo de gramática para el programa.
- `main.py`: Archivo principal.
- `input.txt`: Archivo con las operaciones que se desean ejecutar.

## Generar los Archivos Necesarios con ANTLR

Para generar el lexer, el parser y el visitor, ejecute el siguiente comando en la terminal desde la carpeta donde tienes el archivo `fourier`:

```bash
java -jar /ruta/a/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor fourier.g4
```

### Este comando generará los siguientes archivos:

- `fourier.py`
- `fourier.py`
- `fourier.py`

### Crear el Archivo de Entrada input.txt
El archivo input.txt debe contener las operaciones con números complejos que desea ejecutar. A continuación se muestra un ejemplo del contenido que puede colocar en input.txt:

```bash
f(x) = {(1, t <= a), (0, t > a)}
f(x) = {(1, t <= 3), (0, t > 3)}
sign(t) = {(1, t > 0), (-1, t < 0)}
u(t) = {(1, t >= 0), (0, t < 0)}
d(t)
cos(3 t)
sin(45 t)
SUM(inf, n = -inf, d(t - n 5))
```

### Ejecutar el programa
Con todos los archivos generados y el archivo input.txt listo, ejecute el archivo main.py utilizando el siguiente comando:

```bash
python3 main.py
```
Este comando procesará las operaciones del archivo input.txt y mostrará el resultado de cada una en la terminal. 

# Consideraciones Adicionales

Para el comando 
```bash
java -jar /ruta/a/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor fourier.g4
```

No olvide reemplazar `/ruta/a` con el directorio donde usted tiene descargado el archivo .jar de antlr, para este caso, el archivo se encontraba contenido en la carpeta `Descargas` razon por la cual el comando queda de la siguiente manera:
```bash
java -jar /home/antony_barahona/Descargas/antlr-4.13.2-complete.jar -Dlanguage=Python3 NombrePrograma.g4
```

