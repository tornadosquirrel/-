import random
import time

#-----변수들-----
mySword = ["나뭇가지"]
upgrade = [0]
whichSword = "나뭇가지"
myEquipment = ["잠옷"]
whichEquipment = "잠옷"
money = 1000
upgradeCost = 500
percentage = 100
percentageSystem = random.randint(1, 100)
sellCost = 0
power = 10
bossboss = ["보스1", "보스2", "보스3", "보스4", "보스5", "보스6", "보스7", "보스8", "보스9", "보스10"]
boss = "보스1"
bossPower = 10
hp = 100
bossHp = 50
bossMoneyList = [500, 1000, 10000, 50000, 100000, 1000000, 1000001, 10000002, 10000000, 100000000]
bossMoney = 500
#-----시작화면-----
print("----------\n검강화하기\n----------")

while True:
  menu = input("\033[95m" + "----------\n내정보 : 1\n인벤토리 : 2\n검강화 : 3\n상점 : 4\n보스잡기 : 5\n게임종료 : 6\n----------\n" + "\033[0m")
#-----내정보-----
  if menu == "1":
    print("----------\n현재 검 :", whichSword + "(+" + str(upgrade) + ")\n현재 장비 :", whichEquipment, "\n공격력 :", str(power), "\n체력 :", str(hp), "\n소지금 :", str(money), "\n----------\n")
#-----인벤토리-----
  elif menu == "2":
    print("----------\n나의 검들 :", mySword, "\n나의 장비들", myEquipment, "\n----------")
    while True:
        chooseSword = input("장착할 검의 이름을 입력해 주세요(건너뛰려면 1 입력) : ")
        if chooseSword in mySword:
            whichSword = mySword[mySword.index(chooseSword)]
            print(whichSword + "(+" + str(upgrade) + ") 장착되었습니다.")
            break
        elif chooseSword == "1":
           break
        else:
            print(chooseSword, "없는데?")
    while True:
        chooseEquipment = input("장착할 장비의 이름을 입력해 주세요(건너뛰려면 1입력) : ")
        if chooseEquipment in myEquipment:
            whichEquipment = myEquipment[myEquipment.index(chooseEquipment)]
            print(whichEquipment, "장착되었습니다.")
            break
        elif chooseEquipment == "1":
           break
        else:
            print(chooseEquipment, "없는데?")
  elif menu == "3":
     while True:
      print("----------\n현재 검 :", whichSword + ")\n공격력 :", str(power), "\n소지금 :", str(money), "\n강화비용 :", str(upgradeCost), "강화확률 :", str(percentage) + "%\n판매가 :", str(sellCost), "\n----------")
      reinforce = input("강화하시겠습니까?(y/n)")
      if reinforce == "y":
        if money < upgradeCost:
          print("돈 부족")
        elif percentage < percentageSystem:
          print("\033[31m" + "강화에 실패하였습니다." + "\033[0m")
        else:
          upgrade[mySword.index(whichSword)] = upgrade[mySword.index(whichSword)] + 1
          power = power + 10
          money = money - upgradeCost
          upgradeCost = upgradeCost + 500
          percentage = percentage - 5
          sellCost = sellCost + 500
          whichSword = whichSword + "(+" + str(upgrade[mySword.index(whichSword)])
          print("\033[33m" + "강화에 성공하였습니다." + "\033[0m")
      else:
        break
  elif menu == "4":
    print("귀찮으니까 나중에 구현할게여~ㅋㅋ")
  elif menu == "5":
    while True:
      print("----------\n보스들 :", bossboss, "\n----------")
      bossSelect = input("도전할 보스의 이름을 입력해 주세요(취소하려면 1입력) : ")
      if bossSelect in bossboss:
        boss = bossboss[bossboss.index(bossSelect)]
        bossMoney = bossMoneyList[bossboss.indes(bossSelect)]
        print("----------\n내 체력 :", str(hp), "\n보스 체력 :", str(bossHp))
        while hp > 0 or bossHp > 0:
          hp = hp - bossPower
          print("내 공격\n내 체력 :", str(hp), "\n보스 체력 :", str(bossHp))
          bossHp = bossHp - power
          print("보스 공격\n내 체력 :", str(hp), "\n보스 체력 :", str(bossHp))
          if hp <= 0:
            print("----------\n쥬금")
            retry = input("재도전?(y/n)")
            if retry == "n":
              break
          if bossHp <0:
            money = money + bossMoney
            print("----------\n이김\n----------\n돈 +", bossMoney)
      elif bossSelect == "1":
        break
      else:
        print(bossSelect, "없는데?")
    
      
    
        