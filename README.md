# The Model Counter

A catalogue of current AI models that ranks them against what you care about.
Rate nine requirements from 0 to 10 and the list re-sorts to show the best fit.

- `index.html`: the page (design and logic). Edited by hand only.
- `models.json`: every model's ratings, prices, evidence and the sources behind them.
- `CHANGELOG.md`: what changed in each weekly update.
- `UPDATING.md`: the playbook the weekly update follows.
- `scripts/validate.py`: checks `models.json` before anything is published.

Hosted on GitHub Pages. To preview locally, run `python3 -m http.server` in this
folder and open http://localhost:8000. Opening the file directly won't load the
data, because browsers block `fetch` on `file://` pages.
