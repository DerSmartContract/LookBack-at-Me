from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import FutureMessage, GrowthEntry
from schemas import FutureMessageSchema, GrowthEntrySchema
from datetime import datetime
from typing import List
import random
from pydantic import BaseModel

router = APIRouter()


# 📌 Datenbankverbindung herstellen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📌 1️⃣ Tägliche Reflexionsfrage (Random aus einer Liste)
questions = [
    "Was war dein Highlight des Tages?",
    "Wofür bist du heute dankbar?",
    "Welche Herausforderungen hast du gemeistert?",
    "Was hast du heute gelernt?",
    "Wie fühlst du dich gerade und warum?",
]


@router.get("/api/daily-question")
def get_daily_question():
    return {"question": random.choice(questions)}


# 📌 2️⃣ Benutzer können eigene Fragen hinzufügen
class NewQuestionSchema(BaseModel):
    question: str


user_questions = []  # Temporäre Liste für Benutzerfragen


@router.post("/api/add-question")
def add_question(new_question: NewQuestionSchema):
    user_questions.append(new_question.question)
    return {"message": "Frage hinzugefügt!", "total_questions": len(user_questions)}


@router.get("/api/user-questions")
def get_user_questions():
    return {"user_questions": user_questions}


# 📌 3️⃣ Future-You Nachrichten (Speichern & Abrufen)
@router.post("/future-message/")
def create_future_message(msg: FutureMessageSchema, db: Session = Depends(get_db)):
    message = FutureMessage(message=msg.message, date=datetime.fromisoformat(msg.date))
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


@router.get("/future-messages/", response_model=List[FutureMessageSchema])
def get_future_messages(db: Session = Depends(get_db)):
    return db.query(FutureMessage).all()


# 📌 4️⃣ Fortschrittsverfolgung (Wie oft wurde reflektiert?)
reflection_count = 0  # Temporäre Speicherung (optional: in DB speichern)


@router.post("/api/reflect")
def add_reflection():
    global reflection_count
    reflection_count += 1
    return {"message": "Reflexion gespeichert!", "total_reflections": reflection_count}


@router.get("/api/reflection-count")
def get_reflection_count():
    return {"total_reflections": reflection_count}


# 📌 5️⃣ Growth-Tracking: Fortschritte speichern & abrufen
@router.post("/growth-stats/")
def create_growth_entry(entry: GrowthEntrySchema, db: Session = Depends(get_db)):
    growth_entry = GrowthEntry(
        date=datetime.fromisoformat(entry.date), progress=entry.progress
    )
    db.add(growth_entry)
    db.commit()
    db.refresh(growth_entry)
    return growth_entry


@router.get("/growth-stats/", response_model=List[GrowthEntrySchema])
def get_growth_stats(db: Session = Depends(get_db)):
    return db.query(GrowthEntry).all()
