flag = self.findFlag()
loop:
    flag = self.findFlag()
    if flag:
        if flag.color is "green":
            self.pickUpFlag(flag)
    if flag:
        if flag.color is "black":
            enemy = self.findNearestEnemy()
            if enemy:
                self.attack(enemy),
            self.pickUpFlag(flag)