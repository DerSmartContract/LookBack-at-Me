📖 README.md – Digitaler Reflexionsraum

🧠 Eine moderne Plattform für tägliche Reflexionen, persönliche Entwicklung und Selbstwachstum.
🚀 Entwickelt mit FastAPI (Backend) & Next.js 15 (Frontend) – optimiert für einfache Nutzung und skalierbare Erweiterungen.

⸻

📌 Inhalt
	•	🔹 Projektübersicht
	•	🔹 Features
	•	🔹 Technologie-Stack
	•	🔹 Installation & Setup
	•	🔹 API-Endpunkte
	•	🔹 Testen der Applikation
	•	🔹 Docker-Integration
	•	🔹 Deployment
	•	🔹 Weiterentwicklung

⸻

🔹 Projektübersicht

Digitaler Reflexionsraum ist eine Plattform, die tägliche Reflexionsfragen bereitstellt, Fortschritte speichert und Nutzern ermöglicht, ihre persönliche Entwicklung zu verfolgen.

👨‍💻 Warum dieses Projekt?
	•	Fördert tägliche Reflexion & Selbstverbesserung
	•	Nutzer können eigene Reflexionsfragen hinzufügen
	•	Fortschritts-Tracking für langfristiges Wachstum
	•	Skalierbar & leicht erweiterbar

⸻

🔹 Features

✅ Tägliche Reflexionsfragen → Dynamische Fragen für tägliches Journaling
✅ Benutzerdefinierte Fragen → Nutzer können eigene Fragen speichern
✅ Future-You Nachrichten → Nachrichten an das zukünftige Ich
✅ Fortschrittsverfolgung → Visualisiertes Tracking mit Recharts
✅ Growth-Stats → Fortschritte in einer interaktiven Übersicht
✅ Moderne UI → Next.js 15 mit Tailwind CSS & Framer Motion

⸻

🔹 Technologie-Stack

Bereich	Technologie
Frontend	Next.js 15, Tailwind CSS, Framer Motion, Recharts
Backend	FastAPI, SQLAlchemy, SQLite
Testing	pytest, HTTPX, Cypress
Deployment	Vercel (Frontend), Docker & Uvicorn (Backend)



⸻

🔹 Installation & Setup

1️⃣ Systemanforderungen
	•	🐍 Python 3.10+
	•	🟢 Node.js 18+
	•	🐳 Docker (optional, falls Containerisierung gewünscht ist)

2️⃣ Projekt klonen

git clone https://github.com/dein-user/digitaler-reflexionsraum.git
cd digitaler-reflexionsraum

3️⃣ Backend installieren & starten

cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload

📌 Backend läuft jetzt auf: 👉 http://127.0.0.1:8000

4️⃣ Frontend installieren & starten

cd frontend
npm install
npm run dev

📌 Frontend läuft jetzt auf: 👉 http://localhost:3000

⸻

🔹 API-Endpunkte

📌 Reflexionsfragen

Methode	Endpoint	Beschreibung
GET	/api/daily-question	Gibt eine zufällige Reflexionsfrage zurück
POST	/api/add-question	Benutzer kann eigene Fragen speichern
GET	/api/user-questions	Liste aller benutzerdefinierten Fragen

📌 Future-You Nachrichten

Methode	Endpoint	Beschreibung
POST	/future-message/	Speichert eine Nachricht für die Zukunft
GET	/future-messages/	Ruft alle Future-You Nachrichten ab

📌 Fortschrittsverfolgung

Methode	Endpoint	Beschreibung
POST	/api/reflect	Erhöht den Fortschrittszähler
GET	/api/reflection-count	Gibt die Gesamtanzahl der Reflexionen zurück

📌 Growth-Tracking

Methode	Endpoint	Beschreibung
POST	/growth-stats/	Speichert einen Fortschrittseintrag
GET	/growth-stats/	Holt alle gespeicherten Fortschrittsdaten



⸻

🔹 Testen der Applikation

📌 Backend-Tests (pytest & HTTPX)

cd backend
pytest

📌 Frontend-Tests (Cypress)

cd frontend
npx cypress open



⸻

🔹 Docker-Integration

Falls du Backend & Frontend mit Docker starten möchtest:

1️⃣ Docker-Container starten

docker-compose up --build

📌 Backend: 👉 http://localhost:8000
📌 Frontend: 👉 http://localhost:3000

2️⃣ Alle Docker-Container stoppen

docker-compose down



⸻

🔹 Deployment

📌 Frontend auf Vercel deployen

cd frontend
vercel

📌 Backend auf einer Cloud-Instanz (z. B. AWS, DigitalOcean)

cd backend
docker build -t reflexionsraum-backend .
docker run -p 8000:8000 reflexionsraum-backend



⸻

🔹 Weiterentwicklung

🚀 Ideen für zukünftige Features:
	•	🔗 User-Authentifizierung (OAuth, JWT)
	•	📅 Kalenderbasierte Reflexion
	•	📊 KI-gestützte Analyse von Reflexionen
	•	📩 E-Mail-Reminders für zukünftige Nachrichten

⸻

💡 Fazit

📌 Digitaler Reflexionsraum bietet eine moderne Plattform zur täglichen Selbstreflexion, Fortschrittsverfolgung & persönlichen Entwicklung.
📌 Entwickelt mit FastAPI, Next.js & Docker für maximale Skalierbarkeit.
📌 Zukunftssicher & modular – leicht erweiterbar mit neuen Features.

🚀 Teste die App und werde Teil deiner eigenen Wachstumsreise! 😊
