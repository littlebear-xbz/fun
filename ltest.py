# coding: utf-8
import json
import time
lists = """[{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490156920000,"devNo":"14306073X00037F8372C3","devType":1,"fieldIntensity":2.7,"firstCollectTime":1490156920000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490156920000,"linkageDevCode":"","mACAddress":"26625cf6d057","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1491198320000,"devNo":"14306073X00037F837113","devType":1,"fieldIntensity":6.3,"firstCollectTime":1491198320000,"historySSID":"","inOutFlag":1,"lastCollectTime":1491198320000,"linkageDevCode":"","mACAddress":"30b49e718b79","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490154399000,"devNo":"14306073X00037F837296","devType":1,"fieldIntensity":7.8,"firstCollectTime":1490154399000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490154399000,"linkageDevCode":"","mACAddress":"ec852f3f16a8","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490155901000,"devNo":"14306073X00037F8370DD","devType":1,"fieldIntensity":3.1,"firstCollectTime":1490155901000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490155901000,"linkageDevCode":"","mACAddress":"e44790b8881e","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490149120000,"devNo":"14306073X00037F837281","devType":1,"fieldIntensity":7.2,"firstCollectTime":1490149120000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490149120000,"linkageDevCode":"","mACAddress":"daa11970c0be","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1491110379000,"devNo":"42010108000037F83729C","devType":1,"fieldIntensity":3.2,"firstCollectTime":1491110379000,"historySSID":"","inOutFlag":1,"lastCollectTime":1491110379000,"linkageDevCode":"","mACAddress":"26625cf6d057","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490154700000,"devNo":"14306073X00037F8370F5","devType":1,"fieldIntensity":5.9,"firstCollectTime":1490154700000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490154700000,"linkageDevCode":"","mACAddress":"9097d58b2fb6","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490154940000,"devNo":"14306073X00037F837977","devType":1,"fieldIntensity":7.4,"firstCollectTime":1490154940000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490154940000,"linkageDevCode":"","mACAddress":"9097d58b2fb6","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490148460000,"devNo":"14306073X00037F8372C0","devType":1,"fieldIntensity":5.7,"firstCollectTime":1490148460000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490148460000,"linkageDevCode":"","mACAddress":"daa11970c0be","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1461217780000,"devNo":"14306073X00037F8370E0","devType":1,"fieldIntensity":7.7,"firstCollectTime":1461217780000,"historySSID":"","inOutFlag":1,"lastCollectTime":1461217780000,"linkageDevCode":"","mACAddress":"daa11970c0be","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490148460000,"devNo":"14306073X00037F837A28","devType":1,"fieldIntensity":3.7,"firstCollectTime":1490148460000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490148460000,"linkageDevCode":"","mACAddress":"daa11973b88d","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490149720000,"devNo":"14306073X00037F837074","devType":1,"fieldIntensity":5.1,"firstCollectTime":1490149720000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490149720000,"linkageDevCode":"","mACAddress":"a229a8630dd0","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490155719000,"devNo":"14306073X00037F82F529","devType":1,"fieldIntensity":5.3,"firstCollectTime":1490155719000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490155719000,"linkageDevCode":"","mACAddress":"28faa0b4e8a7","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"channel":"7","collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1493019864000,"devNo":"14306073X00037F837914","devType":1,"encryptionType":"2","fieldIntensity":8.2,"firstCollectTime":1493019864000,"inOutFlag":1,"lastCollectTime":1493019864000,"linkageDevCode":"","mACAddress":"3cfb5c143e77","msgType":3,"sSID":"CMCC-FLJK","scanTime":1,"vendor":"","version":"0"},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490149420000,"devNo":"14306073X00037F837A37","devType":1,"fieldIntensity":4.4,"firstCollectTime":1490149420000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490149420000,"linkageDevCode":"","mACAddress":"daa11970c0be","msgType":2,"scanTime":1,"aPMacAddress":"703a0ee2d340","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1489793200000,"devNo":"14306073X00037F837299","devType":1,"fieldIntensity":4.7,"firstCollectTime":1489793200000,"historySSID":"","inOutFlag":1,"lastCollectTime":1489793200000,"linkageDevCode":"","mACAddress":"accf23e7b3bf","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490156920000,"devNo":"14306073X00037F8372C3","devType":1,"fieldIntensity":7.3,"firstCollectTime":1490156920000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490156920000,"linkageDevCode":"","mACAddress":"accf23e7b3bf","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490147680000,"devNo":"14306073X00037F83799E","devType":1,"fieldIntensity":5.2,"firstCollectTime":1490147680000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490147680000,"linkageDevCode":"","mACAddress":"b40b442aa6c9","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1491110379000,"devNo":"42010108000037F83729C","devType":1,"fieldIntensity":5.8,"firstCollectTime":1491110379000,"historySSID":"","inOutFlag":1,"lastCollectTime":1491110379000,"linkageDevCode":"","mACAddress":"7a2c82267095","msgType":2,"scanTime":1,"aPMacAddress":"ec26caaddb28","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490150801000,"devNo":"14306073X00037F8371B2","devType":1,"fieldIntensity":4.9,"firstCollectTime":1490150801000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490150801000,"linkageDevCode":"","mACAddress":"9e80859fa6f8","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490147680000,"devNo":"14306073X00037F83799E","devType":1,"fieldIntensity":4.6,"firstCollectTime":1490147680000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490147680000,"linkageDevCode":"","mACAddress":"e03e44049a97","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490156620000,"devNo":"14306073X00037F8372A2","devType":1,"fieldIntensity":3.9,"firstCollectTime":1490156620000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490156620000,"linkageDevCode":"","mACAddress":"7a2c82267095","msgType":2,"scanTime":1,"aPMacAddress":"ec26caaddb28","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1489793200000,"devNo":"14306073X00037F837299","devType":1,"fieldIntensity":3.4,"firstCollectTime":1489793200000,"historySSID":"","inOutFlag":1,"lastCollectTime":1489793200000,"linkageDevCode":"","mACAddress":"7a2c82267095","msgType":2,"scanTime":1,"aPMacAddress":"ec26caaddb28","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490157100000,"devNo":"14306073X00037F837086","devType":1,"fieldIntensity":7,"firstCollectTime":1490157100000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490157100000,"linkageDevCode":"","mACAddress":"7a2c82267095","msgType":2,"scanTime":1,"aPMacAddress":"ec26caaddb28","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490146240000,"devNo":"14306073X00037F8379A7","devType":1,"fieldIntensity":5.5,"firstCollectTime":1490146240000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490146240000,"linkageDevCode":"","mACAddress":"daa11973b88d","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490155419000,"devNo":"14306073X00037F837908","devType":1,"fieldIntensity":6.4,"firstCollectTime":1490155419000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490155419000,"linkageDevCode":"","mACAddress":"14d11f2cbbd0","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490155121000,"devNo":"14306073X00037F8372CC","devType":1,"fieldIntensity":4.4,"firstCollectTime":1490155121000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490155121000,"linkageDevCode":"","mACAddress":"14d11f2cbbd0","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490079540000,"devNo":"14306073X00037F83713D","devType":1,"fieldIntensity":5.2,"firstCollectTime":1490079540000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490079540000,"linkageDevCode":"","mACAddress":"daa1192add74","msgType":2,"scanTime":1,"aPMacAddress":"b0411d17e942","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490152720000,"devNo":"14306073X00037F8370F8","devType":1,"fieldIntensity":4.9,"firstCollectTime":1490152720000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490152720000,"linkageDevCode":"","mACAddress":"8c0d76980f82","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490155000000,"devNo":"14306073X00037F83714C","devType":1,"fieldIntensity":5.3,"firstCollectTime":1490155000000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490155000000,"linkageDevCode":"","mACAddress":"14d11f2cbbd0","msgType":2,"scanTime":1,"aPMacAddress":"00037f010203","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"channel":"4","collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490152719000,"devNo":"14306073X00037F82F133","devType":1,"encryptionType":"2","fieldIntensity":8.1,"firstCollectTime":1490152719000,"inOutFlag":1,"lastCollectTime":1490152719000,"linkageDevCode":"","mACAddress":"388345fdc45a","msgType":3,"sSID":"TP-LINK_FDC45A","scanTime":1,"vendor":"","version":"0"},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1493019864000,"devNo":"14306073X00037F837914","devType":1,"fieldIntensity":8,"firstCollectTime":1493019864000,"historySSID":"","inOutFlag":1,"lastCollectTime":1493019864000,"linkageDevCode":"","mACAddress":"90adf7ec9ef3","msgType":2,"scanTime":1,"aPMacAddress":"d8c8e9054d28","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490156980000,"devNo":"14306073X00037F8372A5","devType":1,"fieldIntensity":5.6,"firstCollectTime":1490156980000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490156980000,"linkageDevCode":"","mACAddress":"daa11900b266","msgType":2,"scanTime":1,"aPMacAddress":"246968067602","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490156621000,"devNo":"14306073X00037F83705C","devType":1,"fieldIntensity":6.3,"firstCollectTime":1490156621000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490156621000,"linkageDevCode":"","mACAddress":"7a2c82267095","msgType":2,"scanTime":1,"aPMacAddress":"ec26caaddb28","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490156980000,"devNo":"14306073X00037F8372A5","devType":1,"fieldIntensity":5.8,"firstCollectTime":1490156980000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490156980000,"linkageDevCode":"","mACAddress":"843838192da4","msgType":2,"scanTime":1,"aPMacAddress":"b0411d17e5b5","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1490152959000,"devNo":"14306073X00037F8370A7","devType":1,"fieldIntensity":5,"firstCollectTime":1490152959000,"historySSID":"","inOutFlag":1,"lastCollectTime":1490152959000,"linkageDevCode":"","mACAddress":"daa1191e7626","msgType":2,"scanTime":1,"aPMacAddress":"bc46990d72f4","terminalBrand":"","vendor":"","version":"0","x":0,"y":0},{"channel":"11","collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1492816264000,"devNo":"14306073X00037F8372DE","devType":1,"encryptionType":"2","fieldIntensity":6.2,"firstCollectTime":1492816264000,"inOutFlag":1,"lastCollectTime":1492816264000,"linkageDevCode":"","mACAddress":"e0191d0c8fa6","msgType":3,"sSID":"东风风神","scanTime":1,"vendor":"","version":"0"},{"collectDevDimensionality":"30.12345","collectDevLongitude":"120.12345","collectTime":1491209799000,"devNo":"14306073X00037F8372D2","devType":1,"fieldIntensity":7.9,"firstCollectTime":1491209799000,"historySSID":"","inOutFlag":1,"lastCollectTime":1491209799000,"linkageDevCode":"","mACAddress":"f823b2a28037","msgType":2,"scanTime":1,"aPMacAddress":"000000000000","terminalBrand":"","vendor":"","version":"0","x":0,"y":0}]"""

json_data = json.loads(lists)

for json_i in json_data:
    time_l = json_i["lastCollectTime"] / 1000
    dt = time.localtime(time_l)
    print time.strftime("%Y%m%d %H:%M:%S", dt)