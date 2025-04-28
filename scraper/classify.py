def classify_tool(name, desc):
    text = (name + ' ' + desc).lower()
    rules = {
        "Black Hat Tools":    ['exploit','rootkit','zero-day','payload','cobalt','beef','evil'],
        "White Hat Tools":    ['scanner','nmap','masscan','network','vulnerability','openvas'],
        "Grey Hat Tools":     ['fuzzer','bypass','dual-use','proxychains'],
        "Reverse Engineering":['debug','disassemble','ghidra','radare2','binary'],
        "Wireless Hacking":   ['wifi','aircrack','kismet','bluetooth','rfid'],
        "Web Exploitation":   ['xss','csrf','sql','web','burp','zap'],
        "Social Engineering": ['phishing','spoof','social engineering','king phisher'],
        "Malware Analysis":   ['malware','sandbox','forensic','yara','cuckoo'],
        "Password Cracking":  ['hash','crack','hydra','john','hashcat'],
        "OSINT & Recon":      ['osint','recon','shodan','maltego','theharvester'],
    }
    for cat, keywords in rules.items():
        if any(k in text for k in keywords):
            return cat
    return "Miscellaneous"
  
