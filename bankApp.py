# 1. Note the variable login_types, the list of account types.
login_types = ["admin", "user", "guest"]
# 2. Complete the function called gatekeeper that returns the following error message strings in the following scenarios:
# For “admin”:
# program says “You have the privileges.”
# For “user”:
# program says “You have limited privileges.”
# For “guest”:
# program says “You have no privileges.”
def gatekeeper(login):
  if login == "admin":
    return "You have the privileges"
  if login == "user":
    return "You have limited privileges"
  if login =="guest":
    return "You have no privileges"
# 3. Call the gatekeeper function with a string and print what it returns.
print(gatekeeper("admin"))

# 4. How could this code be improved? Make it better. Think about what other scenarios you should cover in your if logic.
# i think it could be improved by stating the login status, and maybe do login password.
# 5. Complete the function called check_balance that takes one parameter, loan_balance.
def check_balance(loan_balance):
    if loan_balance = "0":
      return "you don't owe any money"
    if loan_balance < "0":
        return
# 6. If loan_balance is zero or more, it says “you don’t owe any money”
# 7. If loan_balance is negative, it  says “you owe $X” where X is the amount
    return

# 8. Call your function with a negative and positive number and print what it returns.
print(check_balance(300))

