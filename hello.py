def print_letter_count(name):
    count = sum(1 for ch in name if ch.isalpha())
    print(f"Your name has {count} letters.")


def main():
    name = input("What is your name? ").strip()
    if not name:
        print("Error: name cannot be empty.")
        return 1
    print(f"Hello, {name}!")
    print_letter_count(name)
    print(f"Goodbye, {name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
