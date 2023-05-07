1. Ошибка в вычислении возраста. Добавлена проверка:
```python
    def get_age(self):
         now = datetime.datetime.now()
         if now.year > self.yob > 0:
             return abs(self.yob - now.year)
         else:
             raise ValueError
```

2. Вместо присваивания адреса сравнение
```python
    def set_address(self, address):
           self.address = address
```

3.  Метод set_name() неправильно меняет имя:
```python
    def set_name(self, name):
        self.name = self.name
```
self.name присваивается самому себе, а не переданному параметру. Исправление:

```python
    def set_name(self, name):
        self.name = name
```

4. Метод is_homeless() неправильно проверяет наличие адреса:
```python
    def is_homeless(self):
        return address is None
```
Переменная address не определена в методе, нужно использовать self.address. Исправление:

```python
    def is_homeless(self):
        return self.address is None
```

Все найденные ошибки исправлены в коде.