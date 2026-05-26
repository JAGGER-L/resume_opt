from fastapi import APIRouter, Depends, HTTPException

from app.schemas.job import OptimizeRequest, OptimizeResponse
from app.services.job_service import JobService, get_job_service

router = APIRouter(prefix="/api/jobs", tags=["jobs"])


@router.post("/optimize", response_model=OptimizeResponse)
def optimize_resume(
    request: OptimizeRequest,
    service: JobService = Depends(get_job_service),
) -> OptimizeResponse:
    try:
        return service.optimize(request)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/{job_id}", response_model=OptimizeResponse)
def get_job(
    job_id: str,
    service: JobService = Depends(get_job_service),
) -> OptimizeResponse:
    response = service.get_job(job_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Job not found.")
    return response
