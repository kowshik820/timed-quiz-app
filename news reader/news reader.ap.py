import urllib.request
from html.parser import HTMLParser
from datetime import datetime

class BBCNewsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_headline = False
        self.headlines = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "h3" and "gs-c-promo-heading__title" in classes:
            self.in_headline = True

    def handle_endtag(self, tag):
        if tag == "h3":
            self.in_headline = False

    def handle_data(self, data):
        if self.in_headline:
            self.headlines.append(data.strip())

def fetch_news():
    try:
        url = "https://www.bbc.com/news"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read().decode()

        parser = BBCNewsParser()
        parser.feed(html)

        cricket_news = []
        politics_news = []
        general_news = []

        # Categorize headlines
        for title in parser.headlines:
            lowered = title.lower()
            if "cricket" in lowered:
                cricket_news.append(title)
            elif "politics" in lowered or "election" in lowered or "government" in lowered:
                politics_news.append(title)
            else:
                general_news.append(title)

        # 🔽 Manually inserted custom news items 🔽

        # Cricket news
        cricket_news.insert(0, "The Blaze exact revenge on Thunder with dominant chase\nGeorgia Elwiss' fifty was followed by Katherine Bryce's 49 to knock off 170 with seven wickets to spare")

        # Political news
        politics_news.insert(0, 
            "Splits in key political parties Shiv Sena and NCP have made the battle for the 48 Lok Sabha seats in Maharashtra more interesting, "
            "besides the focus on traditional issues like unemployment and farmer suicides. Lok Sabha polls in Maharashtra will be held in five phases on "
            "April 19, April 26, May 7, May 13 and May 20. Counting of votes will be held on June 4."
        )

        # --- Display Section ---
        print("\n" + "═" * 60)
        print("🗓️  DATE & TIME:", datetime.now().strftime("%d-%m-%Y  %I:%M %p"))
        print("═" * 60)

        print("\n✨ HIGHLIGHT:")
        print("🎯  Mumbai Indians enters to Qualifier 2 facing with Punjab\n")

        print("🏏 CRICKET NEWS:")
        if cricket_news:
            for i, headline in enumerate(cricket_news[:5], start=1):
                print(f"  {i}. {headline}")
        else:
            print("  - No latest cricket news found!")

        print("\n🏛 POLITICS NEWS:")
        if politics_news:
            for i, headline in enumerate(politics_news[:5], start=1):
                print(f"  {i}. {headline}")
        else:
            print("  - No latest politics news found!")

        print("\n📰 OTHER NEWS:")
        if general_news:
            for i, headline in enumerate(general_news[:5], start=1):
                print(f"  {i}. {headline}")
        else:
            print("  - No general news found!")

        print("\n📢 RANDOM ADDED NEWS (Sample Only):")
        print("  ✔️ ISRO plans to launch Chandrayaan-4 by next year.")
        print("  ✔️ India to host the Global AI Conference 2025.")
        print("  ✔️ Petrol prices to be revised across states this week.")

        print("\n" + "═" * 60)

    except Exception as e:
        print("\n❌ ERROR while fetching news:", e)

# Run the program
fetch_news()