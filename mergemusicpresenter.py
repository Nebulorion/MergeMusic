#import pydoc
from os import walk
from pathlib import Path
from pydub import AudioSegment

class MergeMusicPresenter():
  """
  Класс MergeMusicPresenter() для соединения аудиофайлов mp3 
  """
  input1_filename = ""
  input2_filename = ""

  answer_array=["input1IsEmpty","input1IsFull","input2IsEmpty","input2IsFull","input1IsNotMp3","input2IsNotMp3"]

  def check_conditions(self):
    """
    Функция check_conditions() проверяет наличие mp3 файла в input1 и input2
    Возвращает предупреждение или 0
    """
    input1_filenames = next(walk("input1"), (None, None, []))[2]  # [] if no file
    input2_filenames = next(walk("input2"), (None, None, []))[2]  # [] if no file
    if(len(input1_filenames) == 0):
      return("input1IsEmpty")
    elif (len(input1_filenames) > 1):
      return ("input1IsFull")
    elif (len(input2_filenames) == 0):
      return ("input2IsEmpty")
    elif (len(input2_filenames) > 1):
      return ("input2IsFull")
    input1_filename = input1_filenames[0]
    input2_filename = input2_filenames[0]
    print(input1_filename)
    print(input2_filename)
    if(not(Path(input1_filename).suffix == '.mp3')):
      return("input1IsNotMp3")
    elif(not(Path(input2_filename).suffix == '.mp3')):
      return ("input2IsNotMp3")
    else:
      self.input1_filename = input1_filename
      self.input2_filename = input2_filename
      return("0")
  def create(self):
    """
    Функция create() создаёт новый аудиофайлов в output, последовательно соединяя аудиофайлы из input1 и input2
    Возвращает предупреждение или название нового аудиофайла
    """
    if(self.check_conditions()=="0"):
      sound1 = AudioSegment.from_mp3("input1/"+self.input1_filename)
      sound2 = AudioSegment.from_mp3("input2/"+self.input2_filename)
      sound3 = sound1 + sound2
      sound3.export("output/"+self.input1_filename.split(".")[0].rstrip()+self.input2_filename, format="mp3")
      return("output/"+self.input1_filename.split(".")[0].rstrip()+self.input2_filename)
    else:
      return(self.check_conditions())

if __name__ == "__main__":
  mergeMusicPresenter = MergeMusicPresenter()
  answer="reload"
  while((answer=="reload")):
    print(mergeMusicPresenter.create().rstrip())
    print('\nНапишите "reload", чтобы продолжить работу программы\n')
    answer = input()