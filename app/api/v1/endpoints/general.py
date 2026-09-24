from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/")
def test_v1():
    
    return{"message": "ini api v1 om"}