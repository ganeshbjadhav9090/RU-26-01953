

OPENING_BALANCE = 10000
MAX_LIMIT = 100000


def validate_transaction(t_type, amount_text, balance):
    """Checks one transaction.
    Returns (True, amount) if valid, otherwise (False, reason)."""

   
    if t_type != "Deposit" and t_type != "Withdraw":
        return False, "unknown type '" + t_type + "'"

    
    try:
        amount = int(amount_text)
    except ValueError:
        return False, "amount '" + amount_text + "' is not a number"

    
    if amount <= 0:
        return False, "amount must be positive"
    if amount > MAX_LIMIT:
        return False, "exceeds limit of " + str(MAX_LIMIT)

    
    if t_type == "Withdraw" and amount > balance:
        return False, "insufficient balance"

    return True, amount


def main():
    balance = OPENING_BALANCE
    valid_count = 0
    invalid_count = 0
    valid_lines = []

    
    try:
        file = open("transactions.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: transactions.txt not found.")
        return

    line_no = 0
    for line in lines:
        line = line.strip()
        if line == "":          
            continue
        line_no += 1

        parts = line.split(",")
        if len(parts) != 2:
            print("Line " + str(line_no) + ": Invalid – wrong format.")
            invalid_count += 1
            continue

        t_type = parts[0].strip()
        amount_text = parts[1].strip()

        ok, result = validate_transaction(t_type, amount_text, balance)

        if ok:
            
            if t_type == "Deposit":
                balance += result
            else:
                balance -= result
            valid_count += 1
            valid_lines.append(line)
            print("Line " + str(line_no) + ": Valid | Balance: " + str(balance))
        else:
            
            invalid_count += 1
            print("Line " + str(line_no) + ": Invalid – " + result + ".")

    print("Valid: " + str(valid_count) + " | Invalid: " + str(invalid_count)
          + " | Final balance: " + str(balance))

    
    out = open("valid_transactions.txt", "w")
    for v in valid_lines:
        out.write(v + "\n")
    out.close()


main()