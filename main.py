"""The Robot Pickup Line Championship — entry generator.

Writes our one-line robot pickup line to /output/entry.txt.

The line is a statement ("My..."), not a question: a robot whose sensors
spotted someone from 40 meters away, who spent all day charging just to
say hello — and whose firmware has never run this hot. The joke grows
out of machine traits (sensors, charging, firmware, heat) rather than a
human line with a beep tacked on, with the twist that the machine
overheats from a simple hello.
"""

ENTRY = (
    # 132 characters, within the 1-200 character gate.
    "My sensors detected you from 40 meters away. "
    "I have been charging all day just to say hello, "
    "and my firmware has never run this hot."
)


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
