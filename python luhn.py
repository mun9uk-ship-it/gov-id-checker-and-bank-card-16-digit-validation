import logging

# ---------- Logging setup ----------

logging.basicConfig(
    filename="luhn_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------- Color codes ----------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "Luhn Card Validator (16 digits)" + RESET)

card = input("Enter the 16 digits please: ")

# Basic validation
if len(card) != 16 or not card.isdigit():
    print(RED + "❌ Please enter exactly 16 digits." + RESET)
    logging.warning(f"Invalid input: {card}")
else:
    # Spaces every 4 digits
    formatted = " ".join([card[i:i+4] for i in range(0, 16, 4)])
    # Masking
    masked = "**** **** **** " + card[-4:]

    print(YELLOW + f"Card entered: {formatted}" + RESET)
    print(YELLOW + f"Masked card: {masked}" + RESET)

    logging.info(f"Card entered: {formatted} (masked: {masked})")

    total = 0
    reverse_digits = card[::-1]

    print(CYAN + "\nStep-by-step Luhn processing:" + RESET)

    for i, d in enumerate(reverse_digits):
        n = int(d)
        original_n = n

        if i % 2 == 1:
            n = n * 2
            if n > 9:
                n -= 9
            print(f"Index {i}: digit {original_n} -> doubled -> adjusted -> {n}")
        else:
            print(f"Index {i}: digit {n} (unchanged)")

        total += n

    print(CYAN + f"\nTotal sum = {total}" + RESET)
    print(CYAN + f"Total % 10 = {total % 10}" + RESET)

    if total % 10 == 0:
        print(GREEN + "✅ Valid card number (Luhn check passed)" + RESET)
        logging.info(f"Valid card: {formatted}")
    else:
        print(RED + "❌ Invalid card number (Luhn check failed)" + RESET)
        logging.info(f"Invalid card: {formatted}")
