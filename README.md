# Chatbot con la API de Gemini en Python

## Descripción

Este proyecto consiste en la implementación de un chatbot utilizando la API de Google Gemini y Python, siguiendo la estructura y funcionamiento de los ejemplos oficiales de quickstart de Gemini para Python y Flask.

El objetivo es comprender el funcionamiento de la API, la arquitectura de un chatbot.

## Objetivos

### Objetivo General

Replicar el funcionamiento de un proyecto base de chatbot con Python y Flask, comprendiendo cada uno de sus componentes y el proceso completo de comunicación entre la aplicación y la API de Google Gemini.

### Objetivos Específicos

- Configurar correctamente el entorno de desarrollo.
- Comprender la estructura del proyecto.
- Implementar un chatbot utilizando la API de Google Gemini.
- Comprender el funcionamiento del historial de conversación.
- Analizar el funcionamiento de Flask como servidor web.
- Implementar una interfaz visual moderna para la interacción con el usuario.
- Aplicar buenas prácticas de seguridad mediante el uso de variables de entorno para la API key.
## Tecnologías utilizadas

- Python
- Flask
- Google Gemini API
- HTML5
- CSS3
- JavaScript
- Git
- GitHub
- python-dotenv

## Requisitos

- Python 3.10 o superior
- Cuenta de Google
- API Key válida de Gemini
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

La API key gratuita puede obtenerse desde Google AI Studio: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

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
- Interfaz visual personalizada.
- Botón de nueva conversación para reiniciar el chat.
- Sección informativa sobre el nombre **ALFHEIMR** dentro de la interfaz.

## Autor

**Victor David Martinez Altamirano**  
Estudiante de Licenciatura en Ciberseguridad  
Grupo 1S3232

## Créditos

Este proyecto se basa conceptualmente en los ejemplos oficiales de inicio rápido de Google Gemini para Python y Flask, utilizados exclusivamente con fines educativos y académicos.
