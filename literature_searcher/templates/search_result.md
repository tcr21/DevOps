{% extends "basic.html" %}
{% block title %}Response{% endblock %}
{% block body %}
Response to query:<br>
<ul>
{% for result in search_results %}
<li> {{ result }}
{% endfor %}
</ul>
<!-- <a href="./search_page.html">Back to Search Page</a> -->
{% endblock %}