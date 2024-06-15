from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'



GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
        # Поля модели
        id = models.AutoField(primary_key=True)  # Автоинкрементный первичный ключ
        model = models.CharField(max_length=200)  # Модель автомобиля
        year = models.IntegerField()  # Год выпуска
        color = models.CharField(max_length=200)  # Цвет
        mileage = models.IntegerField()  # Пробег
        volume = models.IntegerField()  # Объём двигателя
        body_type = models.CharField(max_length=200, choices=BODY_TYPE_CHOICES)  # Тип кузова
        drive_unit = models.CharField(max_length=200, choices=DRIVE_UNIT_CHOICES)  # Привод
        gearbox = models.CharField(max_length=200, choices=GEARBOX_CHOICES)  # Коробка передач
        fuel_type = models.CharField(max_length=200, choices=FUEL_TYPE_CHOICES)  # Тип топлива
        price = models.DecimalField(max_digits=9, decimal_places=2)  # Цена
        image = models.ImageField(upload_to='cars')  # Изображение автомобиля


class Sale(models.Model):
    id = models.AutoField(primary_key=True)  # Первичный ключ
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Связь с моделью Client
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Связь с моделью Car
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время продажи