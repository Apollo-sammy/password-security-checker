# Password Security Checker

A beginner-friendly Python command-line project for checking whether a password meets five basic requirements.

## Requirements checked
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

The program lists any missing requirements and reports an overall strength of **Weak**, **Medium**, or **Strong**.

## Run the program
1. Install Python 3 from https://www.python.org/ if it is not already installed.
2. Open a terminal in this folder.
3. Run:

```bash
python password_checker.py
```

On some systems, use `python3 password_checker.py`.

## Example
```text
Enter password: hello
--- PASSWORD CHECK RESULTS ---
Requirements to improve:
  [MISSING] At least 8 characters
  [MISSING] At least one uppercase letter (A-Z)
  [MISSING] At least one number (0-9)
  [MISSING] At least one special character (e.g. !, @, #, $)

Overall strength: Weak
```

## How it works
- `check_password()` checks each requirement and collects missing items.
- `any()` checks whether at least one character matches a condition.
- `if` / `elif` / `else` selects the strength rating.
- `main()` handles user input and prints the results.

## Important note
This is an educational demo, not a full password-auditing tool. It does not store or transmit the password. Password strength depends on more than these simple rules; length and unpredictability are especially important.
