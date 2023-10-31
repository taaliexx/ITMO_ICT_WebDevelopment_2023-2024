## Основная страница до авторизации пользователя
```html title="index.py"
{% load static %}
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Natasha's Hotel</title>
    <style>
        /* Общие стили для страницы */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }


        /* Стили для заголовка */
        h1 {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;
            text-align: center;

        }

        /* Стили для описания */
        p {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;;
            text-align: center;
            max-width: 80%; /* Установите желаемую максимальную ширину для текста */
            margin: 0 auto; /* Чтобы выровнять текст по центру */
        }

        /* Стили для меню-ссылки */
        .menu-link {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;
            background-color: #333;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            text-align: center;
            display: inline-block;
            margin-top: 20px;
            border: 2px solid #fff;
        }

        /* Стили для изображения */
        .hotel-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1; /* Помещаем изображение под основным контентом */
            opacity: 0.2; /* Устанавливаем прозрачность */
        }
    </style>
</head>
<body>
    <img src="{% static 'img.png' %}" alt="Hotel Image" class="hotel-image">
    <h1>{{ hotel_info.name }}</h1>
    <p>{{ hotel_info.description }}</p>
    <a href="{% url 'account_login' %}" class="menu-link">Log in to explore our rooms and reviews</a>
</body>
</html>
```

## Основная страница для авторизированного пользователя
```html title="home.html"
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
    <style>
        /* Общие стили для страницы */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        /* Стили для заголовка */
        h2 {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;
            text-align: center;
        }

        /* Стили для меню-ссылок */
        li {
            list-style: none;
            margin: 10px 0;
        }

        a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #333;
            color: #f4f4f4;
            text-decoration: none;
            border: 2px solid #fff; /* Обводка вокруг ссылок */
            border-radius: 5px;
            text-align: center;
        }

        a:hover {
            background-color: #555;
        }

        /* Стили для изображения */
        .hotel-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1; /* Помещаем изображение под основным контентом */
            opacity: 0.2; /* Устанавливаем прозрачность */
        }
        /* CSS для сообщений */
        .messages {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            max-width: 400px; /* Задайте желаемую максимальную ширину */
            background-color: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            transition: top 0.3s ease;
            display: none; /* Начнем с скрытым блоком сообщений */
        }

        .messages.show {
            display: block; /* Показывает сообщения при добавлении класса "show" */
        }
    </style>
</head>
<body>
    {% if messages %}
        <ul class="messages">
            {% for message in messages %}
                <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    <img src="{% static 'img.png' %}" alt="Hotel Image" class="hotel-image">
    <h2>Welcome {{user.first_name}} {{user.last_name}}</h2>
    <li><a href="{% url 'hotel:RoomListView' %}">View Room List</a></li>
    <li><a href="{% url 'hotel:review_list' %}">Reviews</a></li>
    <li><a href="{% url 'hotel:add_review' %}">Add Review</a></li>
    <li><a href="{% url 'hotel:BookingsListView' %}">Manage Bookings</a></li>
    <li><a href="{% url 'account_logout' %}">Log out</a></li>

    <script>
        // JavaScript код
        document.addEventListener('DOMContentLoaded', function() {
            const messages = document.querySelector('.messages');

            // Показать сообщения
            function showMessages() {
                messages.classList.add('show');
            }

            // Скрыть сообщения
            function hideMessages() {
                messages.classList.remove('show');
            }

            // Показать сообщения при загрузке страницы (если они есть)
            if (messages) {
                showMessages();

                // Закрыть сообщения через некоторое время (например, через 5 секунд)
                setTimeout(hideMessages, 5000);
            }
        });
    </script>
</body>
</html>
```
## Список категорий номеров отеля
```html title="room_list_view.html"
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Natasha's Hotel</title>
    <style>
        /* Общие стили для страницы */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        /* Стили для заголовка */
        #brand {
            font-family: Montserrat, sans-serif;
            color: #333;
            text-align: center;
        }

        /* Стили для внутреннего содержания */
        /* Стили для кнопки Home */
        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #fff;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
        }

        .home a:hover {
            background-color: #555;
        }

        .content {
            font-family: Montserrat, sans-serif;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        /* Стили для комнат */
        .room {
            font-family: Montserrat, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 18%; /* Устанавливаем ширину комнаты */
            float: left; /* Выравниваем комнаты влево */
        }

        .room a {
            font-family: Montserrat, sans-serif;
            color: #333;
            text-decoration: none;
        }

        /* Стили для заголовка комнаты */
        .room h2 {
            font-family: Montserrat, sans-serif;
            font-size: 24px;
        }

        /* Стили для изображения комнаты */
        .room img {
            width: 100%; /* Заполнение изображения внутри блока .room */
            max-height: 120px; /* Ограничение максимальной высоты изображения */
            border-radius: 5px;
        }
        /* CSS для сообщений */
        .messages {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            max-width: 400px; /* Задайте желаемую максимальную ширину */
            background-color: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            transition: top 0.3s ease;
            display: none; /* Начнем с скрытым блоком сообщений */
        }

        .messages.show {
            display: block; /* Показывает сообщения при добавлении класса "show" */
        }
    </style>
</head>
<body>
    {% if messages %}
        <ul class="messages">
            {% for message in messages %}
                <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    <!-- Brand -->
    <h1 id="brand">Natasha's Hotel</h1>

    <!-- Main Content -->
    <div class="home">
                <!-- Div 1: Back to Home -->
        <div class="home">
            <a href="{% url 'hotel:HomeView' %}">Home</a>
        </div>

    </div>
    <div class="content">
        {% for room_category, room_url in room_list %}
        <div class="room">
            <a href="{{room_url}}">
                <h2>{{room_category}}</h2>
                {% if room_category == "Single Room" %}
                    <img src="{% static 'single.png' %}" alt="{{room_category}}">
                {% elif room_category == "Double Room" %}
                    <img src="{% static 'double.png' %}" alt="{{room_category}}">
                {% elif room_category == "Deluxe Room" %}
                    <img src="{% static 'deluxe.png' %}" alt="{{room_category}}">
                {% elif room_category == "Family Room" %}
                    <img src="{% static 'family.png' %}" alt="{{room_category}}">
                {% elif room_category == "Suite" %}
                    <img src="{% static 'suite.png' %}" alt="{{room_category}}">
                {% endif %}
            </a>
        </div>
        {% endfor %}
    </div>

    <script>
        // JavaScript код
        document.addEventListener('DOMContentLoaded', function() {
            const messages = document.querySelector('.messages');

            // Показать сообщения
            function showMessages() {
                messages.classList.add('show');
            }

            // Скрыть сообщения
            function hideMessages() {
                messages.classList.remove('show');
            }

            // Показать сообщения при загрузке страницы (если они есть)
            if (messages) {
                showMessages();

                // Закрыть сообщения через некоторое время (например, через 5 секунд)
                setTimeout(hideMessages, 5000);
            }
        });
    </script>
</body>
</html>
```

