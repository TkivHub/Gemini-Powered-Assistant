# Chatbot con la API de Gemini en Python

## Descripción

Este proyecto consiste en la implementación de un chatbot utilizando la API de Google Gemini y Python, siguiendo la estructura y funcionamiento de los ejemplos oficiales de quickstart de Gemini para Python y Flask. [web:128][web:129]

El objetivo es comprender el funcionamiento de la API, la arquitectura de un chatbot. [web:128][web:130]

## Objetivos

### Objetivo General

Replicar el funcionamiento de un proyecto base de chatbot con Python y Flask, comprendiendo cada uno de sus componentes y el proceso completo de comunicación entre la aplicación y la API de Google Gemini. [web:128][web:129]

### Objetivos Específicos

- Configurar correctamente el entorno de desarrollo.
- Comprender la estructura del proyecto.
- Implementar un chatbot utilizando la API de Google Gemini.
- Comprender el funcionamiento del historial de conversación.
- Analizar el funcionamiento de Flask como servidor web.
- Implementar una interfaz visual moderna para la interacción con el usuario.
- Aplicar buenas prácticas de seguridad mediante el uso de variables de entorno para la API key. [web:129][web:142]

## Tecnologías utilizadas

- Python
- Flask [web:128]
- Google Gemini API [web:129]
- HTML5
- CSS3
- JavaScript
- Git
- GitHub
- python-dotenv [web:141]

## Requisitos

- Python 3.10 o superior [web:128]
- Cuenta de Google
- API Key válida de Gemini [web:134]
- Git

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

### 2. Ingresar al proyecto

```bash
cd alfheimr
```

### 3. Crear un entorno virtual

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar la API Key

Crear un archivo llamado:

```bash
.env
```

con el siguiente contenido:

```env
GEMINI_API_KEY=TU_API_KEY
```

La API key gratuita puede obtenerse desde Google AI Studio: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey). [web:134]

## Estructura del proyecto

```text
alfheimr/
│
├── app.py
├── assistant_core.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Ejecución

El proyecto se ejecuta desde el archivo principal:

```bash
python app.py
```

También puede ejecutarse con Flask si se configura la variable correspondiente:

```bash
flask run
```

Luego abre el navegador en:

```text
http://localhost:5000
```

## Funcionalidades implementadas

- Chat conversacional con respuestas generadas por IA.
- Historial de conversación dentro de la sesión.
- Interfaz visual personalizada con estilo oscuro en tonos índigo.
- Botón de nueva conversación para reiniciar el chat.
- Sección informativa sobre el nombre **ALFHEIMR** dentro de la interfaz.
- Manejo de errores si la API key falta o no es válida.

## Autor

**Victor David Martinez Altamirano**  
Estudiante de Licenciatura en Ciberseguridad  
Grupo 1S3232

## Créditos

Este proyecto se basa conceptualmente en los ejemplos oficiales de inicio rápido de Google Gemini para Python y Flask, utilizados exclusivamente con fines educativos y académicos. [web:128][web:129]