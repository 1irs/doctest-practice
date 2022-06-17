# Практическое занятие

В результате успешного выполнения практического задания студент будет уметь:

* описывать тесты к функции в формате doctest;
* запускать doctest;

## Требования к программному обеспечению

* Операционная система: Windows, MacOS или Linux;
* Python 3.10 или старше
* Любой текстовый редактор

## Установка doctest

Doctest — стандартный пакет Python и не требует установки.

## Тесты в документации

Рассмотрим файл `bubble_sort.py`:


```python
# Source: http://rosettacode.org/
import doctest


def bubble_sort(seq):
    """
    Put your doctests here:

    >>> bubble_sort([])
    []

    """
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq


doctest.testmod(verbose=True)
```

Здесь присутствует один тест, который проверяет, что для `bubble_sort([])` ответ должен быть `[]`.

Запустить тесты можно командой:

    python bubble_sort.py

Вывод на консоль будет таким:

```text
Trying:
    bubble_sort([])
Expecting:
    []
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.bubble_sort
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

## Новые тесты

Запишите тесты в документации функции в файле `bubble_sort.py`:

* проверка работы с пустым массивом;
* проверка работы с упорядоченным массивом целых чисел;
* проверка работы с неупорядоченным массивом вещественных чисел;
* проверка работы со строкой "hello world".

Отчет о запуске (текст консольного вывода) сохраните в файл `doctest_report.txt`.

## Отчет

Для отчета по практическому заданию необходимо:

1. Создать публичный репозиторий на GitHub на основе репозитория https://github.com/1irs/doctest-practice Можно воспользоваться страницей Generate: https://github.com/1irs/doctest-practice/generate для создания своего репозитория по шаблону.
2. В отдельном коммите дописать тесты и добавить файл `doctest_report.txt`
3. Прислать ссылку на репозиторий на obrizan@1irs.net
