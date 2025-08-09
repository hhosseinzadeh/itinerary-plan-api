from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import process_job_logic

router = APIRouter()

class JobData(BaseModel):
    id: str
    status: str
    payload: dict
    created_at: str

@router.post("/process")
async def process_job(job: JobData):
    try:
      return process_job_logic(job)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
