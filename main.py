from mergemusicview import MergeMusicView

mergeMusicView = MergeMusicView()
answer="reload"
while((answer=="reload")):
  print(mergeMusicView.start().rstrip())
  print('\nНапишите "reload", чтобы продолжить работу программы\n')
  answer = input()