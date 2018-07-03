from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'
weather = get(url).json()
