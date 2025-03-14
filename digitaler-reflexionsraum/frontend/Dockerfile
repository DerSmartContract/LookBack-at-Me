# Basis-Image für Node.js (Version 18 empfohlen)
FROM node:18

# Arbeitsverzeichnis im Container
WORKDIR /app

# Alle Dateien ins Arbeitsverzeichnis kopieren
COPY . .

# Abhängigkeiten installieren
RUN npm install

# Standardbefehl für den Start des Containers
CMD ["npm", "run", "dev"]