## Детальное описание категории номера и его бронирование
```html title="room_detail_view.py"
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Room Detail</title>
    <script src="https://kit.fontawesome.com/692189991f.js" crossorigin="anonymous"></script>
    <style>
        /* Ваши стили */
        /* Стили для общей страницы */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        /* Стили для комнаты */
        .room {
            font-family: Montserrat, sans-serif;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 60%;
            margin: 20px;
            padding: 20px;
            text-align: center;
        }

        /* Стили для ссылки "Home" */
        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #fff;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
        }

        .home a:hover {
            background-color: #555;
        }

        /* Стили для информации о комнате */
        .room-info {
            font-family: Montserrat, sans-serif;
        }

        .room-info h1 {
            font-size: 24px;
        }

        .room-info h3 {
            font-size: 20px;
        }

        .room-info img {
            max-width: 55%; /* Максимальная ширина для изображения */
        }

        /* Стили для формы бронирования */
        #booking-form {
            font-family: Montserrat, sans-serif;
            display: flex;
            flex-direction: column;
        }

        .input-div {
            font-family: Montserrat, sans-serif;
            margin: 10px 0;
        }

        label {
            font-family: Montserrat, sans-serif;
        }

        input[type="datetime-local"] {
            font-family: Montserrat, sans-serif;
            padding: 10px;
        }

        button[type="submit"] {
            font-family: Montserrat, sans-serif;
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #555;
        }
    </style>
</head>

<body>
    {% if messages %}
        <ul class="messages">
            {% for message in messages %}
                <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    <!-- Room Details -->
    <div class="room">
        <!-- Div 1: Back to Home -->
        <div class="home">
            <div class="home">
                <a href="{% url 'hotel:RoomListView' %}">Home</i></a>
            </div>
        </div>
        <!-- Div 2: Room Information -->
        <div class="room-info">
            <h1>{{ room_category }}</h1>
            {% if room_category == "Single Room" %}
                <img src="{% static 'single.png' %}" alt="{{room_category}}">
            {% elif room_category == "Double Room" %}
                <img src="{% static 'double.png' %}" alt="{{room_category}}">
            {% elif room_category == "Deluxe Room" %}
                <img src="{% static 'deluxe.png' %}" alt="{{room_category}}">
            {% elif room_category == "Family Room" %}
                <img src="{% static 'family.png' %}" alt="{{room_category}}">
            {% elif room_category == "Suite" %}
                <img src="{% static 'suite.png' %}" alt="{{room_category}}">
            {% endif %}
            <p>{{ room_amenities }}</p>
            <h3>{{ room_price }} $</h3>
        </div>

        <!-- Div 3: Room Booking Form -->
        <form id="booking-form" action="" method="POST">
            {% csrf_token %}
            <!-- Check In Field -->
            <div class="input-div">
                <label for="{{ form.check_in.id_for_label }}" style="font-family: Montserrat, sans-serif;">{{ form.check_in.label_tag }}</label>
                <input type="datetime-local" id="{{ form.check_in.id_for_label }}" name="{{ form.check_in.name }}" style="font-family: Montserrat, sans-serif;">
            </div>

            <!-- Check Out Field -->
            <div class="input-div">
                <label for="{{ form.check_out.id_for_label }}" style="font-family: Montserrat, sans-serif;">{{ form.check_out.label_tag }}</label>
                <input type="datetime-local" id="{{ form.check_out.id_for_label }}" name="{{ form.check_out.name }}" style="font-family: Montserrat, sans-serif;">
            </div>

            <!-- Input Div -->
            <div class="input-div">
                <button type="submit">Book the Room</button>
            </div>
        </form>

    </div> <!-- END Room Div -->
</body>

</html>
```

