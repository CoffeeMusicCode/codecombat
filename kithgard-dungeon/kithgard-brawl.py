loop:
    healReady = self.isReady("heal")
    drainReady = self.isReady("drain-life")
    items = self.findItems()
    throwers = self.findByType("thrower")
    nearest = self.findNearest(throwers)
    if nearest:
        self.attack(nearest)
    enemies = self.findEnemies()
    nearest = self.findNearest(enemies)
    if nearest:
        if healReady:
            self.heal(self)
        elif drainReady:
            self.cast("drain-life", nearest)
        else:
            self.attack(nearest)