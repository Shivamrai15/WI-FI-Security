import re
import time
import Gmail
import asyncio
import requests
import platform
import subprocess
from notifypy import Notify
from threading import Thread
from winsdk.windows.devices.geolocation import Geolocator


def mac_address()->list:
    response = subprocess.check_output(["arp", "-a"]).decode()
    pattern = r"\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}"
    mac_address = re.findall(pattern, response)
    return mac_address


class Device:
    def __init__(self) -> None:
        self.coordinates = None
        self.device_name = None
        self.ip_address = None
        self.isp = None
        self.wifi_name = None

    async def getGPSLocation():
        locator = Geolocator()
        pos = await locator.get_geoposition_async()
        return {
            "latitude": pos.coordinate.latitude,
            "longitude": pos.coordinate.longitude,
        }

    def getGPSCoordinates(self):
        try:
            self.coordinates = asyncio.run(Device.getGPSLocation())
        except PermissionError:
            self.coordinates = {"latitude": None, "longitude": None}

    def getIPAddress(self):
        url = "https://ip-address-tracker-free.p.rapidapi.com/rapidapi/ip"
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "419d81dfdcmsh2f12208b24c1764p1394f9jsnd4b971252d66",
            "X-RapidAPI-Host": "ip-address-tracker-free.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()
        self.ip_address = response.get("ip")
        self.isp = response.get("isp")

    def googleMapLink(self, coordinates: dict) -> str:
        url = f"https://www.google.com/maps/search/?api=1&query={coordinates.get('latitude')},{coordinates.get('longitude')}"
        return url

    def getDeviceName(self):
        self.device_name = platform.node()

    def getWifiName(self):
        response = subprocess.check_output(['netsh', 'wlan', 'show', 'interface']).decode()
        pattern = r"SSID\s+:\s[0-9a-zA-Z ]+"
        result = re.findall(pattern, response)[0]
        wifi_name = result.split(":")
        self.wifi_name = wifi_name[1].strip()

    def getDeviceData(self) -> dict:
        t1 = Thread(target=self.getIPAddress)
        t2 = Thread(target=self.getGPSCoordinates)
        t3 = Thread(target=self.getDeviceName)
        t4 = Thread(target = self.getWifiName)

        t1.start(), t2.start(), t3.start(), t4.start()
        macaddress = mac_address()[0]
        t2.join()
        url = self.googleMapLink(self.coordinates)
        t1.join(), t3.join(), t4.join()

        data = {
            "device_name": self.device_name,
            "ip_address": self.ip_address,
            "mac_address": macaddress,
            "map_url": url,
            "isp": self.isp,
            "wifi_name": self.wifi_name
        }
        return data


async def anonymous_network(verified_mac_address:tuple):
    while True:
        mac =  mac_address()
        if len(mac)!=0:
            if mac[0] not in verified_mac_address:
                return True
        time.sleep(1)
        

def Notificaton():
    notification = Notify()
    notification.application_name  = "Warning"
    notification.icon = "alert.png"
    notification.message = "We have detected unusual network activity from your device. To protect your network, please turn off your Wi-Fi. An email has been sent to Admin"
    notification.title = ""
    notification.send()


if __name__ == "__main__":
    connection = False
    # tuple of verified mac addresses
    verified_mac_addresses = ('d2-20-41-ef-8b-15', "d2-20-41-ef-8b-14")
    while True:
        if connection is False:
            response = asyncio.run(anonymous_network(verified_mac_addresses))
            if response is True:
                connection = True
                credentials = {
                    "sender" : "", # Sender email address
                    "receiver" : "", # Receiver email address
                    "password" : "" # Password
                }
                thread = Thread(target= Notificaton)
                thread.start()
                device_info = Device().getDeviceData()
                Gmail.sendGmail(device_info, credentials)
                thread.join()
        else:
            mac = mac_address()
            if len(mac) == 0:
                connection = False

