import json
from datetime import datetime
from fastapi import HTTPException
from google.cloud import firestore
from config import client, db
from utils import update_job
from pydantic import BaseModel


class JobData(BaseModel):
    id: str
    status: str
    payload: dict
    created_at: str


def process_job_logic(job: JobData):
    destination = job.payload.get("destination")
    duration = job.payload.get("durationDays")

    doc_ref = update_job(job.id)
    doc_ref.set({
        "status": "processing",
        "destination": job.payload.get("destination"),
        "durationDays": job.payload.get("durationDays"),
        "createdAt": firestore.SERVER_TIMESTAMP,
        "completedAt": None,
        "itinerary": None,
        "error": None,
    })
    prompt = (
        f"Generate a detailed travel itinerary for {destination} lasting {duration} days. "
        "Return ONLY the itinerary as a JSON array with this format: "
        "[{day: int, theme: string, activities: [{time: string, description: string, location: string}]}]. "
        "Do NOT include any extra text or explanation."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    itinerary_str = response.choices[0].message.content.strip()
    if itinerary_str.startswith("```"):
        itinerary_str = "\n".join(itinerary_str.split("\n")[1:-1])

    try:

        itinerary_json = json.loads(itinerary_str)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON from LLM")

    doc_ref = db.collection("jobs").document(job.id)
    doc_ref.update({
        "status": "completed",
        "completedAt": firestore.SERVER_TIMESTAMP,
        "itinerary": itinerary_json,
        "error": None,
    })

    return {"message": "Job processed successfully"}
