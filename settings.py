import ConfigParser

def config() :
    load_config()
    load_vars()

# load config file
def load_config() :
    Config = ConfigParser.ConfigParser()
    global cfg
    cfg = {}

    def get_setts_by_section(section) :
        settings = {}
        opts = Config.options(section)
        for o in opts:
            try:
                settings[o] = Config.get(section, o)
                if(settings[o] == -1):
                    DebugPrint("skip: %s" %o)
            except:
                print("exception on setting: %s" %o)
                settings[o] = None
        return settings

    Config.read("panda.config")
    cfg['gen'] = get_setts_by_section("General")
    cfg['web'] = get_setts_by_section("Web")

def load_vars() :
    global keywords, greetings, ty_resp, jokes

    keywords = { 'browse':['browse','open','visit'], 'search':['search','google'], 'define':['define','what'], 'speak':['say','repeat','shout','speak'], 'ty_resp':['thanks','thank'], 'telljoke':['joke','jokes'] }

    greetings = {'long':["Hello, how are you today?", "Hi there, "+cfg['gen']['user_name']], 'short':["Hello", "Hi there", "Greetings"]}

    ty_resp = ["you are welcome", "it's nothing", "it's my pleasure"]

    jokes = ["What is the difference between a large pizza and a professional online poker player? The large pizza can feed a family of four", "I keep hitting \"escape\", but I'm still here.", "Your life"]
