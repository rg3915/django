# Pedido

Baseado no banco de dados [pedido][1] resolvi fazer este projeto para testar os recursos do Django.

Inicialmente eu quero explorar as bibliotecas do [class based views][2] como [TemplateView][3] [ListView][4] e [FormView][5].

Um site com um tutorial legal é [GoDjango][6] e [DevCode.la][7]

Usaremos o sqlite3.

Para gerar o myproject.png usei o *django_extensions* a partir do site [django-notes][8] com o comando

	$ ./manage.py graph_models -a -g -o my_project.png

[1]: https://github.com/rg3915/banco_de_dados/tree/master/pedido
[2]: https://docs.djangoproject.com/en/dev/ref/class-based-views/
[3]: https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#templateview
[4]: https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#listview
[5]: https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#formview
[6]: https://godjango.com/
[7]: http://devcode.la/django/videos/
[8]: http://django-notes.blogspot.com.br/2012/07/vizualization.html