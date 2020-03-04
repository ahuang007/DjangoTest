# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestMode1.models import Test

# 数据库操作

# 添加数据
def testAdd(request):
    test1 = Test(name='ahuang')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

# 查询数据
def testQuery(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过 objects 这个模型管理器的 all() 获得所有数据行，相当于 SQL 中的 SELECT * FROM
    list = Test.objects.all()

    # filter 相当于 SQL 中的 WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2
    Test.objects.order_by('name')[0:2]

    # 数据牌型 相当于 SQL 中的 ORDER BY
    Test.objects.order_by("id")

    # 上面的方法可以联合使用
    Test.objects.filter(name="ahuang").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

# 修改数据

def testModify(request):
    # 修改其中一个 id=1 的 name 字段，再 save,相当于 SQL 中的 UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'andy'
    test1.save()
    return HttpResponse("<p>数据修改成功！</p>")

def testDel(request):
    # 删除 id=1 的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    return HttpResponse("<p>数据删除成功！</p>")
