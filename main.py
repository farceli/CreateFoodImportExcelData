import random

from openpyxl import load_workbook

initStr = '''
西兰花蒸蛋，食材：西兰花、鸡蛋。
苹果胡萝卜泥，食材：苹果、胡萝卜。
紫薯南瓜粥，食材：紫薯、南瓜、米。
蛋黄菠菜包，食材：鸡蛋黄、菠菜、面粉。
胡萝卜糕点，食材：胡萝卜、面粉、蜂蜜。
菠菜土豆泥，食材：菠菜、土豆、牛奶。
鳕鱼蔬菜煎饼，食材：鳕鱼、蔬菜、面粉。
红薯花卷，食材：红薯、面粉、白糖。
三文鱼蔬菜汤，食材：三文鱼、蔬菜、高汤。
苹果南瓜饼，食材：苹果、南瓜、面粉。
木瓜鸡蛋羹，食材：木瓜、鸡蛋、牛奶。
豌豆胡萝卜饺子，食材：豌豆、胡萝卜、面粉。
红薯花生粥，食材：红薯、花生、米。
番茄鸡蛋面，食材：番茄、鸡蛋、面条。
肉末蒸蛋，食材：肉末、鸡蛋、葱姜。
土豆胡萝卜泥，食材：土豆、胡萝卜、牛奶。
麦片苹果粥，食材：麦片、苹果、水。
豆腐花菜汤，食材：豆腐、花菜、高汤。
鳕鱼胡萝卜饼，食材：鳕鱼、胡萝卜、面粉。
木瓜蔬菜煎饼，食材：木瓜、蔬菜、面粉。
黑米核桃粥，食材：黑米、核桃、水。
苹果蒸鸡胸，食材：苹果、鸡胸肉、葱姜。
鸡蛋胡萝卜炒饭，食材：鸡蛋、胡萝卜、米饭。
紫薯花菜沙拉，食材：紫薯、花菜、沙拉酱。
番茄土豆泥，食材：番茄、土豆、牛奶。
鸡肉胡萝卜饺子，食材：鸡肉、胡萝卜、面粉。
红薯香蕉粥，食材：红薯、香蕉、米。
茄子鱼泥，食材：茄子、鱼肉、酱油。
烤南瓜花生饼，食材：南瓜、花生、面粉。
菠菜玉米粥，食材：菠菜、玉米、米。
苹果鳕鱼炒面，食材：苹果、鳕鱼、面条。
牛肉胡萝卜汤，食材：牛肉、胡萝卜、高汤。
红薯蓝莓饼，食材：红薯、蓝莓、面粉。
鸡蛋胡萝卜粥，食材：鸡蛋、胡萝卜、米。
花菜土豆煎饼，食材：花菜、土豆、面粉。
绿豆红薯粥，食材：绿豆、红薯、水。
苹果鸡肉泥，食材：苹果、鸡肉、香菜。
番茄菠菜面，食材：番茄、菠菜、面条。
鱼香茄子饺子，食材：茄子、猪肉、面粉。
红薯豆腐糕，食材：红薯、豆腐、面粉。
苹果南瓜粥，食材：苹果、南瓜、米。
木瓜糯米蒸饭，食材：木瓜、糯米、葱姜。
豆腐胡萝卜汤，食材：豆腐、胡萝卜、高汤。
鳕鱼洋葱煎饼，食材：鳕鱼、洋葱、面粉。
红薯香蕉饼，食材：红薯、香蕉、面粉。
黑米核桃糕，食材：黑米、核桃、白糖。
苹果蒸鸡腿，食材：苹果、鸡腿肉、葱姜。
鸡蛋胡萝卜炒粉，食材：鸡蛋、胡萝卜、粉条。
紫薯菠菜沙拉，食材：紫薯、菠菜、沙拉酱。
番茄土豆羹，食材：番茄、土豆、高汤。
'''

foodName = []
ingredientName = []
for i in initStr.replace('\n', '').split('。'):
    if i != '':
        foodName.append(i.split('，食材：')[0])
        ingredientName.append(i.split('，食材：')[1].split('、'))
print(foodName)
print(ingredientName)

excel = load_workbook('菜品库导入模板.xlsx')
sheet1 = excel['Sheet1']
initSerialNumber = 3
for i in range(len(foodName)):
    initSerialIngredientNameNumber = initSerialNumber
    sheet1['A' + str(initSerialNumber)] = i + 1
    sheet1['B' + str(initSerialNumber)] = foodName[i]
    for j in ingredientName[i]:
        sheet1['C' + str(initSerialIngredientNameNumber)] = j
        sheet1['D' + str(initSerialIngredientNameNumber)] = str(random.randint(5, 15)) + '0'
        initSerialIngredientNameNumber += 1
    initSerialNumber += len(ingredientName[i])

excel.save('菜品库导入模板.xlsx')
excel.close()
