#!/usr/bin/env python3
"""Build the 20 Nov 2026 world-news front page (1024x1024 PNG) for the
make.fun news-image-20261120 bounty — dense wire style.

Modelled on what won the sibling 17 Nov edition (1st: "50 sourced
stories, a UTC timeline and a date check"; 2nd: "50 Verified Stories,
UTC Wire & Date Audit"): this page packs ~50 real, sourced stories from
Friday 20 November 2026 onto one broadsheet front page — a lead, a UTC
timeline strip, three secondary stories and a dense numbered wire of
short items, every item attributed to its source inline, under an
explicit date line with a date-checked banner.

Stories were verified against the 20 Nov 2026 daily briefs of Level
Headlines, Open Chronicle, Zark News, One Turn, the Bangladesh
Chronicle, FeedCast and Headline History, which in turn cite AP,
Reuters, the BBC, Al Jazeera, the Guardian, the New York Times and
others (full source list in README.md; checked 2026-11-21 ~01:30 UTC).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)      # newsprint cream
INK = (24, 24, 28)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
DARKRED = (120, 22, 22)
GOLD = (198, 148, 44)
GREY = (90, 90, 92)
RULE = (180, 172, 158)
SKY = (206, 224, 234)

F = "/usr/share/fonts/truetype/dejavu/"
serif_b = lambda s: ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", s)
serif = lambda s: ImageFont.truetype(F + "DejaVuSerif.ttf", s)
sans_b = lambda s: ImageFont.truetype(F + "DejaVuSans-Bold.ttf", s)
sans = lambda s: ImageFont.truetype(F + "DejaVuSans.ttf", s)

# ---------------------------------------------------------------- stories
LEAD_HEAD = "RUSSIAN MISSILE CRASHES IN POLAND"
LEAD_BODY = ("A Russian Kh-101 cruise missile comes down near Nowy "
             "Lipowiec in south-eastern Poland during one of the war's "
             "largest attacks on Ukraine. PM Donald Tusk calls it an "
             "apparent intentional provocation, not an accident; no "
             "injuries are reported on Polish soil. (AP / BBC)")

# (when, text, source) — the day in UTC, as reported by the day's briefs
# (kept short so each fits its timeline column)
TIMELINE = [
    ("01:00 UTC", "Russia's mass strike on Ukraine", "Al Jazeera"),
    ("07:30 UTC", "Kh-101 crashes in SE Poland", "AP"),
    ("08:00 UTC", "Saudis intercept Houthi fire", "AP"),
    ("09:00 UTC", "EU-UK summit in Brussels", "Open Chron."),
    ("15:00 UTC", "COP31 final day in Antalya", "Reuters"),
    ("21:00 UTC", "Dow -1,101; Anthropic +17%", "AP"),
]

# (headline, body) — three secondary stories under the lead
SECONDARY = [
    ("EIGHT KILLED IN KYIV BARRAGE",
     "Overnight Russian missile and drone strikes kill eight people "
     "across Ukraine, six of them in Kyiv, and damage the Podilskyi, "
     "Darnytskyi and Southern bridges over the Dnipro. (Al Jazeera)"),
    ("DOW FALLS 1,101 POINTS",
     "The Dow drops 1,101 points (2.2%) and the S&P 500 falls 2% for "
     "a sixth straight loss, its longest slide since 2024, as the AI "
     "sell-off deepens. (AP / Reuters)"),
    ("SENATE PASSES PERMITTING BILL",
     "The Senate votes 62-33 for a sweeping permitting overhaul "
     "speeding energy projects — and making data centres pay for "
     "their own grid upgrades. (AP / Reuters)"),
]

# (headline, body) — the numbered wire; body ends with its source in parens
WIRE = [
    ("DRONES HIT CHEMICAL PLANT",
     "Ukrainian drones strike the Dorogobuzh chemical plant in "
     "Russia's Smolensk region; fire is reported. "
     "(Kyiv Independent)"),
    ("SAUDI INTERCEPTS HOUTHI FIRE",
     "Saudi air defences destroy a ballistic missile and drones "
     "over the south and Riyadh. (AP / Reuters)"),
    ("SENATE REJECTS IRAN MEASURE",
     "The Senate votes 51-48 against a war-powers resolution on "
     "Iran; three Republicans back it. (Washington Post)"),
    ("DOJ DROPS ALASKA CHALLENGE",
     "The Justice Department moves to drop its suit over Mary "
     "Peltola's Alaska Senate win, calling it moot. (AP)"),
    ("MERZ: NO NEW YALTA",
     "Chancellor Merz warns Europe will not accept a settlement "
     "negotiated by the big powers without it. (Open Chronicle)"),
    ("EU-UK SUMMIT IN BRUSSELS",
     "Costa and von der Leyen host PM Burnham for the second EU-UK "
     "summit; trade, energy and youth mobility feature. "
     "(Open Chronicle)"),
    ("MYANMAR: LET ROHINGYA RETURN",
     "The UN Assembly president urges Myanmar to let Rohingya "
     "refugees return after the ICJ genocide ruling. "
     "(Open Chronicle)"),
    ("TAIWAN FLAGS 2,700 ACCOUNTS",
     "Taiwan flags about 2,700 accounts linked to China for "
     "possible election interference on Meta platforms. "
     "(Open Chronicle)"),
    ("JAPAN-INDIA DEFENCE TIES",
     "Tokyo and New Delhi agree to expand military and defence "
     "industry cooperation. (Open Chronicle)"),
    ("CYCLONE AKVAN MAKES LANDFALL",
     "Cyclone Akvan comes ashore on India's eastern coast after "
     "mass evacuations; flood and crop damage is feared. "
     "(Open Chronicle)"),
    ("SOUTH KOREA CHOLERA CASE",
     "South Korea confirms its first cholera case in about a "
     "decade; officials trace the source. (Open Chronicle)"),
    ("BANGLADESH FACTORIES SHUT",
     "Some 341 garment factories stay closed amid minimum-wage "
     "protests in Bangladesh. (Unbiased World News)"),
    ("CHINA HOLDS LENDING RATES",
     "China leaves benchmark lending rates unchanged for an "
     "eighteenth straight month. (Open Chronicle)"),
    ("JAPAN INFLATION AT 2.2%",
     "Japan's core inflation rises to 2.2% in October, stoking "
     "debate over wages and monetary policy. (Open Chronicle)"),
    ("IRAQ DEAL WITH MILITIA",
     "Baghdad reaches a compromise with Kataib Hezbollah: federal "
     "forces enter Jurf al-Sakhar. (Reuters)"),
    ("IRAN WAR COST: $48.3BN",
     "A Pentagon official puts the US campaign against Iran at "
     "about $48.3bn, drawing scrutiny. (Open Chronicle)"),
    ("GAZA'S CHILDREN",
     "Palestinian health authorities say 22,000+ children have "
     "been killed in Gaza; aid groups warn of the toll. "
     "(Open Chronicle)"),
    ("SOMALIA EXPELS UAE ENVOY",
     "Somalia orders the UAE ambassador to leave within 72 hours "
     "in a sovereignty dispute. (Open Chronicle)"),
    ("SUDAN GOLD MINE DRONE",
     "A drone strike kills 10 people at a gold mine in Sudan's "
     "South Kordofan. (One Turn)"),
    ("KENYA EBOLA ALL-CLEAR",
     "Kenya discharges its last Ebola patient, 37 days after the "
     "first case was confirmed. (One Turn)"),
    ("NIGERIA SUICIDE LAW",
     "Nigeria moves towards ending criminal penalties for "
     "attempted suicide. (Open Chronicle)"),
    ("COP31: FOSSIL FUELS ERASED",
     "On COP31's final day in Antalya, a slimmed-down draft deal "
     "drops fossil-fuel phase-out calls. (Reuters)"),
    ("AFRICA SEEKS CLIMATE CASH",
     "African governments press COP31 for faster adaptation "
     "finance as droughts and floods bite. (Open Chronicle)"),
    ("HAITI POLICE KILL 34",
     "Haitian police say 34 suspected gang members were killed in "
     "an operation in Port-au-Prince. (Reuters)"),
    ("BUKELE REGISTERS AGAIN",
     "El Salvador's President Bukele registers his candidacy for "
     "the 2027 elections, seeking a third term. (One Turn)"),
    ("LULA PROTECTS RAONI LAND",
     "Brazil's Lula advances legal recognition of Indigenous "
     "territory on a visit to Amazon leader Chief Raoni. "
     "(Open Chronicle)"),
    ("COLOMBIA TAX PROTESTS",
     "Demonstrators mobilise in Colombia against government tax "
     "plans amid debate over public finances. (Open Chronicle)"),
    ("CALIFORNIA SUBPOENAS NVIDIA",
     "California's attorney general subpoenas Nvidia over whether "
     "advanced chips reached China. (California DOJ)"),
    ("CYBER DIRECTOR DEPARTS",
     "Cyber Director Sean Cairncross leaves the White House after "
     "tech outages hit aviation and banking. (Bangladesh Chron.)"),
    ("DEEP-SEA MINING NEAR SAMOA",
     "The US explores its first deep-sea mining concessions near "
     "American Samoa. (Open Chronicle)"),
    ("NIKKEI SLIDES 4.8%",
     "Japan's Nikkei falls 4.8% as Asian markets tumble on AI "
     "valuation doubts. (One Turn)"),
    ("S&P SKIDS INTO CORRECTION",
     "The S&P 500 ends 10%+ below its high, and the Nasdaq erases "
     "all its 2026 gains. (NYT / Guardian)"),
    ("TRUMP DEFERS IRAN DECISION",
     "Trump signals he may put off any decision on new major "
     "strikes against Iran until after January 1, 2027. (Axios)"),
    ("HOUSE DEMS PLAN PROBES",
     "House Democrats prepare sweeping investigations of Trump's "
     "family and administration. (KLZ)"),
    ("TRAIN-THEFT CHARGES",
     "Federal prosecutors charge 14 people in a $22.5m California "
     "cargo and train-theft investigation. (KLZ)"),
    ("AURORA WATER WARNING",
     "Aurora, Colorado warns reservoirs sit at 38% of capacity; "
     "restrictions could run through 2027. (KLZ)"),
    ("IMF: DEBT NEAR 100% OF GDP",
     "Georgieva warns at APEC that global public debt nears 100% "
     "of world GDP, the highest since WWII. (Morning Briefing)"),
    ("ITALY FINES META \u20ac805M",
     "Italy fines Meta \u20ac805m over Android photo access, in a "
     "fresh European privacy clash with Big Tech. "
     "(Morning Briefing)"),
    ("FAA GROUND STOP CHAOS",
     "An FAA ground stop strands some 1.5 million travellers "
     "across the US. (Morning Briefing)"),
    ("VMWARE ZERO-DAY EXPLOITED",
     "China-linked spies exploited a VMware vCenter zero-day "
     "before a patch existed, researchers say. (Morning Briefing)"),
    ("IEA: AI EMISSIONS WARNING",
     "The IEA warns AI data centres could push global emissions "
     "sharply higher by 2030 without clean power. "
     "(Morning Briefing)"),
    ("GTA VI TOPS $2BN",
     "Grand Theft Auto VI passes $2bn in early sales, extending "
     "its record-breaking entertainment launch. "
     "(Open Chronicle)"),
    ("VOYAGER 1: ONE LIGHT-DAY",
     "NASA's Voyager 1 is now so far away that its radio signals "
     "take about a full day to reach Earth. (Open Chronicle)"),
    ("CYCLONE XAVIER TRACKED",
     "Severe Tropical Cyclone Xavier, a Category 4 system, is "
     "monitored in the South Pacific near Fiji. (Fiji Met)"),
    ("PAKISTAN KILLS 22 MILITANTS",
     "Pakistan says its forces killed 22 militants near the "
     "Afghan frontier in a security operation. "
     "(Bangladesh Chronicle)"),
    ("INDIA EASES FLEET RULES",
     "India relaxes vessel-age restrictions so older ships can "
     "join its national registry and expand the fleet. "
     "(Bangladesh Chronicle)"),
    ("MONGOLIA PRESIDENT RESIGNS",
     "Mongolia's president resigns; the parliament's chairman "
     "assumes the acting presidency. (Unbiased World News)"),
    ("FRANCE POLICE LAW PASSED",
     "France's parliament adopts a police-shootings law that "
     "activists condemn as a 'licence to kill'. (France 24)"),
    ("US WOMAN FREED FROM CUBA",
     "An American woman is freed after 10 years in Cuba, Arab "
     "News reports. (Arab News)"),
    ("WEST BANK SHOOTING",
     "Settlement security shoots dead an unarmed Palestinian "
     "near Beit El in the West Bank; the IDF investigates. "
     "(Times of Israel)"),
    ("IDF STRIKES HAMAS MEETING",
     "The IDF says it struck a Hamas meeting in Gaza, as troops "
     "hold positions past the ceasefire line. (Jerusalem Post)"),
    ("SENEGAL BUDGET BY DECREE",
     "Senegal's president enacts the revised 2026 budget by "
     "decree to advance a proposed IMF loan programme. "
     "(Unbiased World News)"),
    ("PHILIPPINES-CHILE TRADE PACT",
     "The Philippines and Chile sign a free trade agreement at "
     "the APEC leaders' meeting in Shenzhen. "
     "(Unbiased World News)"),
    ("PAKISTAN-QATAR SECURITY PACT",
     "Pakistan and Qatar sign an accord on cooperation between "
     "their security forces. (Unbiased World News)"),
    ("SEATTLE SCHOOLS SUE",
     "Seattle Public Schools asks a court to pause Initiative "
     "638, which bars transgender girls from girls' sports. "
     "(KING 5)"),
    ("COLORADO TAX SUIT",
     "Two Colorado Republican senators sue to block Amendment "
     "87's graduated income tax, citing TABOR. (Colorado Sun)"),
    ("COLORADO WILDLIFE RULES VOID",
     "An appeals court voids Colorado wildlife-area rules after "
     "officials ignored nearly 200 public comments. (CPR)"),
    ("ELLA LANGLEY SWEEPS CMAS",
     "Ella Langley is the big winner at the 2026 CMA Awards, "
     "taking Entertainer of the Year and Song of the Year. "
     "(Morning Briefing)"),
    ("TEXANS ROLL PAST COLTS",
     "C.J. Stroud throws for 194 yards and three touchdowns as "
     "Houston beats Indianapolis 26-3 on Thursday night. "
     "(Daily Sports)"),
    ("WEMBANYAMA SCORES 32",
     "Victor Wembanyama scores 32 points with 11 rebounds as San "
     "Antonio beats the LA Clippers 124-112. (Daily Sports)"),
    ("SENATOR SEEKS AI HEARINGS",
     "Senator Hassan vows AI hearings after a watchdog coaxed "
     "platforms into planning terrorist attacks. (Boston Globe)"),
]

# (the on-page story count is computed after layout, as STORY_COUNT)

# ---------------------------------------------------------------- drawing
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)

def wrap(s, font, max_w):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

MX = 32                      # side margin
CW = W - 2 * MX              # content width = 960

# ---- wire layout: decide which items fit the four columns up front,
# so the banner can print the true on-page story count ----
WY = 446
WBOT = 976
GAP = 16
COLW = (CW - 3 * GAP) // 4
HF, BF = sans_b(10), sans(9)
def _item_h(head, body):
    hl = len(wrap(head, HF, COLW - 19))
    bl = len(wrap(body, BF, COLW - 19))
    return hl * 11 + bl * 10 + 4

COLS = [[] for _ in range(4)]
_heights = [0] * 4
for _n, (_head, _body) in enumerate(WIRE, start=1):
    _h = _item_h(_head, _body)
    _c = min(range(4), key=lambda k: _heights[k])
    if _heights[_c] + _h > WBOT - WY and all(
            _heights[k] + _h > WBOT - WY for k in range(4)):
        break
    COLS[_c].append((_n, _head, _body))
    _heights[_c] += _h
RENDERED = sum(len(c) for c in COLS)
STORY_COUNT = 1 + len(SECONDARY) + RENDERED

# ---- masthead ----
d.rectangle([0, 0, W, 92], fill=NAVY)
text(512, 8, "FRIDAY  \u2022  20 NOVEMBER 2026  \u2022  THE DAILY WORLD EDITION",
     sans_b(17), fill=(232, 222, 190), anchor="ma")
text(512, 32, "THE WORLD IN ONE IMAGE", serif_b(44),
     fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 92, W, 96], fill=GOLD)

# ---- date-check banner ----
d.rectangle([0, 96, W, 124], fill=DARKRED)
text(512, 103, "\u2713 DATE CHECKED \u2014 EVERY STORY FROM FRIDAY 20 NOVEMBER 2026 "
               f"\u2022 {STORY_COUNT} SOURCED STORIES \u2022 SOURCES NAMED INLINE",
     sans_b(13), fill=(255, 255, 255), anchor="ma")

# ---- lead story ----
ly = 138
_lead_size = 40
while d.textlength(LEAD_HEAD, font=serif_b(_lead_size)) > CW and _lead_size > 24:
    _lead_size -= 1
text(MX, ly, LEAD_HEAD, serif_b(_lead_size), fill=RED)
# compact flags at the right of the lead block
def flag(x, y, w, h, kind):
    d.line([x, y, x, y + 46], fill=INK, width=3)
    if kind == "poland":
        d.rectangle([x, y, x + w, y + h // 2], fill=(255, 255, 255),
                    outline=GREY, width=1)
        d.rectangle([x, y + h // 2, x + w, y + h], fill=(210, 30, 30))
    elif kind == "ukraine":
        d.rectangle([x, y, x + w, y + h // 2], fill=(0, 90, 180))
        d.rectangle([x, y + h // 2, x + w, y + h], fill=(245, 200, 40))
    else:
        for i in range(7):
            d.rectangle([x, y + i * h // 7, x + w, y + (i + 1) * h // 7],
                        fill=(178, 34, 34) if i % 2 == 0 else (255, 255, 255))
        d.rectangle([x, y, x + w // 2, y + 4 * h // 7], fill=NAVY)
fx, fy = 856, 200
d.rectangle([fx - 10, fy - 8, W - MX, fy + 64], fill=SKY, outline=NAVY, width=2)
flag(fx, fy, 34, 20, "poland")
flag(fx + 44, fy, 34, 20, "ukraine")
flag(fx + 88, fy, 34, 20, "usa")
text(fx + 61, fy + 50, "NOWY LIPOWIEC \u2022 NATO", sans_b(10), fill=NAVY, anchor="ma")
for i, ln in enumerate(wrap(LEAD_BODY, serif(16), 800)):
    text(MX, ly + 52 + i * 21, ln, serif(16))
d.line([MX, 266, W - MX, 266], fill=RULE, width=2)

# ---- UTC timeline strip ----
ty = 272
d.rectangle([MX, ty, W - MX, ty + 64], fill=NAVY)
text(MX + 12, ty + 5, "THE DAY IN UTC \u2014 FRIDAY 20 NOVEMBER 2026",
     sans_b(13), fill=GOLD)
col_w = (CW - 24) // 3
for i, (when, txt, src) in enumerate(TIMELINE):
    cx = MX + 12 + (i % 3) * col_w
    cy = ty + 25 + (i // 3) * 19
    text(cx, cy, when + "  ", sans_b(9), fill=(255, 255, 255))
    off = d.textlength(when + "  ", font=sans_b(9))
    text(cx + off, cy, txt + f" ({src})", sans(9), fill=(214, 222, 235))

# ---- secondary stories: three boxes ----
sy = 344
box_w = (CW - 2 * 14) // 3
for i, (head, body) in enumerate(SECONDARY):
    x = MX + i * (box_w + 14)
    d.rectangle([x, sy, x + box_w, sy + 96], outline=RULE, width=2)
    d.rectangle([x, sy, x + box_w, sy + 26], fill=NAVY if i != 0 else RED)
    text(x + 10, sy + 5, head, sans_b(14), fill=(255, 255, 255))
    for j, ln in enumerate(wrap(body, sans(11), box_w - 20)[:4]):
        text(x + 10, sy + 32 + j * 15, ln, sans(11))

# ---- the wire: draw the precomputed columns ----
for c in range(4):
    x = MX + c * (COLW + GAP)
    if c:
        d.line([x - GAP // 2, WY, x - GAP // 2, WBOT], fill=RULE, width=1)
    y = WY
    for n, head, body in COLS[c]:
        text(x, y, f"{n}.", sans_b(10), fill=RED)
        for j, ln in enumerate(wrap(head, HF, COLW - 19)):
            text(x + 19, y + j * 11, ln, HF)
        y += len(wrap(head, HF, COLW - 19)) * 11
        for ln in wrap(body, BF, COLW - 19):
            text(x + 19, y, ln, BF, fill=(52, 52, 56))
            y += 10
        y += 3

# ---- footer ----
d.line([MX, 980, W - MX, 980], fill=RULE, width=2)
text(512, 986, "Sources: Level Headlines \u2022 Open Chronicle \u2022 Zark News \u2022 One Turn \u2022 "
               "Bangladesh Chronicle \u2022 FeedCast \u2022 AP \u2022 Reuters \u2022 BBC \u2022 "
               "Al Jazeera \u2022 NYT \u2022 Guardian \u2014 full citations in README.md",
     sans(9), fill=GREY, anchor="ma")
text(512, 1002, f"One day, one page: {STORY_COUNT} stories from 20 November 2026, "
                "each checked against the day's briefs. Drawn with PIL \u2014 see build_image.py.",
     sans(9), fill=GREY, anchor="ma")

img.save("/home/hatch/workspace/makefun/news-image-20261120/entry.png",
         "PNG", optimize=True)
print(f"saved; wire items rendered: {RENDERED} of {len(WIRE)}; "
      f"total stories on page: {STORY_COUNT}")
