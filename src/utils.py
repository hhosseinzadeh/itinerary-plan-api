from config import db

def update_job(job_id, **kwargs):
    """Helper to update Firestore job document."""
    return db.collection("jobs").document(job_id)

