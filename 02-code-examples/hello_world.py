"""First Python program for CSCI E-7."""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to Python Fundamentals."


if __name__ == "__main__":
    student_name = "Muhamad"
    message = greet(student_name)
    print(message)
