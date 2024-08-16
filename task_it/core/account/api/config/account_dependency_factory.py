from task_it.config.service_locator import ServiceLocator
from task_it.core.account.application.account_service import AccountService
from task_it.core.account.domain.account_factory import AccountFactory
from task_it.core.account.domain.account_repository import AccountRepository
from task_it.core.account.infra.in_memory_account_repository import (
    InMemoryAccountRepository,
)


def create_account_service():
    account_repository = ServiceLocator().get_dependency(AccountRepository)

    account_service = AccountService(account_repository, AccountFactory())
    return account_service


def create_in_memory_account_repository():
    return InMemoryAccountRepository()
