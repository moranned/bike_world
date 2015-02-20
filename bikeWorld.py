__author__ = 'ned'

class Customer(object):
  def __init__(self,name,budget):
    self.name = name
    self.budget = budget

  def purchase(self,bike,margin):
    '''
    customer purchases bike and decrements total cost of purchase from budget
    :return:
    '''

    if self.budget > bike.cost * margin + bike.cost:
      print '\nCongratulations %s, You purchased a %s for $%d' %(self.name,bike.model,(bike.cost * margin + bike.cost))
      print 'You have $%d remaining in your budget\n' %(self.budget - (bike.cost * margin + bike.cost))
    else:
      print '\n%s, you need and additional $%d to purchase a %s bike' %(self.name,((bike.cost * margin + bike.cost) - self.budget),bike.model)

class Part(object):
  def __init__(self,weight,cost):
    self.weight = weight
    self.cost = cost

class Bicycle(Part):
  def __init__(self,model,weight,cost,stock):
    self.model = model
    self.stock = stock
    super(Bicycle,self).__init__(weight,cost)

  def calculate_weight(self,wheel,frame):
    return wheel.weight + frame.weight

  def calculate_cost(self,wheel,frame):
    return wheel.cost + frame.cost

class Wheel(Part):
  def __init__(self,model,weight,cost):
    self.model = model
    super(Wheel,self).__init__(weight,cost)

class Frame(Part):
  def __init__(self,type,weight,cost):
    self.type = type
    super(Frame,self).__init__(weight,cost)

class Shop(object):

  def __init__(self,name,margin,profit):
    self.name = name
    self.margin = margin
    self.profit = profit

  def sell(self,bike,margin):
    '''
    calculate profit by adding margin to production cost and then subtracting production cost
    :param bike object - gives us access price attribute:
    :param customer object - gives us access to budget object:
    :return profit :
    '''

    profit = 0
    profit += (bike.cost * margin)
    return profit