## Отзывы
```html title="review_list.html"
<!DOCTYPE html>
<html>
<head>
    <title>Reviews</title>

    <style>
        /* Add your custom styles here */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100vh;
            color: #333
        }

        .content {
            width: 80%;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .reviews {
            width: 80%;
        }

        .reviews h1 {
            font-family: Montserrat, sans-serif;
            text-align: center;
            margin-top: 20px;
        }

        .review {
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 10px 0;
            width: 100%; /* Review container takes the full width */
        }

        .user-name {
            font-weight: bold;
            font-size: 18px;
        }

        .user-rating {
            font-size: 16px;
        }

        .user-room {
            font-size: 16px;
        }

        .check-in {
            font-size: 16px;
        }

        .check-out {
            font-size: 16px;
        }

        .user-review {
            font-size: 16px;
        }

        .review-divider {
            border-bottom: 1px solid #ccc;
            margin: 20px 0;
        }

        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #fff;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-right: 10px;
        }

        .home a:hover {
            background-color: #555;
        }
    </style>

</head>
<body>
    <div class="content">
        <div class="reviews">
            <h1>Reviews</h1>
            {% for review in reviews %}
                <div class="review">
                    <p class="user-name">User: {{ review.user }}</p>
                    <p class="user-rating">Rating: {{ review.rating }}/10</p>
                    <p class="user-room">Room: {{ review.room }}</p>
                    <p class="check-in">Check-In Date: {{ review.booking.check_in }}</p>
                    <p class="check-out">Check-Out Date: {{ review.booking.check_out }}</p>
                    <div class="user-review">
                        <p>Review: {{ review.text }}</p>
                    </div>
                </div>
                <p class="review-divider"></p> <!-- Добавляем разделитель между отзывами -->
            {% endfor %}
        </div>
        <div class="home">
            <a href="{% url 'hotel:HomeView' %}">Home</a>
        </div>
    </div>
</body>

</html>
```

