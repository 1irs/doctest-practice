# Практическое занятие

В результате успешного выполнения практического задания студент будет уметь:

* описывать тесты к функции в формате docteste;
* запускать doctest;

## Требования к программному обеспечению

* Операционная система: Windows, MacOS или Linux;
* Python 3.10 или старше
* Любой текстовый редактор

## Установка doctest

Doctest — стандартный пакет Python и не требует установки.

## Тесты в документации

Запишите тесты в документации функции в файле `bubble_sort.py`:

* проверка работы с пустым массивом;
* проверка работы с упорядоченным массивом целых чисел;
* проверка работы с неупорядоченным массивом вещественных чисел;
* проверка работы со строкой "hello world".

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

Отчет о запуске (текст консольного вывода) сохраните в файл `doctest_report.txt`.

## Отчет

Для отчета по практическому заданию необходимо:

1. Создать публичный репозиторий на GitHub на основе репозитория https://github.com/1irs/doctest-practice Можно воспользоваться страницей Generate: https://github.com/1irs/doctest-practice/generate для создания своего репозитория по шаблону.
2. В отдельном коммите дописать тесты и добавить файл `doctest_report.txt`
3. Прислать ссылку на репозиторий на obrizan@1irs.net
