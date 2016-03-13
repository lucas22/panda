import ConfigParser

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
