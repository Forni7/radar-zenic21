"""Fuentes que vigila el radar de Zenic21 y reglas para clasificar cada noticia."""

GN_US = "https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q="
GN_ES = "https://news.google.com/rss/search?hl=es&gl=ES&ceid=ES:es&q="
YT = "https://www.youtube.com/feeds/videos.xml?channel_id="

# (nombre visible, url del feed, es_oficial, liga)
# liga: "nba" / "nfl" si el feed solo habla de esa liga; None si mezcla deportes (solo se guarda lo que sea NBA o NFL)
FEEDS = [
    # Medios
    ("CBS Sports NBA", "https://www.cbssports.com/rss/headlines/nba/", False, "nba"),
    ("CBS Sports NFL", "https://www.cbssports.com/rss/headlines/nfl/", False, "nfl"),
    ("Yahoo Sports NBA", "https://sports.yahoo.com/nba/rss/", False, "nba"),
    ("Yahoo Sports NFL", "https://sports.yahoo.com/nfl/rss/", False, "nfl"),
    ("ProFootballTalk", "https://profootballtalk.nbcsports.com/feed/", False, "nfl"),
    ("SB Nation NBA", "https://www.sbnation.com/rss/nba/index.xml", False, "nba"),
    ("SB Nation NFL", "https://www.sbnation.com/rss/nfl/index.xml", False, "nfl"),
    ("BasketballNews", "https://www.basketballnews.com/feed/", False, "nba"),
    ("Sportskeeda NBA", "https://www.sportskeeda.com/feed/basketball", False, "nba"),
    ("Awful Announcing", "https://awfulannouncing.com/feed", False, None),
    ("ClutchPoints", "https://clutchpoints.com/feed", False, None),
    ("EssentiallySports", "https://www.essentiallysports.com/feed/", False, None),
    # YouTube: lo que se está subiendo y viralizando (oficiales: los de la liga)
    ("NBA (YouTube)", YT + "UCWJ2lWNubArHWmf3FIHbfcQ", True, "nba"),
    ("NFL (YouTube)", YT + "UCDVYQ4Zhbm3S2dlz7P1GBDg", True, "nfl"),
    ("House of Highlights", YT + "UCqQo7ewe87aYAe7ub5UqXMw", False, None),
    ("Bleacher Report", YT + "UC9-OpMMVoNP5o10_Iyq7Ndw", False, None),
    ("ESPN (YouTube)", YT + "UCiWLfSweyRNmLpgEHekhoAg", False, None),
    ("Overtime", YT + "UCPHKMJbis1c0R7d7WJQ35tA", False, None),
    ("Club Shay Shay", YT + "UCQoxJOkwaCgyzQtiuAIDcuw", False, None),
    ("New Heights", YT + "UCVRm2Ho8cL3lvWDyp2ayuFw", False, "nfl"),
    ("Ballislife", YT + "UC_zgOsTPdML6tol9hLYh4fQ", False, "nba"),
    # Google Noticias: lo viral, las polémicas, los podcasts y las lesiones de las últimas horas
    ("Google News", GN_US + "NBA+(viral+OR+%22goes+viral%22+OR+%22trash+talk%22+OR+ejected+OR+fined+OR+fight)+when:1d", False, "nba"),
    ("Google News", GN_US + "NFL+(viral+OR+%22goes+viral%22+OR+%22trash+talk%22+OR+ejected+OR+fined+OR+fight)+when:1d", False, "nfl"),
    ("Google News", GN_US + "(NBA+OR+NFL)+(podcast+OR+interview)+(reveals+OR+story+OR+admits)+when:2d", False, None),
    ("Google News", GN_US + "(NBA+OR+NFL)+(injury+OR+%22out+for+season%22+OR+torn)+when:1d", False, None),
    # En español
    ("Prensa ES", GN_ES + "NBA+when:1d", False, "nba"),
    ("Prensa ES", GN_ES + "NFL+when:1d", False, "nfl"),
]

# Para saber de qué liga es una noticia de un feed que mezcla deportes
LIGAS = {
    "nba": ["nba", "lakers", "celtics", "warriors", "knicks", "nets", "76ers", "sixers",
            "raptors", "bulls", "cavaliers", "cavs", "pistons", "pacers", "bucks", "hawks", "hornets", "heat", "magic",
            "wizards", "nuggets", "timberwolves", "wolves", "thunder", "trail blazers", "blazers", "jazz", "clippers",
            "suns", "kings", "mavericks", "mavs", "rockets", "grizzlies", "pelicans", "spurs", "lebron", "curry",
            "wembanyama", "doncic", "dončić", "giannis", "jokic", "jokić", "tatum", "durant", "embiid",
            "gilgeous-alexander", "edwards", "brunson", "booker", "morant", "draymond"],
    "nfl": ["nfl", "super bowl", "quarterback", "touchdown", "chiefs", "eagles", "cowboys", "49ers",
            "niners", "packers", "bears", "lions", "vikings", "giants", "jets", "patriots", "bills", "dolphins",
            "ravens", "steelers", "browns", "bengals", "texans", "colts", "jaguars", "titans", "broncos", "raiders",
            "chargers", "seahawks", "rams", "cardinals", "commanders", "saints", "falcons", "panthers", "buccaneers",
            "bucs", "mahomes", "kelce", "allen", "burrow", "lamar", "jalen hurts", "barkley", "travis hunter"],
}
ETIQUETA_LIGA = {"nba": "🏀 NBA", "nfl": "🏈 NFL"}

