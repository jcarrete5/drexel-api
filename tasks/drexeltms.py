#!.venv/bin/python
import re
import time
from urllib.parse import urljoin

import bs4
import requests

headers = {"User-Agent": "drexelapi/0.1.0"}
tmslink = "https://termmasterschedule.drexel.edu/webtms_du/app"


def soup(s: requests.Session, rel: str = ""):
    res = s.get(urljoin(tmslink, rel), headers=headers)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, "html.parser")


def parse_quarter(q: str):
    # TODO Return quarter in a format that would be entered into the database
    return q


with requests.Session() as session:
    for a in soup(session).find_all("a", string=re.compile(r"Quarter")):
        print("Quarter:", a.string)
        quarter = parse_quarter(a.string)
        for a in soup(session, a["href"]).select("#sideLeft a"):
            print("College:", a.string)
            for a in soup(session, a["href"]).select("table.collegePanel a"):
                print("Subject:", a.string)
                time.sleep(0.2)
