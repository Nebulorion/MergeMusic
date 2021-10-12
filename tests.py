from mergemusicview import MergeMusicView
from mergemusicpresenter import MergeMusicPresenter
import shutil
import os
import glob

class TestMergeMusic():
  """
  Класс TestMergeMusic() проводит модульные тесты для MergeMusicPresenter и MergeMusicView 
  """
  mergeMusicPresenter = MergeMusicPresenter()
  mergeMusicView = MergeMusicView()

  def clean_folders(self):
    """
    Функция clean_folders() очищает output, input1 и input2 перед проведением тестов
    """
    files = glob.glob('input1/*')
    for f in files:
      os.remove(f)
    files = glob.glob('input2/*')
    for f in files:
      os.remove(f)
    files = glob.glob('output/*')
    for f in files:
      os.remove(f)

  def test_check_conditions(self):
    """
    Функция test_check_conditions() проверяет, что функция check_conditions() из MergeMusicPresenter определяет файлы в output, input1 и input2 и выводит правильные значения
    """
    self.clean_folders()
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1') 
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2') 
    
    assert self.mergeMusicPresenter.check_conditions() == "0"
    ###
    self.clean_folders()
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1/input1_1.mp3') 
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1/input1_2.mp3')
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2/input2.mp3') 
    
    assert self.mergeMusicPresenter.check_conditions() == "input1IsFull"
    ###
    self.clean_folders()
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1/input1.mp3') 
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2/input2_1.mp3') 
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2/input2_2.mp3') 
    
    assert self.mergeMusicPresenter.check_conditions() == "input2IsFull"
    ###
    self.clean_folders()
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2/input2.mp3') 
    
    assert self.mergeMusicPresenter.check_conditions() == "input1IsEmpty"
    ###
    ###
    self.clean_folders()
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1/input1.mp3') 
    
    assert self.mergeMusicPresenter.check_conditions() == "input2IsEmpty"
    self.clean_folders()


  def test_create(self):
    """
    Функция test_create() проверяет, что функция create() из MergeMusicPresenter правильно возращает название аудиофайла, созданного в output, последовательно соединённого из аудиофайлов из input1 и input2
    Также проводится проверка на возвращение предупреждений, если в папках input1 и input2 ожидается проблема с файлами
    """
    self.clean_folders()
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1') 
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2') 
    
    assert self.mergeMusicPresenter.create() == "output/Alla-TurcaHall of the Mountain King.mp3"
    self.clean_folders()

  def test_start(self):
    """
    Функция test_start() проверяет, что функция start() из MergeMusicView, которая также вызывает функцию create() из MergeMusicPresenter, правильно возращает название аудиофайла, созданного в output, последовательно соединённого из аудиофайлов из input1 и input2
    Также проводится проверка на возвращение предупреждений, если в папках input1 и input2 ожидается проблема с файлами
    """
    self.clean_folders()
    shutil.copy2('tests/input1/Alla-Turca.mp3', 'input1') 
    shutil.copy2('tests/input2/Hall of the Mountain King.mp3', 'input2') 
    
    assert self.mergeMusicView.start() == "output/Alla-TurcaHall of the Mountain King.mp3"
    self.clean_folders()