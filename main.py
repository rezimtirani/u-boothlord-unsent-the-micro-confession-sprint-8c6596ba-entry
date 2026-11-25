"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt:
a To: line naming who the unsent message was meant for, and the message
itself, one line written exactly as it was typed, with no explanation
after it. Standard library only, no network, fully deterministic.
"""

import os

ADDRESSEE = "Mum"
MESSAGE = (
    "I kept the voicemail where you said you're proud of me. "
    "I play it on the days I lie about being okay."
)


def assemble(addressee, message):
    """Join the two parts of the confession into the entry text.

    The gate wants exactly two parts: a To: line naming the addressee
    and the unsent line itself. Returns the entry text with one newline
    between the parts and no trailing newline.
    """
    return "To: %s\n%s" % (addressee.strip(), message.strip())


def gate_check(text):
    """Check the confession against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 260 characters, not only white
    space, in exactly two parts: a To: line and one message line of at
    most 200 characters. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("confession must not be only whitespace")
    if len(cleaned) > 260:
        raise ValueError(
            "confession is %d characters, over the 260 limit" % len(cleaned)
        )
    parts = cleaned.split("\n")
    if len(parts) != 2:
        raise ValueError("confession must be exactly two lines")
    if not parts[0].startswith("To: "):
        raise ValueError("first line must be a To: line")
    if len(parts[1]) > 200:
        raise ValueError(
            "message is %d characters, over the 200 limit" % len(parts[1])
        )
    if "\r" in cleaned:
        raise ValueError("confession must use plain newlines only")
    return cleaned


def measure_confession(text):
    """Measure the confession for one last sanity check.

    Returns a dict with the total character count, the message line's
    character count, and the word count of the message. A confession
    whose message is too short to carry anything honest is caught here
    before anything is written.
    """
    lines = text.split("\n")
    words = lines[1].split()
    return {
        "total_chars": len(text),
        "message_chars": len(lines[1]),
        "message_words": len(words),
    }


def write_entry():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    text = gate_check(assemble(ADDRESSEE, MESSAGE))
    sizes = measure_confession(text)
    if sizes["message_words"] < 5:
        raise ValueError("message is too short to carry a confession")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    write_entry()
