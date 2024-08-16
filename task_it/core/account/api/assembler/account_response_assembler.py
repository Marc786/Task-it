from task_it.core.account.api.dto.response.account_response import AccountResponse
from task_it.core.account.domain.account import Account


class AccountResponseAssembler:
    def account_to_response(self, user: Account):
        return AccountResponse(
            id=str(user.get_id()),
            username=str(user.get_username()),
            email=str(user.get_email()),
        )

    def accounts_to_response(self, accounts: list[Account]):
        return [self.account_to_response(account) for account in accounts]