## Добавление отзыва
```html title="add_review.html"
{% load static %}
<html>
<head>
    <title>Add Review</title>

     <style>
    /* Ваши стили здесь */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        /* Стили для контейнера с формой */
        .container {
            font-family: Montserrat, sans-serif;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 60%;
            margin: 20px;
            padding: 20px;
            text-align: center;
        }

        .input-div, select, input[type="text"] {
            font-family: Montserrat, sans-serif;
            margin: 10px 0;
            color: #333
        }

        /* Стили для кнопки Home */
        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #fff;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-right: 10px; /* Добавьте отступ справа, например, 10px */
        }

        .home a:hover {
            background-color: #555;
        }

        h2 {
            font-family: Montserrat, sans-serif;
            color: #333
        }

        form {
            font-family: Montserrat, sans-serif;
            display: flex;
            flex-direction: column;
            color: #333
        }

        /* Стили для кнопки */
        button[type="submit"] {
            font-family: Montserrat, sans-serif;
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #555;
        }
    </style>


</head>
<body>
    <div class="container">
        <div class="home">
            <a href="{% url 'hotel:HomeView' %}">Home</a>
        </div>
        <h2>Add Review</h2>
        <form method="post">
            {% csrf_token %}

            <div class="input-div">
                <label for="{{ form.rating.id_for_label }}">Rating:</label>
                {{ form.rating }}
            </div>

            <div class="input-div">
                <label for="{{ form.text.id_for_label }}" style="font-family: Montserrat, sans-serif; color: #333;">Review Text:</label>
                {{ form.text }}
            </div>

            <div class="input-div">
                <label for="{{ form.room.id_for_label }}">Room:</label>
                {{ form.room }}
            </div>

            <div class="input-div">
                <label for="{{ form.booking.id_for_label }}">Booking:</label>
                {{ form.booking }}
            </div>

            <div class="submit">
                <button type="submit">Send Review</button>
            </div>
        </form>
    </div>
</body>
</html>
```

## Управление своими бронированиями 
```html title="bookings_list.html"
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking List</title>

    <style>

        *{
            padding:0;
            margin:0;
            box-sizing: border-box;
        }
        body{
            font-family: Montserrat, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .content{
            display: flex;
            flex-direction: column;
        }

        /* Стили для заголовка "Your Bookings" */
        .headings h1 {
            font-family: Montserrat, sans-serif;
            font-size: 24px;
            text-align: center;
            color: #333;
        }

        /* Стили для "Welcome {{user}}" */
        .headings h2 {
            font-family: Montserrat, sans-serif;
            font-size: 18px;
            text-align: center;
            color: #333;

        }

        /* Стили для кнопки Home */
        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
        }

        .home a:hover {
            background-color: #555;
        }

        .bookings{
            margin-top: 2rem;
            flex:1;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: space-evenly;
        }

        .booking{
            font-family: Montserrat, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 18%; /* Устанавливаем ширину комнаты */
            float: left; /* Выравниваем комнаты влево */
<!--            flex-grow: 1; /* Позволяет блоку расти по высоте */-->
<!--            flex-direction: column;-->

        }


        .category img {
            max-width: 100%;
            border-radius: 5px;
        }


        .home a i{
            font-size: 1.7rem;

        }

        /* Стили для категории комнаты */
        .category h2 {
            font-family: Montserrat, sans-serif;
            color: #333;
            font-size: 20px;
            font-weight: bold;
        }


        .booking a i{
            font-family: Montserrat, sans-serif;
            color: #333;
            font-size: 1.1rem;
            visibility: hidden;
            opacity: 0;
            transition: visibility 0s, opacity 0.5s linear;
        }

        .booking:hover .cancel a i,.cancel a i:hover{
            font-family: Montserrat, sans-serif;
            color: #333;
            visibility: visible;
            opacity: 1;
        }
        .cancel a i:hover{
            font-family: Montserrat, sans-serif;
            color: #333;
            color: rgb(206, 43, 43);

        }
        .from h3{
            font-family: Montserrat, sans-serif;
            color: #333;
        }
        .to h3{
            font-family: Montserrat, sans-serif;
            color: #333;
        }
        .capacity h3{
            font-family: Montserrat, sans-serif;
            color: #333;
        }
        .beds h3{
            font-family: Montserrat, sans-serif;
            color: #333;
        }

        .cancel a {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;
            background-color: #333;
            padding: 5px 10px; /* Уменьшили внутренние отступы */
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block; /* Изменили на блочный элемент, чтобы не перекрывать текст */
            font-size: 14px; /* Уменьшили размер шрифта */
            line-height: 1; /* Уменьшили межстрочное расстояние */
            margin-top: 5px; /* Добавили небольшой отступ сверху */
        }

        .cancel a:hover {
            background-color: #555;
        }

        .update a {
            font-family: Montserrat, sans-serif;
            color: #f4f4f4;
            background-color: #333;
            padding: 5px 10px; /* Уменьшили внутренние отступы */
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block; /* Изменили на блочный элемент, чтобы не перекрывать текст */
            font-size: 14px; /* Уменьшили размер шрифта */
            line-height: 1; /* Уменьшили межстрочное расстояние */
            margin-top: 5px; /* Добавили небольшой отступ сверху */
        }

        .update a:hover {
            background-color: #555;
        }

        /* CSS для сообщений */
        .messages {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            max-width: 400px; /* Задайте желаемую максимальную ширину */
            background-color: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            transition: top 0.3s ease;
            display: none; /* Начнем с скрытым блоком сообщений */
        }

        .messages.show {
            display: block; /* Показывает сообщения при добавлении класса "show" */
        }

    </style>

</head>

<body>
    {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
                {% endfor %}
            </ul>
    {% endif %}
    <div class="content">
        <div class="header">
            <div class="headings">
                <h1>Welcome {{user.first_name}} {{user.last_name}}</h1>
                <h2>Your Bookings</h2>
            </div>
            <div class="home">
                <!-- Div 1: Back to Home -->
                <div class="home">
                    <a href="{% url 'hotel:HomeView' %}">Home</a>
            </div>

        </div>

        <div class="bookings">
            {% for booking in bookings_list %}
            <div class="booking">
                <div class="category">
                    <h2>{{booking.get_room_category}}</h2>
                    {% if booking.get_room_category == "Single Room" %}
                    <img src="{% static 'single.png' %}" alt="{{booking.get_room_category}}">
                    {% elif booking.get_room_category == "Double Room" %}
                        <img src="{% static 'double.png' %}" alt="{{booking.get_room_category}}">
                    {% elif booking.get_room_category == "Deluxe Room" %}
                        <img src="{% static 'deluxe.png' %}" alt="{{booking.get_room_category}}">
                    {% elif booking.get_room_category == "Family Room" %}
                        <img src="{% static 'family.png' %}" alt="{{booking.get_room_category}}">
                    {% elif booking.get_room_category == "Suite" %}
                        <img src="{% static 'suite.png' %}" alt="{{booking.get_room_category}}">
                    {% endif %}
                </div>
                    <div class="from">
                        <h3>From: {{booking.check_in}}</h3>
                    </div>
                    <div class="to">
                        <h3>To: {{booking.check_out}}</h3>
                    </div>
                    <div class="beds">
                        <h3>Beds: {{booking.room.beds}}</h3>
                    </div>
                    <div class="capacity">
                        <h3>Capacity: {{booking.room.capacity}}</h3>
                    </div>
                    <div class="cancel"><a href="{{booking.get_cancel_booking_url}}">Cancel Booking</a></div>

                    <div class="update"><a href="{{booking.edit_booking}}">Update Booking</a></div>

            </div>
            {% endfor %}
        </div>

            <script>
        // JavaScript код
        document.addEventListener('DOMContentLoaded', function() {
            const messages = document.querySelector('.messages');

            // Показать сообщения
            function showMessages() {
                messages.classList.add('show');
            }

            // Скрыть сообщения
            function hideMessages() {
                messages.classList.remove('show');
            }

            // Показать сообщения при загрузке страницы (если они есть)
            if (messages) {
                showMessages();

                // Закрыть сообщения через некоторое время (например, через 5 секунд)
                setTimeout(hideMessages, 5000);
            }
        });
    </script>

</body>

</html>
```

