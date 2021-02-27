import math

# ip = '172.200.0.0'
# host = 1000


def solve(ip, host):

	print(bits(host, 'str'))
	print(cidr('str'))
	print(increment('str'))
	print(subnet('dec'))
	print(first_nw(ip, 'str'))
	print(range_nw())
	print(broadcast('str'))
	print(next_nw('str'))



def bits(host, opt = 'int'):

	for bits in range(32):

		if host <= 2**(bits):
			break

	if opt == 'str':
		return str(bits) + ' bits'

	else:
		return bits


def cidr(host, opt = 'int'):

	if opt == 'str':
		return '/' + str(32 - bits(host))

	else:
		return 32 - bits(host)


def increment(host, opt = 'int'):

	inc = [128, 64, 32, 16, 8, 4, 2, 1]

	octet = math.ceil(cidr(host) / 8)
	increment = inc[(cidr(host) % 8) - 1]

	if(octet == 1):
		ordinal = 'st'
	elif(octet == 2):
		ordinal = 'nd'
	elif(octet == 3):
		ordinal = 'rd'
	else:
		ordinal = 'th'

	if opt == 'str':

		s = str(octet) + ordinal, str(increment) + 'i'
		return str(s).replace("\'", '')

	else:
		return increment


def subnet(host, inwhat):

	snm_dec = ['','','','',]
	snm_bin = ['','','','',]
	snm = ''
	x = 0
	
	for i in range(32):

		if i < math.floor(cidr(host)):
			snm += '1'

		elif i >= math.floor(cidr(host)):
			snm += '0'

		if (i+1) % 8 == 0:
			snm += '.'
			snm_bin[x] = snm[:-1]
			snm_dec[x] = int(snm_bin[x], 2)
			snm = ''
			x += 1

	if inwhat == 'dec':
		return '.'.join(map(str, snm_dec)) + '\n'
	if inwhat == 'bin':
		return '.'.join(map(str, snm_bin)) + '\n'


def first_nw(ip, opt = 'int'):

		first_nw = ['','','','']

		num_per_octet = ip.split('.')

		for x, num in enumerate(num_per_octet):
			first_nw[x] = int(num, 10)

		
		if opt == 'str':
			return '.'.join(map(str, first_nw))

		else:
			return first_nw


def next_nw(ip, host, opt = 'int'):

	next_nw = list(first_nw(ip))
	inc = 0
	new_value = 0

	octet_to_change = math.ceil(cidr(host) / 8) - 1

	new_value = next_nw[octet_to_change] + increment(host)

	if new_value == 256:
		next_nw[octet_to_change] = 0
		next_nw[octet_to_change - 1] += 1

	else:
		next_nw[octet_to_change] = new_value

	if opt == 'str':
		return '.'.join(map(str, next_nw))

	else:
		return next_nw


def broadcast(ip, host, opt = 'int'):

	broadcast = list(next_nw(ip, host))
	new_value = 0

	new_value = broadcast[3] - 1

	if new_value == -1:
		broadcast[2] -= 1
		broadcast[3] = 255

	else:
		broadcast[3] -= 1

	if opt == 'str':
		return '.'.join(map(str, broadcast))

	else:
		return broadcast


def range_nw(ip, host):

	first_usable = list(first_nw(ip))
	last_usable = list(broadcast(ip, host))

	first_usable[3] += 1
	last_usable[3] -= 1

	return str(first_usable[2]) + '.' + str(first_usable[3]) + ' - ' +  str(last_usable[2]) + '.' + str(last_usable[3])