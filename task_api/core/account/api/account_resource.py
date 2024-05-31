from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from task_api.core.account.api.assembler.account_response_assembler import (
    AccountResponseAssembler,
)
from task_api.core.account.api.config.account_dependency_factory import (
    create_account_service,
)
from task_api.core.account.api.dto.request.create_account_request import (
    CreateAccountRequest,
)
from task_api.core.account.application.account_service import AccountService

router = APIRouter(
    prefix="/account",
    tags=["account"],
)


@router.get("/")
def get_accounts(
    account_service: AccountService = Depends(create_account_service),
    account_response_assembler: AccountResponseAssembler = Depends(
        AccountResponseAssembler
    ),
):
    accounts = account_service.get_accounts()
    accounts_response = account_response_assembler.accounts_to_response(accounts)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=[
            account_response.model_dump() for account_response in accounts_response
        ],
    )


@router.get("/{username}")
def get_account(
    username: str,
    account_service: AccountService = Depends(create_account_service),
    account_response_assembler: AccountResponseAssembler = Depends(
        AccountResponseAssembler
    ),
):
    account = account_service.get_account(username)
    account_response = account_response_assembler.account_to_response(account)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=account_response.model_dump(),
    )


@router.post("/")
def create_account(
    create_account_request: CreateAccountRequest,
    account_service: AccountService = Depends(create_account_service),
    account_response_assembler: AccountResponseAssembler = Depends(
        AccountResponseAssembler
    ),
):
    email = create_account_request.email
    username = create_account_request.username
    account = account_service.create_account(email, username)
    account_response = account_response_assembler.account_to_response(account)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=account_response.model_dump(),
    )
