# Python from noob to expert

Este repositorio contiene una colección de proyectos en Python diseñada para reforzar y poner en práctica los conceptos fundamentales del lenguaje de programación.

## Nivel 1: Generador de Nombres Aleatorios

En este proyecto aprenderás a interactuar con el usuario a través de la consola, capturar datos de entrada y mostrarlos por pantalla. Sirve para reforzar conceptos básicos de Python como:

- Uso de la función `print()` para mostrar mensajes.
- Uso de la función `input()` para recibir datos.
- Concatenación de cadenas de texto.
- Manejo de variables de tipo `str`.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `random_name_generator.py`.
2. Abre la terminal y navega hasta la carpeta donde está el archivo.
3. Ejecuta el comando:

   ```bash
   python random_name_generator.py
   ```

4. Responde a las preguntas que aparecerán en pantalla para generar tu nombre aleatorio.

**Objetivos de aprendizaje:**

- Familiarizarse con la interacción básica en consola.
- Comprender cómo funcionan las funciones integradas de Python.
- Practicar la concatenación y el manejo de cadenas.

## Nivel 2: Calculadora de Propinas

En este proyecto de nivel 2 aprenderás a trabajar con tipos numéricos, conversión de datos de entrada, operaciones aritméticas y formateo de salida. Sirve para reforzar conceptos como:

- Conversión de `input()` a float e int.
- Operaciones aritméticas básicas.
- Uso de la función `round()` para redondeo.
- Formateo de cadenas con f-strings.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `tip_calculator.py`.
2. Abre la terminal y dirígete a la carpeta donde está el archivo.
3. Ejecuta el comando:

   ```bash
   python tip_calculator.py
   ```

4. Ingresa el valor de la cuenta, porcentaje de propina y número de personas para obtener el monto individual.

**Objetivos de aprendizaje:**

- Manejo de tipos numéricos (float, int).
- Aplicación de operaciones matemáticas y fórmulas.
- Redondeo de resultados.
- Uso de f-strings para formatear la salida.

## Nivel 3: Aventura en Guayakill

En este proyecto de nivel 3 aprenderás a utilizar cadenas multilínea, estructuras de control if/else anidadas, comparación de cadenas y arte ASCII para crear un pequeño juego de texto. Sirve para reforzar conceptos como:

- Uso de cadenas de texto multilínea con triple comillas.
- Estructuras condicionales y lógica anidada.
- Recepción y comparación de datos de entrada `(str)`.
- Inclusión de arte ASCII para mejorar la experiencia de usuario.
- Diseño básico de flujo de juego.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado adventure_guayakill.py.
2. Abre la terminal y ve a la carpeta donde esté el archivo.
3. Ejecuta el comando:

   ```bash
   python history.py
   ```

4. Sigue las indicaciones en pantalla para vivir la aventura.

**Objetivos de aprendizaje:**

- Dominar cadenas multilínea con triple comillas.
- Gestionar flujos de ejecución con if, elif y else.
- Anidar condicionales para decisiones múltiples.
- Comparar y evaluar input de usuario.
- Integrar arte ASCII para enriquecer salidas de consola.

## Nivel 4: Piedra, papel o tijeras

En este proyecto de nivel 4 desarrollarás un clásico juego de Piedra, Papel o Tijeras contra la computadora. Aprenderás a utilizar módulos externos `(random)`, listas, indexación, validación de entrada y estructuras condicionales complejas.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `rock_paper_scissors.py`.
2. Abre la terminal y sitúate en la carpeta donde guardaste el archivo.
3. Ejecuta el comando:

   ```bash
   python rock_paper_scissors.py
   ```

4. Ingresa 0, 1 o 2 para elegir tu jugada y compite contra la compu.

**Objetivos de aprendizaje:**

- Importar y usar funciones de módulos estándar `(randint)`.
- Definir y manejar listas.
- Acceder a elementos de una lista mediante indexación.
- Validar y gestionar entradas no válidas.
- Implementar lógica de juego con múltiples condiciones.

## Nivel 5: Generador de Contraseñas

