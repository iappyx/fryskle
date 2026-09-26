#!/usr/bin/env python3
"""Make Fryskle's word lists from the official Frisian word list (Foarkarswurdlist).

Usage:
  python3 make_wordlist.py path/to/fy_NL.dic path/to/fy_NL.aff

Writes wordlist/fy_NL-4.txt to -7.txt: every four-, five-, six- and seven-letter
word in the official list, spelled with the letters Fryskle's keyboard has
(a-z and â ê é ô û ú). Left out:
  - proper nouns and abbreviations (anything with a capital letter),
  - non-standard spellings: the list's REP rules name a preferred form for
    these (for example achterbân -> efterbân), so only the preferred form counts.

The word list is (c) Fryske Akademy, licensed under the GNU GPL v3, and so are
the files this script writes; see wordlist/README.txt and wordlist/gpl.txt.
The dictionary files must be UTF-8 (the Iepen Fryske Stavering project has
converted copies in its dict/ folder).
"""
import os
import sys
import unicodedata

LENGTHS = (4, 5, 6, 7)
ALLOWED = set("abcdefghijklmnopqrstuvwxyzâêéôûú")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def read_aff(path):
    pfx, keep, rep = [], None, set()
    for raw in open(path, encoding="utf-8"):
        p = raw.split()
        if not p or p[0].startswith("#"):
            continue
        if p[0] == "KEEPCASE" and len(p) > 1:
            keep = p[1]
        elif p[0] == "PFX" and len(p) >= 4 and not (len(p) == 4 and p[2] in "YN" and p[3].isdigit()):
            pfx.append((p[1], "" if p[2] == "0" else p[2], "" if p[3] == "0" else p[3]))
        elif p[0] == "REP" and len(p) == 3 and p[1].startswith("^") and p[1].endswith("$"):
            rep.add(nfc(p[1][1:-1].replace("_", " ")))   # whole-word non-standard form
    return pfx, keep, rep


def expand_dic(path, pfx, keep):
    lines = open(path, encoding="utf-8").read().splitlines()
    for line in lines[1:]:                               # first line is the word count
        if not line:
            continue
        word, _, flags = line.partition("/")
        flags = flags.split()[0] if flags else ""
        if keep and keep in flags:                       # special casing: not a plain word
            continue
        yield word
        for flag, strip, add in pfx:
            if flag in flags and word.startswith(strip):
                yield add + word[len(strip):]


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    pfx, keep, rep = read_aff(sys.argv[2])
    words = {n: set() for n in LENGTHS}
    for w in expand_dic(sys.argv[1], pfx, keep):
        w = nfc(w)
        if len(w) in words and w == w.lower() and set(w) <= ALLOWED and w not in rep:
            words[len(w)].add(w)
    os.makedirs("wordlist", exist_ok=True)
    for n in LENGTHS:
        out = os.path.join("wordlist", f"fy_NL-{n}.txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(f"# {n}-letter words from the Foarkarswurdlist (version 20160722), made with make_wordlist.py\n")
            f.write("# Word list (c) Fryske Akademy, GNU GPL v3: see wordlist/README.txt and wordlist/gpl.txt\n")
            f.write("\n".join(sorted(words[n])) + "\n")
        print(f"Wrote {out}: {len(words[n])} words")


if __name__ == "__main__":
    main()
