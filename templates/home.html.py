{% extends 'layout.html.py' %}
{% block content %}
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>By {{ post.author }} on {{ post.date_posted }} </p>
        <p>{{ post.content }}</p>
    {% endfor %}
{% endblock  content %}