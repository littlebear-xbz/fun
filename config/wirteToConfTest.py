# -- coding: utf-8 --
import ConfigParser
import time

config = ConfigParser.RawConfigParser()

task = {}
task["id"] = 1
task["package"] = "exe"
task["timeout"] = 150
task["dst_filename"] = "1.exe"
task["custom"] = ""
config.add_section("analysis")  # 增加section
config.set("analysis", "id", task["id"])  # 增加option
config.set("analysis", "target", task["dst_filename"])
config.set("analysis", "package", task["package"])
config.set("analysis", "timeout", task["timeout"])
config.set("analysis", "started", time.asctime())
fp = open("analy.conf", "w")
config.write(fp)
