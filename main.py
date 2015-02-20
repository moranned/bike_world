__author__ = 'ned'

from bikeWorld import Bicycle,Shop,Customer,Wheel,Frame

ANSWERS = ['yes','y']

MODELS = {
  "Trek":Bicycle('Trek',0,0),
  "Cannondale":Bicycle('Cannondale',0,0),
  "Schwinn":Bicycle('Schwinn',0,0),
  "Lemond":Bicycle('Lemond',0,0),
  "Huffy":Bicycle('Huffy',0,0),
  "Fuji":Bicycle('Fuji',0,0)
}

CUSTOMERS = {
  "Ned":Customer('Ned',500),
  "Kara":Customer('Kara',1000),
  "Layla":Customer('Layla',200)
}

INVENTORY = {
  "Trek" : 5,
  "Cannondale" : 5,
  "Schwinn" : 5,
  "Lemond" : 5,
  "Huffy" : 5,
  "Fuji" : 5
}

WHEEL = {
  "BrandX" : Wheel('Brandx',10,25),
  "Shimano" : Wheel('Shimano',5,100),
  "Vuelta" : Wheel('Vuelta',2,200)
}

FRAME = {
  "steel" : Frame('steel',15,300),
  "carbonfiber" : Frame('carbonfiber',10,500),
  "aluminum" : Frame('aluminum',15,150),
  "tin": Frame('tin',20,100)
}

SHOP = Shop('Bike World',INVENTORY,.2,0)

def get_inventory():
  print '%-15s %s' %('MODEL','ITEMS REMAINING')
  for model, count in INVENTORY.iteritems():
    print '%-15s %d' %(model,count)

def main():
  print 'Welcome to %s. We have the following models in stock at our shop:' %SHOP.name
  get_inventory()

  print '\nWe have the following Wheels in stock:'
  print '%-15s %s' %('MODEL','PRICE')
  for wheel,object in WHEEL.iteritems():
    print '%-15s %s' %(wheel, object.cost)

  print '\nWe have the following Frames in stock:'
  print '%-15s %s' %('TYPE','PRICE')
  for frame,object in FRAME.iteritems():
    print '%-15s %s' %(frame, object.cost)

  print '\nThe following customers are in the store:'
  for customer in CUSTOMERS.keys():
    print customer

  while True:
    customer = raw_input('\nHello, I am your automated Sales assistant. What is your name? ')
    continue_purchase = raw_input('Would you like to purchase a bike today? ')
    if continue_purchase.lower() not in ANSWERS:
      break
    else:
      print 'Hello, %s. What Bike, Frame and Wheels would you like to purchase today?' %customer
      bike = raw_input('Bike: ')
      frame = raw_input('Frame: ')
      wheels = raw_input('Wheels: ')

      total_weight = (WHEEL[wheels].weight * 2) + FRAME[frame].weight
      total_cost = (WHEEL[wheels].cost * 2) + FRAME[frame].cost
      MODELS[bike].weight = total_weight
      MODELS[bike].cost = total_cost

      if CUSTOMERS[customer].budget > (MODELS[bike].cost * SHOP.margin) + MODELS[bike].cost:
        CUSTOMERS[customer].purchase(MODELS[bike],SHOP.margin)
        SHOP.profit += SHOP.sell(MODELS[bike],SHOP.margin)
        INVENTORY[bike] -= 1
        print 'We now have the following models in stock at our shop:'
        get_inventory()
        print '\nHey boss, weve made $%d today' %SHOP.profit
      else:
        CUSTOMERS[customer].purchase(MODELS[bike],SHOP.margin)

if __name__ == '__main__':
  main()