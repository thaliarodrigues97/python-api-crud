FROM python:3.11-slim

RUN useradd -m mba_usp_esalq

WORKDIR /app

COPY --chown=mba_usp_esalq:mba_usp_esalq . .

RUN pip install --no-cache-dir -r requirements.txt

USER mba_usp_esalq

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]