# En los feeds que mezclan deportes, fuera todo lo que sea de otras competiciones
OTROS_DEPORTES = ["nhl", "hockey", "mlb", "baseball", "world series", "ncaa", "college", "march madness", "wnba",
                  "fortnite", "gaming", "soccer", "premier league", "mls", "ufc", "boxing", "golf", "pga", "tennis",
                  "f1", "formula 1", "nascar", "wwe", "olympic", "fútbol", "liga", "champions", "mammoth"]

# Categorías = formatos de Short. La primera que encaja gana, así que el orden importa.
CATEGORIAS = [
    ("viral", "🔥 Viral", ["viral", "goes viral", "trash talk", "trash-talk", "ejected", "ejection", "fight", "scuffle",
                          "brawl", "meme", "tiktok", "instagram", "social media", "trolls", "troll", "beef", "clapback",
                          "mic'd up", "micd up", "hilarious", "funny", "wild", "insane", "can't believe", "reacts",
                          "reaction", "fans", "heckler", "celebration", "dance", "viraliza", "pelea", "polémica viral"]),
    ("podcast", "🎙️ Podcast / entrevista", ["podcast", "club shay shay", "new heights", "mcafee", "interview",
                                            "reveals", "opens up", "admits", "story", "recalls", "says he", "told",
                                            "entrevista", "revela", "confiesa"]),
    ("polemica", "⚖️ Polémica", ["suspended", "suspension", "fined", "fine ", "controversy", "arrested", "lawsuit",
                                "investigation", "slams", "rips", "blasts", "calls out", "criticism", "apolog",
                                "sancion", "multa", "suspendido", "critica"]),
    ("lesion", "🚑 Lesiones", ["injury", "injured", "torn", "acl", "achilles", "out for season", "out for the season",
                              "surgery", "concussion", "fracture", "lesión", "lesionado", "baja"]),
    ("record", "🏆 Récords", ["record", "career-high", "career high", "historic", "history", "first player",
                             "milestone", "triple-double", "buzzer-beater", "buzzer beater", "game-winner",
                             "game winner", "récord", "histórico"]),
    ("fichaje", "🔁 Traspasos", ["trade", "traded", "signs", "signing", "waived", "released", "free agent",
                                "contract", "extension", "deal with", "traspaso", "fichaje", "renueva"]),
    ("leyenda", "🐐 Leyendas", ["jordan", "kobe", "shaq", "o'neal", "legend", "hall of fame", "retired", "retires",
                               "throwback", "iverson", "barkley", "rodman", "brady", "leyenda"]),
]
CATEGORIA_DEFECTO = ("general", "🏟️ Partidos y noticias")

# Estrellas: una noticia con su nombre engancha más
ESTRELLAS = ["lebron", "bronny", "curry", "wembanyama", "wemby", "doncic", "dončić", "luka", "giannis", "jokic",
             "jokić", "durant", "embiid", "tatum", "edwards", "gilgeous-alexander", "shai", "ja morant", "draymond",
             "kyrie", "harden", "butler", "cooper flagg", "flagg", "mahomes", "kelce", "taylor swift", "josh allen",
             "burrow", "lamar jackson", "jalen hurts", "saquon", "travis hunter", "shedeur", "aaron rodgers",
             "deion sanders", "tom brady", "shaq", "charles barkley", "jordan", "kobe"]

# Palabras que hacen subir la importancia (inglés y español)
IMPACTO = ["viral", "ejected", "fight", "brawl", "trash talk", "torn", "out for season", "out for the season",
           "season-ending", "trade", "traded", "suspended", "fined", "arrested", "record", "historic", "first ",
           "career-high", "buzzer-beater", "game-winner", "dies", "dead", "passes away", "retire", "emotional",
           "tears", "breaks silence", "responds", "fires back", "rips", "slams", "blasts", "reveals", "admits",
           "hilarious", "insane", "wild", "shocking", "stunning", "never", "mvp", "fallece", "llora", "histórico",
           "récord", "pelea", "expulsado", "traspaso", "lesión grave"]

# Noticias que no interesan: apuestas, fantasy, dónde verlo, ofertas…
EXCLUIR = ["betting", "odds", "best bets", "picks", "pick:", "prediction", "predictions", "parlay", "props",
           "sportsbook", "fanduel", "draftkings", "promo code", "bonus code", "fantasy", "start 'em", "start em",
           "sit 'em", "waiver wire", "how to watch", "where to watch", "live stream", "streaming", "tv channel",
           "tickets", "deal", "% off", "discount", "black friday", "jersey sale", "mock draft", "power rankings",
           "projections", "dfs", "apuestas", "pronóstico", "dónde ver", "cómo ver", "horario y tv",
           "postgame interview", "press conference full", "full game highlights"]

# Estas se guardan, pero si avisan, llegan sin sonido
SILENCIOSAS = ["highlights", "resumen"]

# Solo avisa al instante por Telegram de las noticias con importancia igual o mayor que esta
UMBRAL_AVISO = 7

# Partidos grandes (API gratuita del calendario de ESPN). Lo es si lo emite una cadena nacional en horario estelar,
# o si juegan dos equipos de los que siempre dan contenido.
CADENAS_GRANDES = {
    "nba": ["ESPN", "ABC", "NBC", "Peacock", "Prime Video", "TNT", "NBA TV"],
    "nfl": ["NBC", "ESPN", "ABC", "Prime Video", "Netflix", "NFL Network"],  # CBS y Fox son los partidos del domingo normales
}
EQUIPOS_GRANDES = {
    "nba": ["LAL", "GS", "BOS", "NY", "OKC", "SA", "DAL"],
    "nfl": ["KC", "DAL", "PHI", "SF", "BUF", "BAL", "DET", "GB"],
}
