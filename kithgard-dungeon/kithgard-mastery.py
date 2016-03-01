count = 0
loop:
    count = count + 1
    self.moveUp()
    self.moveRight(3)
    self.moveUp()
    self.moveDown()
    self.moveRight()
    self.say("Friend")
    self.moveRight(2)
    self.moveUp(1)
    self.say(count)
    enemy1 = self.findNearest(self.findEnemies())
    self.attack(enemy1)
    self.moveLeft(4)
    self.moveUp(2)