# 8.生成字典
import copy
keys = ["演员", "角色", "配音演员"]
actors = ["刘昊然", "宋祖儿", "陈岩轩", "张志坚", "李光洁", "许晴", "江疏影", "王鸥", "张丰毅",
          "张嘉译", "宣言", "魏千翔", "刘冠成", "江涛", "董勇", "杨新鸣", "张智尧", "陈昊宇", "杨玏", "吴佳怡"]
characters = ["吕归尘", "羽然", "姬野", "雷碧城", "息衍", "白绫波", "宫羽衣", "苏舜卿", "赢无翳",
              "百里景洪", "白鹿颜", "百里宁卿", "拓跋山月", "翼天瞻", "吕蒿", "大合萨", "白毅", "小周公主", "吕鹰扬", "赢玉"]
voiceActors = ["无", "无", "许凯", "无", "无", "无", "韩啸", "无", "宣晓鸣",
               "无", "无", "姜广涛", "杨默", "无", "无", "郭正建", "宝木中阳", "无", "无", "无"]
dictA = dict()
for i in actors:
    j = 0
    dictA[i] = (dict(zip(keys, list(zip(actors, characters, voiceActors))[j])))
    j += 1
print(dictA["刘昊然"]["角色"])
dictBackup = copy.deepcopy(dictA)
dictA.pop("江疏影")
dictA.update({"张静初": {"演员": "张静初", "角色": "宫羽衣", "配音演员": "韩啸"}})
print(dictBackup)
print("总角色数", len(dictBackup))
