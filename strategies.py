from hypothesis.strategies import integers


def main() -> None:
    print(integers(min_value=1, max_value=10).filter(lambda x: x % 2 == 0).example())


if __name__ == "__main__":
    main()
