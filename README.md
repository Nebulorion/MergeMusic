# MergeMusic


## Демонстрация


https://replit.com/@alexanderprikup/MergeMusic


## Команды перед запуском


### Библиотеки для запуска


pip install ffmpeg


pip install pydub


### Библиотеки для тестирования

pip install ffmpeg


pip install pydub


pip install pytest

### Тестирование


bash tests.bash


### Библиотеки для документации


pip install pydoc


### Создание документации в html

bash doc.bash


### Запуск

python main.py


## Документация


### Класс MergeMusicPresenter() для соединения аудиофайлов mp3 

Функция check_conditions() проверяет наличие mp3 файла в input1 и input2.
Возвращает предупреждение или 0

Функция create() создаёт новый аудиофайлов в output, последовательно соединяя аудиофайлы из input1 и input2.
Возвращает предупреждение или название нового аудиофайла

### Класс MergeMusicView() для работы с классом MergeMusicPresenter() (для работы в консоли)

Функция start() для начала работы в консоли.
Возвращает предупреждение или название нового аудиофайла

### Класс TestMergeMusic() проводит модульные тесты для MergeMusicPresenter и MergeMusicView 

Функция clean_folders() очищает output, input1 и input2 перед проведением тестов

Функция test_check_conditions() проверяет, что функция check_conditions() из MergeMusicPresenter определяет файлы в output, input1 и input2 и выводит правильные значения

Функция test_create() проверяет, что функция create() из MergeMusicPresenter правильно возращает название аудиофайла, созданного в output, последовательно соединённого из аудиофайлов из input1 и input2.
Также проводится проверка на возвращение предупреждений, если в папках input1 и input2 ожидается проблема с файлами

Функция test_start() проверяет, что функция start() из MergeMusicView, которая также вызывает функцию create() из MergeMusicPresenter, правильно возращает название аудиофайла, созданного в output, последовательно соединённого из аудиофайлов из input1 и input2.
Также проводится проверка на возвращение предупреждений, если в папках input1 и input2 ожидается проблема с файлами