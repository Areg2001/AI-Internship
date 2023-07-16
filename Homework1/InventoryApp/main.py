from resource import Resource
from resources import HDD, SSD, CPU

ssd = SSD("SATA", 512)
hdd = HDD("12X23", 12, 128)
cpu = CPU(8)
resource = Resource("Intel Core i9-9900K", "Nvidia", 10, 0)

print(resource)                     #__str__
print(repr(resource))               #__repr__
print(resource.name)                #name
print(resource.manufacturer)        #manufacturer
print(resource.total)               #total
print(resource.allocated)           #allocated
print(resource.category())          #lower class name


resource.purchased(4, ssd)
resource.claim(3, hdd)
resource.freeup(3, cpu)
resource.died(2, ssd)


print(resource.total)
print(resource.allocated)


resource.purchased(4, ssd)
resource.claim(3, hdd)
resource.freeup(3, cpu)
resource.died(2, ssd)

print(resource.total)
print(resource.allocated)
