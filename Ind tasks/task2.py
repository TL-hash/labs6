#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def user_profile(name, *interests, **details):
    parts = [f"Имя: {name}"]

    if interests:
        parts.append(f"Интересы: {', '.join(interests)}")
    else:
        parts.append("Интересы не указаны")

    if details:
        details_str = ', '.join(f"{k}: {v}" for k, v in details.items())
        parts.append(f"Дополнительная информация: {details_str}")

    return ", ".join(parts)


if __name__ == "__main__":
    result = user_profile("Alice", "music", "travel", city="Paris", age=25)
    print(result)