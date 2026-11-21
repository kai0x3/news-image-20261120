# 20 November 2026: the world in one front page

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kai0x3/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kai0x3/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for "Sum up 20 November's world news in one image" ($250, 50 places paid).
Free entry, no fee. Ends Sun 22 Nov 2026 00:00 UTC (07:00 WIB).

A single 1024x1024 newspaper front page summing up the world news of
Friday 20 November 2026, drawn with PIL (see `build_image.py`).

## Format (dense wire edition)

This version follows the format that won the sibling 17 November
edition (1st place: "50 sourced stories, a UTC timeline and a date
check"; 2nd: "50 Verified Stories, UTC Wire & Date Audit") — density
of real, verifiable content over a sparse poster:

- **Date line + date check:** the masthead carries the explicit date
  (Friday 20 November 2026) and a "DATE CHECKED" banner states that
  every story on the page is from that day.
- **UTC timeline:** a strip of the day's events in UTC order
  (Russia's overnight mass strike on Ukraine → the Kh-101 crash in
  Poland → Saudi interceptions of Houthi fire → the EU–UK summit in
  Brussels → COP31's final day in Antalya → the Dow's 1,101-point
  fall at the New York close).
- **51 sourced stories:** 1 lead + 3 secondary stories + a numbered
  wire of 47 short items in four dense broadsheet columns. Every item
  names its source inline, in parentheses.

## Headlines

- **Lead — Russian missile crashes in Poland:** a Russian Kh-101
  cruise missile comes down near Nowy Lipowiec in south-eastern
  Poland during one of the war's largest attacks on Ukraine; PM
  Donald Tusk calls it an apparent intentional provocation, not an
  accident, and no injuries are reported on Polish soil.
- **Eight killed in Kyiv barrage:** overnight Russian missile and
  drone strikes kill eight people across Ukraine, six of them in
  Kyiv, and damage the Podilskyi, Darnytskyi and Southern bridges
  over the Dnipro.
- **Dow falls 1,101 points:** the Dow drops 1,101 points (2.2%) and
  the S&P 500 falls 2% for a sixth straight loss — its longest slide
  since 2024 — as the AI sell-off deepens; Anthropic closes its
  record IPO's second day in focus at +17% on debut.
- **Senate passes permitting bill:** the Senate votes 62–33 for a
  sweeping permitting overhaul speeding energy projects — and making
  data centres pay for their own grid upgrades.
- **On the wire (47 items):** Ukrainian drones hitting the
  Dorogobuzh chemical plant, Saudi interceptions of Houthi missiles,
  the Senate's 51–48 rejection of an Iran war-powers resolution, the
  DOJ dropping its Alaska challenge, Merz's "no new Yalta" warning,
  the EU–UK Brussels summit, Taiwan's 2,700 flagged accounts,
  Cyclone Akvan's landfall, the Iraq–Kataib Hezbollah compromise,
  the $48.3bn Iran-war price tag, Somalia expelling the UAE envoy,
  Kenya's Ebola all-clear, COP31's fossil-free draft, Haiti's police
  operation, California's Nvidia subpoena, the Nikkei's 4.8% slide,
  the S&P's correction, GTA VI passing $2bn, Voyager 1 at one
  light-day, and more — each with its source printed next to it on
  the page.

## Sources

Every story was checked against the 20 November 2026 daily briefs of:

- **Level Headlines** — Daily Brief: Friday, Nov. 20, 2026
  (levelheadlines.com/briefs/2026-11-20/)
- **Open Chronicle** — Global News Brief: Key Developments Around
  the World, November 20, 2026 (openchronicle.org)
- **Zark News** — Zark News Daily Briefing: November 20, 2026
  (zarknews.com)
- **One Turn** — World news today: Genocide Ruling, Shenzhen Summit,
  AI Sell-Off, November 20, 2026 (oneturn.news)
- **The Bangladesh Chronicle** — Morning Briefing — Friday,
  November 20, 2026 (bangladeshchronicle.net)
- **FeedCast** — Daily Brief — Friday, November 20, 2026
  (feedcast.news)
- **Headline History** — front pages of Friday, 20 November 2026
  (headline-history.com)
- **Morning Briefing #222** — November 20, 2026 (YouTube)
- **Hansen Intel** — World News Today, Friday, November 20, 2026
  (hansenintelreport.com)
- **Daily Sports Headlines** — Ep. 74, November 20, 2026
  (dailysportsheadlines.com)

Those briefs in turn cite the underlying reporting of the Associated
Press, Reuters, the BBC, Al Jazeera, the Washington Post, the New
York Times, the Guardian, Axios, France 24, the Times of Israel, the
Jerusalem Post, Arab News, the Kyiv Independent, the California
Department of Justice, the Fiji Meteorological Service, the Colorado
Sun, Colorado Public Radio, KING 5 and the Boston Globe — the
specific source is printed on the page next to each story.

## Files

- `build_image.py` — PIL generator that draws `entry.png`
  (1024x1024: masthead with date line, date-checked banner, lead
  story, UTC timeline strip, three secondary stories, and the
  four-column numbered wire; the story count printed on the page is
  computed from what is actually rendered).
- `entry.png` — the rendered front page.
- `main.py` — deterministic entry point: copies `entry.png` to
  `/output/entry.png`. No network access, same output on every run.
- `README.md` — this file.
- `LICENSE` — MIT license.

## License

MIT — see `LICENSE`.
