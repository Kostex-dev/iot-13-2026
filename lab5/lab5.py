class Flower:
    def __init__(self, name, height, size, color, price, quantity, delivery_rate):
        self.name = name
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.delivery_rate = delivery_rate


class FlowerShop:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)
        print(f"Додано квітку в магазин: {flower.name}")

    def remove_flower(self, name):
        for flower in self.flowers:
            if flower.name == name:
                self.flowers.remove(flower)
                print(f"Квітку '{name}' успішно видалено.")
                return

        print(f"Помилка: квітки '{name}' немає в наявності.")

    def show_top_expensive(self, count=3):
        def get_price(flower):
            return flower.price

        sorted_flowers = sorted(self.flowers, key=get_price, reverse=True)

        print(f"\nТоп-{count} найдорожчих квітів:")
        for i, flower in enumerate(sorted_flowers[:count], 1):
            print(f"{i}. {flower.name} - {flower.price} грн")


class Bouquet:
    def __init__(self):
        self.items = []

    def add_flower(self, flower, count=1):
        self.items.append((flower, count))

    def get_cost(self):
        total_cost = 0
        for flower, count in self.items:
            total_cost += (flower.price + flower.delivery_rate) * count

        return total_cost


if __name__ == "__main__":
    rose = Flower("Троянда", 60, 6, "червоний", 50, 100, 5)
    tulip = Flower("Тюльпан", 40, 5, "жовтий", 25, 200, 3)
    orchid = Flower("Орхідея", 50, 8, "фіолетовий", 120, 20, 10)

    shop = FlowerShop()
    shop.add_flower(rose)
    shop.add_flower(tulip)
    shop.add_flower(orchid)

    shop.show_top_expensive(2)

    print()
    shop.remove_flower("Тюльпан")
    shop.remove_flower("Півонія")

    bouquet = Bouquet()
    bouquet.add_flower(rose, 5)
    bouquet.add_flower(orchid, 1)

    print(f"\nЗагальна вартість букета: {bouquet.get_cost()} грн")
