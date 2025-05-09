FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los requisitos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia toda la app
COPY . .

# Agrega PYTHONPATH para que FastAPI encuentre el paquete 'app'
ENV PYTHONPATH=/app

# Ejecuta el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
