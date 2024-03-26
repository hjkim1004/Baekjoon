def get_time(current: list, cook_minute: str) -> str:
    hour, minute = current
    hour = int(hour)
    minute = int(minute)
    cook_minute = int(cook_minute)

    minute += cook_minute
    if minute >= 60:
        hour += minute // 60
        minute = minute % 60

    if hour >= 24:
        hour = hour % 24

    return f"{hour} {minute}"


if __name__ == "__main__":
    print(get_time(input().split(), input()))
