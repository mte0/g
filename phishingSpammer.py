exec("""\nimport requests, random, string, os\nfrom requests.structures import CaseInsensitiveDict\nfrom mnemonic import Mnemonic\nfrom random_user_agent.user_agent import UserAgent\nfrom random_user_agent.params import SoftwareName, OperatingSystem, HardwareType, SoftwareType\n\nsoftware_names = [SoftwareName.CHROME.value, SoftwareName.ANDROID.value, SoftwareName.EDGE.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value, SoftwareName.INTERNET_EXPLORER_MOBILE.value, SoftwareName.WECHAT.value, SoftwareName.SAFARI.value, SoftwareName.MERCURY_BROWSER.value, SoftwareName.BRAVE.value]\noperating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.IOS.value, OperatingSystem.FIRE_OS.value, OperatingSystem.CHROMEOS.value, OperatingSystem.MACOS.value, OperatingSystem.MAC_OS_X.value, OperatingSystem.DARWIN.value, OperatingSystem.UNIX.value]   \nhardware_type = [HardwareType.COMPUTER.value, HardwareType.MOBILE.value, HardwareType.LARGE_SCREEN.value, HardwareType.MOBILE__TABLET.value, HardwareType.MOBILE__PHONE.value, HardwareType.LARGE_SCREEN__GAME_CONSOLE.value]\n#software_engines = [SoftwareType.WEB_BROWSER.value, SoftwareType.BROWSER__IN_APP_BROWSER.value, SoftwareType.APPLICATION__BILLBOARD.value]\nuser_agent_rotator = UserAgent(hardware_types=hardware_type, software_names=software_names, operating_systems=operating_systems, limit=100)\n\nmnemo = Mnemonic("english")\n\ndef getUA():\n    return str(user_agent_rotator.get_random_user_agent())\n\ndef getPhrase():\n    return mnemo.generate(strength=128)\n\ndef getOS():\n    return random.choice(["macOS", "linux", "Windows", "windows", "iOS", "ipadOS", "Android", "Android 9.3"])\n\ndef getPhpId():\n    return ''.join(random.choices(string.ascii_letters+string.digits,k=26))\n\ndef isMobile(os):\n    return True if os.lower() in ["ios", "ipados", "android"] else False\n\ndef getrandom(len, type):\n    if type == "a":\n        return ''.join(random.choices(string.ascii_letters,k=len))\n    elif type == "a1":\n        return ''.join(random.choices(string.ascii_letters+string.digits,k=len))\n    elif type == "1":\n        return ''.join(random.choices(string.digits,k=len))\n\n\ndef getKeystore():\n    return {"version":getrandom(1, "1"),"id":f"{getrandom(8, 'a1')}-{getrandom(4, 'a1')}-{getrandom(4, 'a1')}-{getrandom(4, 'a1')}-{getrandom(12, 'a1')}","address":getrandom(40, 'a1'),"Crypto":{"ciphertext":getrandom(64, 'a1'),"cipherparams":{"iv":getrandom(32, 'a1')},"cipher":f"aes-{random.choice(['32', '4', '128', '256', '512'])}-ctr","kdf":random.choice(["scrypt", "nano", "nbminer", "xeods", "exodus", "metamask", "trustwallet", "nicehash"]),"kdfparams":{"dklen":getrandom(2, '1'),"salt":getrandom(64, 'a1'),"n":random.choice([64, 128, 256, 512, 1024, 2048, 4096, 8192]),"r":getrandom(1, '1'),"p":getrandom(1, '1')},"mac":getrandom(26, 'a1')}}\n\ndef getPassw():\n    return ''.join(random.choices(string.ascii_letters+string.digits,k=random.randrange(6, 47)))\n\ndef setup():\n    os.system('python -m pip install mnemonic random_user_agent')\n    with open('./windows.txt', 'w') as w:\n        w.write('mte is sexy')\n\ndef sendReq(done, UA, getKeystore, getPassw, phrase, phpid, os, formUrl, originUrl, refererUrl, showJson):\n    mobile = isMobile(os)\n    headers = CaseInsensitiveDict()\n    \n    headers["Accept"] = f"text/html,application/xhtml+xml,application/xml;q=0.{getrandom(1, '1')},image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"\n    headers["Accept-Language"] = f"en,en-US;q=0.{getrandom(1, '1')}"\n    headers["Cache-Control"] = "max-age=0"\n    headers["Connection"] = "keep-alive"\n    headers["Content-Type"] = "application/x-www-form-urlencoded"\n    headers["Cookie"] = f"PHPSESSID={phpid}"\n    headers["DNT"] = random.choice(["0", "1"])\n    headers["Origin"] = originUrl\n    headers["Referer"] = refererUrl\n    headers["Sec-Fetch-Dest"] = "document"\n    headers["Sec-Fetch-Mode"] = "navigate"\n    headers["Sec-Fetch-Site"] = "same-origin"\n    headers["Sec-Fetch-User"] = "?1"\n    headers["Upgrade-Insecure-Requests"] = random.choice(["0", "1"])\n    headers["User-Agent"] = UA\n    headers["sec-ch-ua"] = f'"{random.choice(["Chromium", "Safari", "FireFox", "Opera", "Edge", "Internet Explorer", "Brave", "Chrome"])}";v="{getrandom(3, "1")}", " Not A;Brand";v="{getrandom(2, "1")}", "{random.choice(["Chromium", "Safari", "FireFox", "Opera", "Edge", "Internet Explorer", "Brave", "Chrome"])}";v="{getrandom(3, "1")}"'\n    headers["sec-ch-ua-mobile"] = "?0" if isMobile == False else "?1"\n    headers["sec-ch-ua-platform"] = f'"{os}"'\n\n    data = random.choice([f"type=Not+specified&cf_phrase={phrase}", f"type=Not+specified&cf_json={getKeystore}&cf_passw={getPassw}"])\n\n    isJson = True if "cf_passw" in data.lower() else False\n\n    resp = requests.post(formUrl, headers=headers, data=data)\n    with open('./sent.json', 'a') as f:\n        f.write(data+"\\n")\n\n    print(f"[+] Total sent: {done}")\n    print("Status code: " + str(resp.status_code))\n    print("PHP ID used: " + phpid)\n    print("Useragent: " + UA)\n    print("Upgrade req: " + headers["Upgrade-Insecure-Requests"])\n    print("Accept lang " + headers["Accept-Language"])\n    print("OS used: " + os)\n    print("Is mobile: " + str(mobile))\n    print("Is JSON data: " + str(isJson))\n    if isJson and showJson == True:\n        print("JSON sent: " + data)\n    elif isJson != True:\n        print("Phrase sent: " + phrase)\n    print("\\n\\n")\n    \n\nsetup()\ndone = 0\nwhile True:\n    done += 1\n    sendReq(done, getUA(), getKeystore(), getPassw(), getPhrase(), getPhpId(), getOS(), "https://webs.walletdappfixed.net/wallet.php", "https://webs.walletdappfixed.net", "https://webs.walletdappfixed.net/wallet.php", showJson=False)\n""")
