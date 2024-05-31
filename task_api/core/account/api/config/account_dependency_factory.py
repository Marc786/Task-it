from task_api.config.service_locator import ServiceLocator
from task_api.core.account.application.account_service import AccountService
from task_api.core.account.domain.account_factory import AccountFactory
from task_api.core.account.domain.account_repository import AccountRepository
from task_api.core.account.infra.InMemoryAccountRepository import (
    InMemoryAccountRepository,
)


def create_account_service():
    account_repository = ServiceLocator().get_dependency(AccountRepository)

    account_service = AccountService(account_repository, AccountFactory())
    return account_service


def create_in_memory_account_repository():
    return InMemoryAccountRepository()
