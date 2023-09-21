import turtle
turtle.speed(100000000)
turtle.up()
turtle.forward(20)
turtle.right(90)
turtle.down()

#Needs to have soemthing like x=100
#turtle.forward(x)

def Amoung_us():
  turtle.forward(100)
  turtle.backward(100)
  turtle.right(90)
  turtle.forward(20)
  
  
  backpack=30
  for thing in range(backpack):
    turtle.forward(1)
    turtle.left(3)
  
  turtle.up()
  turtle.left(90)
  turtle.forward(40)
  turtle.right(90)
  turtle.forward(81)
  turtle.down()
  turtle.right(90)
  turtle.forward(21)
  
  for thing in range(backpack):
    turtle.forward(1)
    turtle.right(3)
  turtle.forward(64)
  turtle.up()
  turtle.right(90)
  turtle.forward(40)
  turtle.left(90)
  turtle.forward(18)
  turtle.down()
  
  
  Head=160
  for another_thing in range(Head):
    turtle.forward(1)
    turtle.right(1)
    
  turtle.right(20)
  turtle.up()
  turtle.forward(121)
  turtle.right(90)
  turtle.forward(111)
  turtle.right(-90)
  turtle.down()
  turtle.forward(30)
  
  def leg():
    Leg=30
    for thing in range(Leg):
      turtle.forward(1)
      turtle.left(3)
    turtle.forward(11)
  
    for thing in range(Leg):
      turtle.forward(1)
      turtle.left(3)
    turtle.forward(30)
  
  leg()
  turtle.right(120)
  turtle.forward(5)
  turtle.right(-30)
  turtle.forward(10)
  turtle.left(30)
  turtle.forward(5)
  turtle.left(-120)
  turtle.forward(30)
  leg()
  turtle.forward(75)
  
  turtle.up()
  turtle.left(90)
  turtle.forward(117)
  turtle.right(90)
  turtle.forward(20)

  
  
  turtle.forward(6)
  turtle.right(90)
  turtle.forward(50)
  turtle.down()
  turtle.right(90)
  turtle.forward(6)
  
  Head_glass=30
  for thing in range(Head_glass):
      turtle.forward(1)
      turtle.left(3)
  turtle.forward(50)
  
  for thing in range(Head_glass):
      turtle.forward(1)
      turtle.left(3)
  
  turtle.forward(6)

  for thing in range(Head_glass):
      turtle.forward(1)
      turtle.left(3)
  turtle.forward(50)
  
  for thing in range(Head_glass):
      turtle.forward(1)
      turtle.left(3)

 
  


Amoung_us()

turtle.up()
turtle.right(90)
turtle.forward(50)

turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(40)
turtle.down()

for arm_length in range(9):
  turtle.forward(arm_length*5) 
  turtle.right(60)
turtle.right(180)
turtle.forward(6)
turtle.left(60)

turtle.forward(8*5)
turtle.left(60)
turtle.forward(7*5)
turtle.left(60)
turtle.forward(6*5)
turtle.left(60)
turtle.forward(5*5)
turtle.left(60)
turtle.forward(4*5)
turtle.left(60)
turtle.forward(3*5)
turtle.left(60)
turtle.forward(2*5)
turtle.left(60)
turtle.forward(1*5)
turtle.left(60)
turtle.forward(6)

turtle.up()
turtle.forward(100)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.down()
Amoung_us()