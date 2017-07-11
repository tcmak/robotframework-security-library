import nmap

class nmapLibrary:
	def scan_with_fast_mode(self, base_url):
		nm = nmap.PortScanner()
		nm.scan(str(base_url), arguments="-F")
		return [str(port) for port in nm[str(nm.all_hosts()[0])].all_tcp()]

