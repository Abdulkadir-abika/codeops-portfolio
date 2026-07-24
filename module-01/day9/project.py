from collections import deque
class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []      
        self.accounts = []      
    def add_child(self, branch):
        self.children.append(branch)
    def add_account(self, account):
        self.accounts.append(account)
    def total_balance(self):
        total = sum(a.balance for a in self.accounts)
        for child in self.children:
            total += child.total_balance()
        return total
class Account:
    def __init__(self, acct_type, name, number, balance):
        self.type = acct_type
        self.name = name
        self.number = number
        self.balance = balance
        self._subscribers = []
    def subscribe(self, observer):
        self._subscribers.append(observer)
    def notify(self, event):
        for s in self._subscribers:
            try:
                s.update(self, event)
            except Exception:
                pass
class AccountFactory:
    @staticmethod
    def create(acct_type, name, number, balance):
        return Account(acct_type, name, number, balance)
class AccountRegistry:
    def __init__(self):
        self._accounts = {}
    def add(self, account):
        self._accounts[account.number] = account
    def get(self, number):
        return self._accounts.get(number)

class SMSAlert:
    def update(self, account, event):
        pass
class AuditLog:
    def update(self, account, event):
        pass
def bfs(transfers, start):
    visited = set()
    queue = deque([start])
    while queue:
        acct = queue.popleft()
        if acct not in visited:
            visited.add(acct)
            for neighbor in transfers.get(acct, []):
                queue.append(neighbor)
    return visited
if __name__ == "__main__":
  a1 = AccountFactory.create("savings", "Riham", 101, 5000)
  a2 = AccountFactory.create("current", "Chala", 102, 2000)
  a3 = AccountFactory.create("savings", "Abdu", 103, 3000)

  head_office = Branch("Head Office")
  addis_region = Branch("Addis Region")
  kolfe_branch = Branch("Kolfe Branch")

  head_office.add_child(addis_region)
  addis_region.add_child(kolfe_branch)

  head_office.add_account(a3)
  addis_region.add_account(a1)
  kolfe_branch.add_account(a2)

  print(kolfe_branch.total_balance())
  print(addis_region.total_balance())
  print(head_office.total_balance())

  transfers = {101: [102], 102: [103], 103: []}

  reachable = bfs(transfers, 101)
  print(list(reachable))