__author__ = 'ned'

from bikeWorld import Bicycle,Shop,Customer,Wheel,Frame

ANSWERS = ['yes','y']

MODELS = {
  "Trek":Bicycle('Trek',0,0,5),
  "Cannondale":Bicycle('Cannondale',0,0,5),
  "Schwinn":Bicycle('Schwinn',0,0,5),
  "Lemond":Bicycle('Lemond',0,0,5),
  "Huffy":Bicycle('Huffy',0,0,5),
  "Fuji":Bicycle('Fuji',0,0,5)
}

CUSTOMERS = {
  "Ned":Customer('Ned',500),
  "Kara":Customer('Kara',1000),
  "Layla":Customer('Layla',200)
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

SHOP = Shop('Bike World',.2,0)

def show_wheels():
  print '%-15s %s' %('MODEL','PRICE')
  for wheel,object in WHEEL.iteritems():
    print '%-15s %s' %(wheel, object.cost)

def show_frames():
  print '%-15s %s' %('TYPE','PRICE')
  for frame,object in FRAME.iteritems():
    print '%-15s %s' %(frame, object.cost)

def show_customers():
  for customer in CUSTOMERS.keys():
    print customer

def get_inventory():
  print '%-15s %s' %('MODEL','ITEMS REMAINING')
  for model in MODELS.values():
    print '%-15s %d' %(model.model,model.stock)

def main():

  while True:
    print '\nWelcome to %s. We have the following models in stock at our shop:' %SHOP.name
    get_inventory()
    print '\nWe have the following Wheels in stock:'
    show_wheels()
    print '\nWe have the following Frames in stock:'
    show_frames()
    print '\nThe following customers are in the store:'
    show_customers()

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


      if CUSTOMERS[customer].purchase(MODELS[bike],SHOP.margin):
        SHOP.profit += SHOP.sell(MODELS[bike],SHOP.margin)
        MODELS[bike].stock -= 1
        print '\nHey boss, weve made $%d today' %SHOP.profit
      else:
        print '\n%s, you need and additional $%d to purchase a %s bike' %(customer,((MODELS[bike].cost * SHOP.margin + MODELS[bike].cost) - CUSTOMERS[customer].budget),MODELS[bike].model)

      '''
      if CUSTOMERS[customer].budget > (MODELS[bike].cost * SHOP.margin) + MODELS[bike].cost:
        CUSTOMERS[customer].purchase(MODELS[bike],SHOP.margin)
        SHOP.profit += SHOP.sell(MODELS[bike],SHOP.margin)
        MODELS[bike].stock -= 1
        print '\nHey boss, weve made $%d today' %SHOP.profit
      else:
        CUSTOMERS[customer].purchase(MODELS[bike],SHOP.margin)
      '''

if __name__ == '__main__':
  main()