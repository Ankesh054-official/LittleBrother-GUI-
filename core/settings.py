import os, datetime
import requests, json
from core.bssidFinder import bssidFinder
from core.employee_lookup import employee_lookup
from core.google import google
from core.hashDecrypt import hashdecrypt
from core.ipFinder import ipFinder
from core.mailToIP import mailToIP
from core.profilerFunc import profilerFunc
from core.searchAdresse import searchAdresse
from core.searchTwitter import searchTwitter
from core.searchPersonne import searchPersonne
from core.searchInstagram import searchInstagram
from core.searchUserName import searchUserName
from core.searchNumber import searchNumber
from core.searchEmail import SearchEmail
from core.Profiler import Profiler
from core.facebookStalk import facebookStalk
import time

def init(progress, frame1):
    global version
    global monip, monpays, country, countrycode, Region, Regionname
    global pathDatabase, city, zip, timezone, isp, org, query
    global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
    global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
    global Profiler

    version = '0.0.9 beta'

    progress['value'] = 10
    frame1.update_idletasks()
    time.sleep(0.1)

    pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
    pathDatabase = "\\".join(pathDatabase)+"\\Watched"
    monip = requests.get("https://api.ipify.org/").text
    monpays = requests.get("http://ip-api.com/json/"+monip).text
    value = json.loads(monpays)

    progress['value'] = 15
    frame1.update_idletasks()
    time.sleep(0.1)

    country = value['country']
    countrycode = value['countryCode']
    Region = value['region']
    Regionname = value['regionName']
    city = value['city']
    zip = value['zip']
    progress['value'] = 20
    frame1.update_idletasks()
    time.sleep(0.1)

    timezone = value['timezone']
    isp = value['isp']
    org = value['org']
    query = value['query']

    progress['value'] = 30
    frame1.update_idletasks()
    time.sleep(0.1)

    if not os.path.exists(pathDatabase):
        os.mkdir(pathDatabase)
