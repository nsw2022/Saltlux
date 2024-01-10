class Pikachu:
    def __init__(self, name="그냥 피카츄"):
        self.name = name
        self.health = 100
        self.level = 1
        self.attack_power = 10

    def __repr__(self):
        return "Pika Pika!"

    def attack(self, target=None):
        if target is None:
            print(f"{self.name}는 공격할 상대가 필요해요 ㅜㅜ")
            return

        damage = self.attack_power * self.level
        print(f"{self.name}가 {target.name}를 {damage}의 데미지로 공격했다!")
        target.be_attacked(damage, self)

    def be_attacked(self, damage, attacker):
        self.health -= damage
        print(f"{self.name}는 {damage}의 데미지만큼 {attacker.name}에게 상처를 입었다!")

        if self.health <= 0:
            print(f"{self.name}은 더 이상 싸울 수 없다!")
            self.health = 0

    def heal(self, amount=10):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name}가 체력을 {amount} 만큼 회복했다!")


"""
p1 = Pikachu()
p2 = Pikachu(name="짱짱쎈 피카츄")
p1.attack(p2)
p2.heal()
print(f"{p2.name}의 {p2.health}다.")
p1.be_attacked(200, p2)
"""

yellow_pikachu = Pikachu(
    name="노란색 피카츄",
)
red_pikachu = Pikachu(name="빨간 피카츄")
for i in range(10):
    yellow_pikachu.attack(red_pikachu)
print(yellow_pikachu)
