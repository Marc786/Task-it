from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/")
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{username}")
async def get_user(username: str):
    return {"username": username}

@router.post("/")
async def create_user():
    return {"username": "FakeUser"}