## Изменение бронирования
```html title="edit_booking.html"
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        /* Ваши стили */
        /* Стили для общей страницы */
        body {
            font-family: Montserrat, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        /* Стили для контейнера с формой */
        .container {
            font-family: Montserrat, sans-serif;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 60%;
            margin: 20px;
            padding: 20px;
            text-align: center;
        }

        /* Стили для заголовка "Edit Booking" */
        h1 {
            font-family: Montserrat, sans-serif;
            color: #333
        }

        /* Стили для формы */
        form {
            font-family: Montserrat, sans-serif;
            display: flex;
            flex-direction: column;
            color: #333
        }

        /* Стили для полей ввода и выбора */
        .input-div, select {
            font-family: Montserrat, sans-serif;
            margin: 10px 0;
            color: #333
        }

        /* Стили для кнопки "Save Changes" */
        button[type="submit"] {
            font-family: Montserrat, sans-serif;
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #555;
        }

         /* Стили для кнопки Home */
        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #fff;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-right: 10px; /* Добавьте отступ справа, например, 10px */
        }

        .home a:hover {
            background-color: #555;
        }
        
    </style>
</head>
<body>
    {% block content %}
    <div class="home">
            <a href="{% url 'hotel:BookingsListView' %}">Get Back</a>
    </div>
    <div class="container">
        <h1>Edit Booking</h1>
        <form method="post">
            {% csrf_token %}


            <!-- Check In Field -->
            <div class="input-div">
                <label for="{{ form.check_in.id_for_label }}" style="font-family: Montserrat, sans-serif;">{{ form.check_in.label_tag }}</label>
                <input type="datetime-local" id="{{ form.check_in.id_for_label }}" name="{{ form.check_in.name }}" style="font-family: Montserrat, sans-serif;" value="{{ form.instance.check_in|date:'Y-m-d\TH:i:s' }}">
            </div>

            <!-- Check Out Field -->
            <div class="input-div">
                <label for="{{ form.check_out.id_for_label }}" style="font-family: Montserrat, sans-serif;">{{ form.check_out.label_tag }}</label>
                <input type="datetime-local" id="{{ form.check_out.id_for_label }}" name="{{ form.check_out.name }}" style="font-family: Montserrat, sans-serif;" value="{{ form.instance.check_out|date:'Y-m-d\TH:i:s' }}">
            </div>

            <!-- Room Category Field (добавленное поле) -->
            <div class="input-div">
                <label for="{{ form.room.id_for_label }}">Room Category : </label>
                {{ form.room }}
            </div>

            <!-- Save Changes Button -->
            <div class="input-div">
                <button type="submit">Save Changes</button>
            </div>
        </form>
    </div>
    {% endblock %}
</body>
</html>
```

