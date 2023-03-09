
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]