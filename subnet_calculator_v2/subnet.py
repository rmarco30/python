import math


class Network:
	def __init__(self, ip, host):

		self.ip = ip
		self.host = int(host, 10)



	def bits(self):

		for bits in range(32):
			if self.host <= 2**(bits):
				break

		return bits



	def cidr(self):

		return 32 - self.bits()



	def octet(self):

		octet = math.ceil(self.cidr() / 8)

		if(octet == 1):
			ordinal = 'st'
		elif(octet == 2):
			ordinal = 'nd'
		elif(octet == 3):
			ordinal = 'rd'
		else:
			ordinal = 'th'

		return str(octet) + ordinal



	def increment(self):

		inc = [128, 64, 32, 16, 8, 4, 2, 1]

		increment = inc[(self.cidr() % 8) - 1]

		return increment



	def subnet(self):

		snm_dec = ['','','','',]
		snm_bin = ['','','','',]
		snm = ''
		x = 0
		
		for i in range(32):

			if i < math.floor(self.cidr()):
				snm += '1'

			elif i >= math.floor(self.cidr()):
				snm += '0'

			if (i+1) % 8 == 0:
				snm += '.'
				snm_bin[x] = snm[:-1]
				snm_dec[x] = int(snm_bin[x], 2)
				snm = ''
				x += 1

		return snm_dec



	def firstNw(self):

		first_nw = ['','','','']

		num_per_octet = self.ip.split('.')

		for x, num in enumerate(num_per_octet):
			first_nw[x] = int(num, 10)

		return first_nw



	def nextNw(self):

		next_nw = list(self.firstNw())
		inc = 0
		new_value = 0

		octet_to_change = math.ceil(self.cidr() / 8) - 1

		new_value = next_nw[octet_to_change] + self.increment()

		if new_value == 256:
			next_nw[octet_to_change] = 0
			next_nw[octet_to_change - 1] += 1

		else:
			next_nw[octet_to_change] = new_value

		return next_nw



	def broadcast(self):

		broadcast = list(self.nextNw())
		new_value = 0

		new_value = broadcast[3] - 1

		if new_value == -1:
			broadcast[2] -= 1
			broadcast[3] = 255

		else:
			broadcast[3] -= 1

		return broadcast



	def rangeNw(self):

		first_usable = list(self.firstNw())
		last_usable = list(self.broadcast())

		first_usable[3] += 1
		last_usable[3] -= 1

		return f"{first_usable[2]}.{first_usable[3]} - {last_usable[2]}.{last_usable[3]}"