En este proyecto de nivel 5 crearás un generador de contraseñas seguro y aleatorio. Aprenderás a trabajar con múltiples estructuras de datos, elegir elementos al azar, mezclar listas y unir caracteres en una cadena final.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `password_generator.py`.
2. Abre la terminal y sitúate en la carpeta donde guardaste el archivo.
3. Ejecuta el comando:

   ```bash
   python password_generator.py
   ```

4. Especifica la cantidad de letras, símbolos y números para generar tu contraseña.

**Objetivos de aprendizaje:**

- Importar y usar módulos estándar (`random`).
- Crear y combinar listas.
- Utilizar `random.choices()` para selección aleatoria.
- Emplear `random.shuffle()` para mezclar elementos.
- Convertir una lista de caracteres en cadena con `"".join()`.
- Formatear la salida con f-strings.

## Nivel 6: Juego del ahorcado

En este proyecto de nivel 6 desarrollarás el clásico juego del Ahorcado. Aprenderás a gestionar el flujo de juego con bucles, manejar estado (vidas, letras adivinadas), validar entradas repetidas y mostrar etapas de ASCII art para la representación visual del ahorcado.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `hangman_game.py`.
2. Asegúrate de tener en la misma carpeta los módulos auxiliares:
   - `hangman_words.py` con la lista `word_list`.
   - `hangman_art.py` con las variables `stages` y `logo`.
3. Abre la terminal y navega hasta la carpeta.
4. Ejecuta:

   ```bash
   python hangman_game.py
   ```

5. Adivina letras hasta completar la palabra o quedarte sin vidas.

**Objetivos de aprendizaje:**

- Importar módulos y gestionar dependencias entre archivos.
- Uso de bucles `while` para controlar el flujo de juego.
- Gestión de listas y cadenas para mostrar el progreso del jugador.
- Control de estado con variables (`lives`, `correct_letters`).
- Manejo de entradas repetidas y validación.
- Integración de arte ASCII para representar las etapas del ahorcado.

## Nivel 7: Cifrado César

En este proyecto de nivel 7 implementarás el cifrado César, una técnica de criptografía clásica que consiste en desplazar cada letra del texto un número fijo de posiciones en el alfabeto.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `caesar_cipher.py`.
2. Asegúrate de tener en la misma carpeta el módulo `caesar_cipher_art.py` con la variable `logo`.
3. Abre la terminal y navega hasta la carpeta.
4. Ejecuta:

   ```bash
   python caesar_cipher.py
   ```

5. Sigue las indicaciones para cifrar o descifrar mensajes.

**Objetivos de aprendizaje:**

- Definir y llamar funciones con múltiples parámetros.
- Manejar bucles `for` para procesar cadenas.
- Utilizar el operador `%` para el desplazamiento cíclico.
- Gestionar entrada de usuario y validar opciones.
- Estructurar código en módulos y archivos separados.

## Nivel 8: Subasta Secreta

En este proyecto de nivel 8 desarrollarás un programa de subasta secreta donde múltiples participantes pujan y el sistema determina al ganador con la oferta más alta.

**Cómo ejecutarlo:**

1. Guarda este código en un archivo llamado `secret_auction.py`.
2. Asegúrate de tener en la misma carpeta el módulo `secret_auction_art.py` con la variable `logo`.
3. Abre la terminal y navega hasta la carpeta.
4. Ejecuta:

   ```bash
   python secret_auction.py
   ```

5. Ingresa tu nombre y tu puja, repite hasta que no queden más participantes, y el programa mostrará el ganador.

**Objetivos de aprendizaje:**

- Importar y usar módulos (`os`).
- Manejar diccionarios para almacenar y comparar datos.
- Diseñar funciones para encapsular lógica.
- Controlar múltiples bucles anidados y validación de entradas.
- Mostrar resultados consolidados al finalizar.

## Nivel 9: Calculadora Avanzada

En este nivel construirás una calculadora avanzada que soporta operaciones básicas (suma, resta, multiplicación y división), permite continuar cálculos con el resultado anterior o reiniciar.

**Cómo ejecutarlo:**

1. Guarda este código en `calculator.py` y ten `calculator_art.py` con logo.
2. Ejecuta:

   ```bash
   python calculator.py
   ```

**Objetivos de aprendizaje:**

- Funciones para cada operación.
- Uso de diccionario de funciones.
- Recursividad y reinicio de flujo.
- Gestión de consola con `os.system`.
