# Fryskle

Alle dagen in nij Frysk wurd om te rieden. A daily Frisian word puzzle that runs entirely in the browser, made for GitHub Pages.

**Play it at https://iappyx.github.io/fryskle/**, in 4, 5, 6 or 7 letters.

## Files

- `index.html` is the whole game (HTML, CSS and JavaScript in one file).
- `words.js` holds the daily words and allowed guesses for each mode (4, 5, 6 and 7 letters), and settings. It is generated.
- `answers.txt` (5 letters), `answers-4.txt`, `answers-6.txt` and `answers-7.txt` are the daily answers for each mode, one per line.
- `build_words.py` generates `words.js` from the word lists and the answer lists.
- `make_wordlist.py` makes the word lists `wordlist/fy_NL-4.txt` to `-7.txt` from the official Frisian word list.
- `wordlist/` holds that word list, with the Fryske Akademy's `README.txt` and the GPL licence text (`gpl.txt`).
- `og-image.jpg` is the preview image shown when the game is shared (WhatsApp, Telegram, …). Change `preview/og-image.html` and run `bash preview/make_og_image.sh` to remake it.

## Word list

Guesses are checked against the **Foarkarswurdlist**, the official Frisian word
list (version 20160722, 2015 spelling). `wordlist/` holds every word from it
that uses Fryskle's letters (a–z, â, ê, é, ô, û, ú): 2,174 four-letter,
5,394 five-letter, 11,398 six-letter and 18,863 seven-letter words. Proper nouns, abbreviations
and non-standard spellings (such as *achterbân*, where the list prefers
*efterbân*) are left out, so the game teaches the official spelling. The game
only accepts real words as guesses.

To remake the lists, for example after a new version of the official list:

```
python3 make_wordlist.py path/to/fy_NL.dic path/to/fy_NL.aff
python3 build_words.py build --start 2026-09-26
```

The dictionary files must be UTF-8; the Iepen Fryske Stavering project has
converted copies in its `dict/` folder. Keep `--start` the same as before, or
the puzzle numbers and daily words change.

## Modes and answers

Players choose 4, 5, 6 or 7 letters with the buttons under the header; 5 letters
is the default. Each mode has its own daily word, progress and statistics; a link
ending in `#4`, `#6` or `#7` opens that mode directly.

The daily words come from the answer lists: `answers.txt` (5 letters),
`answers-4.txt`, `answers-6.txt` and `answers-7.txt`, one word per line and one line per day.
Each holds all words of its length from the word list, shuffled once, so the
words last for years (4 letters: about 6, 5 letters: almost 15). Every answer is also a valid guess.

- The order is fixed: day 1 is the first line, day 2 the second, and so on.
  Don't shuffle or reorder a list again after launch, or the word for days that
  have already been fixed changes.
- To add words later, only add them at the end of a list, then rebuild.

## Publish on GitHub Pages

1. Create a public repository and push these files to the `main` branch.
2. In the repository, go to Settings, then Pages, and choose "Deploy from a branch" with `main` and `/ (root)`.
3. After a minute the game is live at `https://<username>.github.io/<repository>/`. A custom domain can be set on the same page.

You can also test locally by opening `index.html` directly in a browser.

## How it works

- Everyone gets the same word: the day number since `start` (in Dutch time, Europe/Amsterdam) picks an entry from each mode's answer list. The day number is also the puzzle number when sharing; shared results for 6 and 7 letters name the mode and link to it.
- Progress and statistics are stored in the player's browser (`localStorage`), separately for each mode.
- Help for when you're stuck, in each mode and without any penalty:
  - **Ynspiraasje** suggests three good starting words: words whose different letters are common in the word list, never the day's answer.
  - **Hint** reveals one letter that isn't in place yet. One per day per mode; it stays visible after a reload.
  - **Wurdsiker** only tells how many words still fit all the colours so far (and the hint), without showing them.
- Accents are forgiven. Players can type *fugel* and the game makes it *fûgel*: a typed word is matched to the day's word or another real word that differs only in accents, and shown with the right accents. Colours ignore accents too, so an *a* counts for an *â*. The accented letters (â, ê, é, ô, û, ú) still have their own keyboard row for anyone who wants them. Physical keyboards work too, including dead keys.
- When the game is over, the day's word stays visible below the board, with a link *Wat betsjut it?* that looks it up on [frysker.nl](https://frysker.nl), the Fryske Akademy's online dictionaries. Inflected forms lead to their base word there (*daald* → *dale*).
- Colors are blue (right place), amber (in the word) and grey (not in the word). Blue and amber are easy to tell apart for most people with color blindness. Shared results use 🟦🟨⬜.

## License

Made by **iappyx**.

- **The game code** (`index.html`, `build_words.py`, `make_wordlist.py`) is © 2026 iappyx, released under the [MIT License](LICENSE).
- **The words** in `wordlist/` and `words.js` come from the Foarkarswurdlist, © Fryske Akademy, and are licensed under the [GNU GPL v3](wordlist/gpl.txt); see [wordlist/README.txt](wordlist/README.txt). The game shows this in its help screen.

This project is not affiliated with or endorsed by the Fryske Akademy.
