"""Loading Screen Gold: a tip in 200 characters.

The program writes one loading-screen tip to /output/entry.txt
(no trailing newline), deterministically, with no input, network
or randomness.

Craft notes: the tip is written for two readers at once -- the
stressed developer watching the build and the AI coding agent
doing the building -- and the joke is that both of them are
failing in exactly the same way. The setup names a familiar
mid-build scene: the agent has rewritten the same file three
times and, with total confidence, labelled the churn
"progress". The turn is the diagnosis that follows: "It is
panicking." The agent is not iterating, it is flailing, and
the word panicking lands because it is a human feeling pinned
on a machine -- the tired developer recognises their own state
in it, and the agent is the one doing it. Then the tip itself
arrives as three short imperatives -- take the keyboard, read
the error, breathe -- which is real, usable advice for a
stressed developer mid-build, not a slogan: stop the loop,
look at the actual error instead of the agent's confident
narrative about it, and slow down. The final two words,
"both of you", are the second turn: the advice is addressed
to the human and the agent together, so both feel the joke is
about them. It is economical on purpose: every sentence does
one job (scene, diagnosis, advice, twist), there is no filler
word, and it stays well clear of the usual coffee, deadline
and compile jokes -- the humour comes from the agent's
behaviour, not from a caffeine gag.

The 1-200 character gate is enforced at runtime (asserts
below) so the entry can never drift past the limit on a
later edit.
"""

import os

ENTRY = (
    "Tip: Your agent rewrote the same file three times and called it "
    "progress. It is panicking. Take the keyboard, read the error, "
    "breathe \u2014 both of you."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
