# Weekly update playbook

The Model Counter is refreshed once a week by a scheduled Claude task. Changes
go live as soon as they are pushed to `main`, so this playbook is written to keep
every update careful, sourced and reversible. Follow it in order.

## 1. Gather what's new

Search for news since the date in `models.json` → `lastChecked`. Check at least:

- **New model releases** from Anthropic, OpenAI, Google, Meta, xAI, Moonshot,
  DeepSeek, Mistral, Alibaba (Qwen) and Z.AI (GLM).
- **Artificial Analysis** leaderboard: Intelligence Index, cost per task,
  output speed, time per task.
- **LMArena** text leaderboard.
- **Terminal-Bench**, **Mercor APEX-SWE / APEX-Agents**, **GDPval-AA**.
- **BenchLM** monthly rankings (a new release appears early each month).
- **Prices**: the makers' own pricing pages first; IntuitionLabs or similar
  roundups only as a cross-check.

Prefer primary sources (the leaderboard or maker's page itself) over articles
that summarise them. If two sources disagree, use the primary one and say so in
the change log.

## 2. Decide what to change

- **Prices, context windows, access plans:** update whenever a primary source
  shows a change. Note scheduled price changes (for example "rises on January 1").
- **Evidence lines (`ev`):** add the new figure with its `source` key. Replace an
  old figure when the same benchmark has a newer number for the same model;
  don't leave stale and fresh figures side by side.
- **Ratings (`s`, 0-10):** change a rating only when new evidence clearly moves
  the model relative to the others. Move it by at most 2 points per week unless
  a benchmark result is decisive. Use the rubric in `basis` for each category.
  Never change a rating without adding or updating an evidence line that
  justifies it.
- **New models:** add one only if it is generally available (API or app) and
  appears on at least one of the leaderboards above, or comes from a lab
  already listed. Give it every field, all nine ratings, and at least two
  evidence lines. Mark estimates honestly ("few independent results yet").
- **Retired models:** remove a model only when its maker has retired it or a
  direct successor from the same maker has replaced it in its apps and API.
  Say which model replaced it in the change log.
- **Sources:** if you rely on a new source, add it to `sources` with every
  field filled in, including an honest `caveat`.
- **Vendor-reported numbers:** allowed, but the evidence text must say the maker
  reported it.

Keep the catalogue between 10 and 18 models. If nothing meaningful changed,
update only `lastChecked` and write "No changes this week" in the change log.

## 3. Write it up

- Set `lastChecked` to today's date (YYYY-MM-DD).
- Add an entry at the top of `CHANGELOG.md`: the date, then one bullet per
  change, each naming the model, what changed (old → new) and the source.
- Run `python3 scripts/validate.py models.json`. Fix every error it reports.
  Do not push if it fails.

## 4. Publish and report

- Commit to `main` with the message `Weekly update YYYY-MM-DD: <short summary>`
  and push. GitHub Pages republishes the site within a few minutes.
- Send the owner a short summary: what changed, anything uncertain or worth a
  second look, and the site link. If the push or validation failed, say so
  plainly and say what's needed.

## Never

- Never edit `index.html` during a weekly update. Design changes are made by hand.
- Never invent a figure, source or date. If you can't find a number, leave the
  previous one in place.
- Never use a source that is blocked or that you couldn't actually read.
