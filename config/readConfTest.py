import ConfigParser

config = ConfigParser.ConfigParser()

config.read("./analy.conf")
if config.has_option("analysis", "timeout"):
    print config.get("analysis", "timeout")

print config.sections()
print config.get("analysis", "package")
print config.get("analysis", "id")
if config.has_option("analysis","name"):
    print config.get("analysis","name")

config.read("./2016.conf");
print config.get("url","firstUrl")