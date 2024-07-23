from scapy.all import ARP, Ether, srp
import socket

'''

    MUST HAVE NPCAP DOWNLOADED:
    https://npcap.com/#download

'''

def get_local_ip():
    """Get the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external server; doesn't actually send data
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

def scan_network(ip_range):
    """Scan the network for devices and return their IP and MAC addresses."""
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered_list:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def getMacs():
    local_ip = get_local_ip()
    ip_parts = local_ip.split('.')
    network_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"

    # Scan the network
    devices = scan_network(network_range)
    macs = []
    for device in devices:
        macs.append(device['mac'])
    return macs

if __name__ == "__main__":
    print(getMacs())