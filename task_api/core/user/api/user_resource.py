from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from task_api.core.user.api.assembler.user_response_assembler import (
    UserResponseAssembler,
)
from task_api.core.user.api.config.user_dependency_factory import create_user_service
from task_api.core.user.api.dto.request.create_user_request import CreateUserRequest
from task_api.core.user.application.user_service import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
def get_users(
    user_service: UserService = Depends(create_user_service),
    user_response_assembler: UserResponseAssembler = Depends(UserResponseAssembler),
):
    users = user_service.get_users()
    users_response = user_response_assembler.users_to_response(users)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=[user_response.model_dump() for user_response in users_response],
    )


@router.get("/{username}")
def get_user(
    username: str,
    user_service: UserService = Depends(create_user_service),
    user_response_assembler: UserResponseAssembler = Depends(UserResponseAssembler),
):
    user = user_service.get_user(username)
    user_response = user_response_assembler.user_to_response(user)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=user_response.model_dump(),
    )


@router.post("/")
def create_user(
    create_user_request: CreateUserRequest,
    user_service: UserService = Depends(create_user_service),
    user_response_assembler: UserResponseAssembler = Depends(UserResponseAssembler),
):
    email = create_user_request.email
    username = create_user_request.username
    user = user_service.create_user(email, username)
    user_response = user_response_assembler.user_to_response(user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=user_response.model_dump(),
    )
