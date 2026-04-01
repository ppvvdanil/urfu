# Найденные ошибки и исправления

1. В `get_age` возраст вычислялся как `self.yob - now.year`, что давало отрицательное значение.
Исправлено на `now.year - self.yob`.

2. В `set_name` было присваивание `self.name = self.name`, поэтому имя не менялось.
Исправлено на `self.name = name`.

3. В `set_address` использовалось сравнение `self.address == address` вместо присваивания.
Исправлено на `self.address = address`.

4. В `is_homeless` использовалась несуществующая переменная `address`, что вызывало `NameError`.
Исправлено на проверку поля объекта: `self.address == ''`.

5. В модуле отсутствовал импорт `datetime`, хотя он используется в `get_age`.
Добавлен `import datetime`.
