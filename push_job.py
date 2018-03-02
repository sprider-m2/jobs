#!/usr/bin/env python
# encoding: utf-8

"""
@author: m2
@software: PyCharm
@file: push_job.py
@time: 18-3-2 下午3:39
"""

import requests
import pandas as pd
import datetime
import time
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

host = "https://api.neituixiaowangzi.com"

url = "/api/search/jobs?s=%s&l=10&addr_city=全国&cat1=%s"

cats = ["技术", "产品", "运营", "设计", "市场", "销售", "职能"]
for cat in cats:
    d = []
    cur = 0
    try:
        data = requests.get(url=host + url % (cur, cat))

        ret = data.json()

        total = int(ret["total"])
        print("%s total %s" % (cat, total))

        while cur < total:
            print("now is %s" % cur)
            data = requests.get(url=host + url % (cur, cat))
            d.append([datetime.datetime.now(), data.text])
            cur += 10
            time.sleep(0.2)

    except Exception as e:
        print(e)

    finally:

        RET = []
        df = pd.DataFrame(d, columns=["created_at", "data"])

        for index, d in df.iterrows():
            # print(d["data"])
            RET.extend(json.loads(d["data"])["records"])

        df2 = pd.DataFrame.from_dict(RET)
        df2.to_csv("%s.csv" % cat)
        # df.to_csv("%s.csv" % cat)
        # print(data.text)
