from fastapi import APIRouter, Depends, Form

router = APIRouter(prefix="/auth", tags=["Authentication"])