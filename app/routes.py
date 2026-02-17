from fastapi import APIRouter
from .utils import now_utc_iso, hostname

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello from devops-app", "hostname": hostname()}

@router.get("/health")
def health():
    return {"status": "oki doki;)"}

@router.get("/time")
def time():
    return {"utc_time": now_utc_iso(), "hostname": hostname()}

@router.get("/echo/{msg}")
def echo(msg: str):
    return {"echo": msg, "hostname": hostname()}
