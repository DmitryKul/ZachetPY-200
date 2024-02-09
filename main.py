import random
DATABASE = [{'user1' 'password123'}]


class idCounter():

    id_count = 0
    def idCounter(self):
        idCounter.id_count += 1

class Password:

    def check(self, password):
        if not isinstance(password, str):
            raise TypeError('Пароль должен быть типа STR')


class Product:

    def __init__(self, id, name, price, rating):
        self._id = id
        self._name = name
        self.price = price
        self.rating = rating

    @property
    def id(self):
        print('Вызван геттер')
        return self._id

    @property
    def name(self):
        print('Вызван геттер')
        return self._name

    @property
    def price(self):
        print('Вызван геттер')
        return self.price

    @price.setter
    def price(self, value):
        print('Вызван сеттер')
        self.price = value

    @property
    def rating(self):
        print('Вызван геттер')
        return self.rating

    @rating.setter
    def rating(self, value):
        print('Вызван сеттер')
        self.rating = value

class Cart:

    cart_list = []
    def __init__(self):
        self.len = 0
        self.head: Optional[Cart] = None

    def view_cart(self):
        print(cart_list)



    def append_cart(self, value: any):
        """ Добавление элемента в конец связного списка. """
        append_cart = Cart(value)
        if self.head is None:
            self.head = append_cart
        else:
            last_product = self.cart_list[self.len-1]
            self.cart_list(last_product, append_cart)

class User:

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def password1(self):
        pass


if __name__ == '__main__':
    pass