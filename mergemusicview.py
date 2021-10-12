#import pydoc
from mergemusicpresenter import MergeMusicPresenter

class MergeMusicView():
  """
  Класс MergeMusicView() для работы с классом MergeMusicPresenter() (для работы в консоли)
  """
  mergeMusicPresenter = MergeMusicPresenter()
  def start(self):
    """
    Функция start() для начала работы в консоли
    Возвращает предупреждение или название нового аудиофайла
    """
    print("\nПри ошибке кодеков используйте одну из следующих команд:\n")
    print("pip install ffmpeg\npip install avconv\npip install ffprobe\npip install avprobe\n")
    print("В Replit.com процесс занимает до 3-х минут\n")
    answer = self.mergeMusicPresenter.create()
    if(answer in self.mergeMusicPresenter.answer_array):
      print("\nВыполните следующие действия с mp3 файлами:\n")
      print("Перенесите первый аудиофайл в input1;\n")
      print("Перенесите второй аудиофайл в input2.\n")
      print('Когда условия выше будут выполнены, попробуйте вызвать функцию ещё раз\n')
      
      print('Предупреждение:\n')
      print(answer)
      return(answer)
    else:
      return(answer)

if __name__ == "__main__":
  mergeMusicView = MergeMusicView()
  answer="reload"
  while((answer=="reload")):
    print(mergeMusicView.start().rstrip())
    print('\nНапишите "reload", чтобы продолжить работу программы\n')
    answer = input()