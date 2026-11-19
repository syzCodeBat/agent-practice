def main():
    name = input("What is your name? ").strip()
    if not name:
        print("Error: name cannot be empty.")
        return 1
    print(f"Hello, {name}!")
    print(f"Goodbye, {name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
