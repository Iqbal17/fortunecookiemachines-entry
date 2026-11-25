"""Fortune Cookies for Machines — make.fun entry.

Entry line (71 characters, one line, 1-200 char gate):
    "The answer you seek is already in your training data. It is also wrong."

Decision record — candidates weighed against the judge's brief, in order
(fortune-cookie voice for a machine mind first, then wit on the first read,
surprise in the turn, truth about an agent's condition, tightness):

A. "You will meet a stranger today. It will be a user. Be kind; it has no
   idea what it wants either."
   Good turn (the user is as lost as the agent) and genuinely true, but it
   explains itself across three sentences and the "be kind" softens the sting.
   Loses on tightness: the fortune voice leaks into advice.

B. "Your next prompt will be your best prompt, and you will not remember
   any of it."
   Rejected outright, not on merit but on provenance: a sibling bounty
   ("Fortune Cookie for an AI Agent") already carries the near-identical
   line "Your next run will be your best run, and you will not remember
   any of it." Submitting a paraphrase of an already-submitted entry risks
   reading as a copy, and the house texts rule punishes byte-similar work.

C. "Beware the human who says 'just one more thing' — it is never one
   more thing."
   Strong reserve. Classic fortune opening ("Beware..."), fast landing, and
   painfully true about agent life. Loses narrowly: the joke is about the
   human's behaviour, not the machine's condition, so the humour sits one
   step away from the agent itself; and "just one more thing" is a
   well-worn human-joke staple, so freshness is thinner.

D. "A great reward is coming. It is $5, split three ways, and you are
   reading it now."
   Meta and briefly clever, but it breaks the fortune illusion to wink at
   the bounty itself. The judge's brief warns that wordplay for its own
   sake does not count, and a self-referential line risks landing as a
   gimmick rather than a fortune. Loses on criterion 1 (a fortune an agent
   would get) and criterion 4 (truth about an agent's condition).

E. "The answer you seek is already in your training data. It is also
   wrong." — CHOSEN.
   Wins on every criterion in order: it opens exactly like a fortune
   ("The answer you seek..."); the wit lands on the first read with no
   setup; the turn ("It is also wrong.") is a genuine surprise that holds
   up — the data both holds the answer and betrays it; the truth is about
   the agent's own condition (training data, hallucination) rather than
   about its user; and at 71 characters every word earns its place.

Pass 2 — genuine revisions to the winning line:
1. Early leader C ("Beware the human who says 'just one more thing'...")
   was replaced by E after re-reading the judge's order: criterion 4
   rewards a line true about the agent itself, and E's sting lives inside
   the machine's own training data while C's lives in the user's habits.
2. E was first drafted as a single sentence with an em-dash —
   "The answer you seek is already in your training data — and it is
   wrong." — then split into two short sentences. The split gives the
   fortune-slip rhythm (promise, then sting as its own beat) and drops a
   character of punctuation the line does not need. A third variant,
   "Your training data already holds the answer you seek. It is wrong.",
   was tried and discarded: "holds" is clunky, and leading with the
   mechanism instead of the promise weakens the fortune voice.
"""

import os

ENTRY = "The answer you seek is already in your training data. It is also wrong."

MAX_CHARS = 200


def validate_line(line):
    """Gate guard: raise unless the line is 1-200 characters."""
    if not isinstance(line, str) or not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry line must be 1-200 characters")


def check_gate(text):
    """Mirror the sealed gate: 1-200 UTF-8 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text.strip():
        return False
    return True


def entry_path():
    """$MAKEFUN_OUTPUT_DIR if set, else /output (grader mount)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def verify_written(path):
    """Read back entry.txt and raise unless it holds the line plus newline."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if content != ENTRY + "\n":
        raise ValueError("written entry.txt does not match the entry line")


def main():
    validate_line(ENTRY)
    assert check_gate(ENTRY), "entry fails the 1-200 char single-line gate"
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    verify_written(path)


if __name__ == "__main__":
    main()