## Отмена бронирования
```html title="booking_cancel_view.html"
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cancel Booking</title>

    <style>
        /* Ваши стили */
        /* Стили для общей страницы */
        body {
            font-family: Montserrat, sans-serif;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .room {
            font-family: Montserrat, sans-serif;
            color: #333;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 60%;
            margin: 20px auto; /* Центрирование по горизонтали */
            padding: 20px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Стили для изображения комнаты */
        .room img {
            width: 100%; /* Заполнение изображения внутри блока .room */
            max-height: 300px; /* Ограничение максимальной высоты изображения */
            border-radius: 5px;
        }

        /* Стили для кнопки "Cancel the Booking" */
        #booking-form button {
            font-family: Montserrat, sans-serif;
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
            margin-top: 20px;
        }

        #booking-form button:hover {
            background-color: #555;
        }

        /* Стили для кнопки Home */
        .home {
            font-family: Montserrat, sans-serif;
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
        }

        .home a {
            font-family: Montserrat, sans-serif;
            color: #fff;
            background-color: #333;
            padding: 10px 20px;
            border: 2px solid #fff;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-right: 10px; /* Добавьте отступ справа, например, 10px */
        }

        .home a:hover {
            background-color: #555;
        }
    </style>

</head>

<body>

    <!-- Div 1: Back to Home -->
        <div class="home">
            <a href="{% url 'hotel:BookingsListView' %}">Get Back</a>
        </div>
    <!-- Main Content -->
    <div class="content">

        <!-- Room Details -->
        <div class="room">


            <!-- Div 2: Room Information -->
            <div class="room-info">
                <h1>{{bookings.get_room_category}}</h1>
                {% if bookings.get_room_category == "Single Room" %}
                    <img src="{% static 'single.png' %}" alt="{{bookings.get_room_category}}">
                {% elif bookings.get_room_category == "Double Room" %}
                    <img src="{% static 'double.png' %}" alt="{{bookings.get_room_category}}">
                {% elif bookings.get_room_category == "Deluxe Room" %}
                    <img src="{% static 'deluxe.png' %}" alt="{{bookings.get_room_category}}">
                {% elif bookings.get_room_category == "Family Room" %}
                    <img src="{% static 'family.png' %}" alt="{{bookings.get_room_category}}">
                {% elif bookings.get_room_category == "Suite" %}
                    <img src="{% static 'suite.png' %}" alt="{{bookings.get_room_category}}">
                {% endif %}
                <p> </p>
            </div>

            <!-- Div 3: Room Booking Form -->
            <form id="booking-form" action="" method="POST">

                {% csrf_token %}
                <h2>Are you sure you want to cancel this booking: {{bookings.room.number}} {{bookings.get_room_category}} from {{bookings.check_in}} to {{bookings.check_out}}?</h2>
                <!-- Input Div -->
                <div class="input-div">
                    <button type="submit">Cancel the Booking</button>
                </div>

            </form>

        </div> <!-- END Room Div -->

    </div> <!-- END Main Content Div -->

</body>

</html>
```