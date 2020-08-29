import geoipgen

print("\033[33m\033[01mRandom IP from (45.9.132.0/22):\033[0m\033[33m "+geoipgen.generate.IP("45.9.132.0/22")+"\033[0m")
print("\033[33m\033[01mAll IP list range from (45.9.132.0/22):\033[0m\033[33m Generate list with "+str(len(geoipgen.generate.rangeIP("45.9.132.0/22")))+" ips\033[0m")

country_code="es"
cidr_es=geoipgen.generate.randomCIDR(country_code)
print("\n\033[36m\033[01mRandom IP from '"+country_code+"':\033[0m\033[36m "+geoipgen.generate.IP(cidr_es)+"\033[0m")
print("\033[36m\033[01mRandom CIDR from '"+country_code+"':\033[0m\033[36m "+cidr_es+"\033[0m")
print("\033[36m\033[01mAll IP list range from random CIDR on '"+country_code+"':\033[0m\033[36m Generate list with "+str(len(geoipgen.generate.rangeIP(cidr_es)))+" ips\033[0m")