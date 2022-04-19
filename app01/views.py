from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import math
import MySQLdb
from django.db.models import Avg, Max, Min, Count, Sum


# Create your views here.
def index(request):
    if request.method=='GET':
        db = MySQLdb.connect("localhost", "root", "", "mysite", charset='utf8')
        cursor = db.cursor()
        sql="SELECT * FROM mysite.app01_symmap3_herb_herb_cosine_jiaoji  where id<=7;"
        cursor.execute(sql)
        res=cursor.fetchall()
        mid1 = models.symmap3_herb_mm_symp_jiaoji.objects.filter(Herb="西河柳")
        res1 = mid1[0:3]
        print(res1)
        mid2 = models.symmap3_herb_mm_symp_jiaoji.objects.filter(Herb="娑罗子")
        res2 = mid2[0:3]
        mid3 = models.symmap3_herb_mm_symp_jiaoji.objects.filter(Herb="栀子")
        res3 = mid3[0:3]
        mid4 = models.symmap3_herb_mm_symp_jiaoji.objects.filter(Herb="山豆根")
        res4 = mid4[0:3]
        mid5 = models.symmap3_herb_target_jiaoji.objects.filter(Herb="艾叶")
        res5 = mid5[0:3]
        mid6 = models.symmap3_herb_target_jiaoji.objects.filter(Herb="羌活")
        res6 = mid6[0:3]
        mid7 = models.symmap3_herb_target_jiaoji.objects.filter(Herb="酸枣仁")
        res7 = mid7[0:3]
        mid8 = models.symmap3_herb_target_jiaoji.objects.filter(Herb="罗汉果")
        res8 = mid8[0:3]
        sql1="SELECT * FROM mysite.app01_gene_gene limit 0,8;"
        cursor.execute(sql1)
        newres2 = cursor.fetchall()
        sql2="SELECT * FROM mysite.app01_gene_dis limit 0,8;"
        cursor.execute(sql2)
        newres1=cursor.fetchall()
        return render(request, "index2.html",
                      {'res':res,'res1': res1, 'res2': res2, 'res3': res3, 'res4': res4, 'res5': res5, 'res6': res6, 'res7': res7,
                       'res8': res8,'newres1':newres1,'newres2':newres2})


def searchres(request):
    search=request.GET.get('search')
    db = MySQLdb.connect("localhost", "root", "", "mysite", charset='utf8')
    cursor = db.cursor()
    sql1="select * from mysite.app01_symmap3_herb_mm_symp_jiaoji where Herb='%s' or Gene='%s';"%(search,search)
    cursor.execute(sql1)
    res1=cursor.fetchall()
    sql2 = "select * from mysite.app01_symmap3_herb_target_jiaoji where Herb='%s' or Gene='%s';" % (search,search)
    cursor.execute(sql2)
    res2 = cursor.fetchall()
    sql3 = "select * from mysite.app01_symmap3_herb_herb_cosine_jiaoji where herb1='%s' or herb2='%s';" % (search,search)
    cursor.execute(sql3)
    res3 = cursor.fetchall()
    sql4 = "select * from mysite.app01_gene_dis where Gene='%s' or Dis='%s';" % (search,search)
    cursor.execute(sql4)
    res4 = cursor.fetchall()
    sql5 = "select * from mysite.app01_gene_gene where Gene1='%s' or Gene2='%s';" % (search, search)
    cursor.execute(sql5)
    res5 = cursor.fetchall()
    return render(request, "searchres.html",{'res1':res1,'res2':res2,'res3':res3,'res4':res4,'res5':res5})



def more(request):
    name = request.GET.get('name')
    got = request.GET.get('got')
    print(got)
    now = ""
    if got == "1":
        now = "MM"
    else:
        now = "target"
    mid = models.symmap3_herb_mm_symp_jiaoji.objects.filter(Herb=name)
    ress = {}
    for num in range(0, math.ceil(mid.__len__() / 4)):
        start = 4 * num
        end = mid.__len__() if 4 * (num + 1) > mid.__len__() else 4 * (num + 1)
        ress[num] = mid[start:end]
        print(ress[num])
    if request.method == 'GET':
        res = mid[0:8]
        return render(request, "findmore.html", {'res': ress, 'now': now})
    return render(request, "findmore.html", {'res': ress, 'now': now})




def symall(request):
    newres={}
    db = MySQLdb.connect("localhost", "root", "", "mysite", charset='utf8')
    cursor = db.cursor()
    sqls = "SELECT count(*) FROM mysite.app01_symmap3_herb_herb_cosine_jiaoji;"
    cursor.execute(sqls)
    itemnum = int(cursor.fetchall()[0][0])
    finalpage = itemnum / 16
    ranges = 5
    startpage=1
    if request.method=='GET':
        id=request.GET.get('id')
        page=int(request.GET.get('page'))
        if page>=finalpage:
            page=finalpage
        if page>=finalpage-ranges:
            endpage=finalpage-ranges
        elif page<=6:
            startpage=1
            endpage=11
        else:
            startpage=page-ranges
            endpage=page+ranges
        page_str_list=[]
        if page>1:
            prev='<li class="page-item"><a class="page-link" href="/symall/?id={}&page={}" target="_self">上一页</a></li>'.format(id,page-1)
        else:
            prev='<li class="page-item"><a class="page-link" href="/symall/?id={}&page={}" target="_self">上一页</a></li>'.format(id,1)
        page_str_list.append(prev)
        for i in range(startpage,endpage):
            if i==page:
                ele='<li class="page-item active"><a class="page-link" href="/symall/?id={}&page={}" target="_self">{}</a></li>'.format(id,i,i)
            else:
                ele='<li class="page-item"><a class="page-link" href="/symall/?id={}&page={}" target="_self">{}</a></li>'.format(id,i,i)
            page_str_list.append(ele)
        if page<endpage:
            invv='<li class="page-item"><a class="page-link" href="/symall/?id={}&page={}" target="_self">下一页</a></li>'.format(id,page+1)
        else:
            invv='<li class="page-item"><a class="page-link" href="/symall/?id={}&page={}" target="_self">下一页</a></li>'.format(id,63)
        page_str_list.append(invv)
        page_string=mark_safe("".join(page_str_list))
        #数据库
        head = 8 * (page - 1)
        tail = 8 * page
        if(id=="1"):
            cursor = db.cursor()
            sql="select a.Herb,a.Gene from mysite.app01_symmap3_herb_mm_symp_jiaoji as a,(SELECT DISTINCT Herb from mysite.app01_symmap3_herb_mm_symp_jiaoji limit %s,%s) as b where a.Herb=b.Herb" %(head,tail)
            cursor.execute(sql)
            results = cursor.fetchall()
            sql2="SELECT DISTINCT Herb from mysite.app01_symmap3_herb_mm_symp_jiaoji limit %s,%s" %(head,8)
            cursor.execute(sql2)
            results2=cursor.fetchall()
            newresindex=0;
            for i in results2:
                mid=[i[0],]
                for j in results:
                    if(mid.__len__()>5):
                        break
                    if(j[0]==i[0]):
                        mid.append(j[1])
                newres[newresindex]=mid
                newresindex+=1
            res=list(newres.values())
            return render(request,"symall.html",{'pagestring':page_string,'newres':res})
        else:
            cursor = db.cursor()
            sql = "select a.Herb,a.Gene from mysite.app01_symmap3_herb_target_jiaoji as a,(SELECT DISTINCT Herb from mysite.app01_symmap3_herb_target_jiaoji limit %s,%s) as b where a.Herb=b.Herb" % (
            head, tail)
            cursor.execute(sql)
            results = cursor.fetchall()
            sql2 = "SELECT DISTINCT Herb from mysite.app01_symmap3_herb_target_jiaoji limit %s,%s" % (head, 8)
            cursor.execute(sql2)
            results2 = cursor.fetchall()
            newresindex = 0;
            for i in results2:
                mid = [i[0], ]
                for j in results:
                    if (mid.__len__() > 5):
                        break
                    if (j[0] == i[0]):
                        mid.append(j[1])
                newres[newresindex] = mid
                newresindex += 1
            res = list(newres.values())
            return render(request, "symall.html", {'pagestring': page_string, 'newres': res})
def HHall(request):
    db = MySQLdb.connect("localhost", "root", "", "mysite", charset='utf8')
    cursor=db.cursor()
    sqls="SELECT count(*) FROM mysite.app01_symmap3_herb_herb_cosine_jiaoji;"
    cursor.execute(sqls)
    itemnum=int(cursor.fetchall()[0][0])
    finalpage=itemnum/16
    startpage=int(1)
    if request.method=='GET':
        page=int(request.GET.get('page'))
        # 页码部分
        if page>=finalpage:
            page=finalpage
        ranges = 5
        if page>=finalpage-ranges:
            endpage=finalpage-ranges
        elif page<=6:
            startpage=1
            endpage=11
        else:
            startpage=page-ranges
            endpage=page+ranges
        page_str_list=[]
        if page>1:
            prev='<li class="page-item"><a class="page-link" href="/HHall/?page={}" target="_self">上一页</a></li>'.format(page-1)
        else:
            prev='<li class="page-item"><a class="page-link" href="/HHall/?page={}" target="_self">上一页</a></li>'.format(1)
        page_str_list.append(prev)
        for i in range(startpage,endpage):
            if i==page:
                ele='<li class="page-item active"><a class="page-link" href="/HHall/?page={}" target="_self">{' \
                    '}</a></li>'.format(i,i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="/HHall/?page={}" target="_self">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        if page<endpage:
            invv='<li class="page-item"><a class="page-link" href="/HHall/?page={}" target="_self">下一页</a></li>'.format(page+1)
        else:
            invv='<li class="page-item"><a class="page-link" href="/HHall/?page={}" target="_self">下一页</a></li>'.format(63)
        page_str_list.append(invv)
        page_string=mark_safe("".join(page_str_list))
        #数据库
        head = 16 * (page - 1)
        tail = 8 * page
        cursor=db.cursor()
        sql = "SELECT * from mysite.app01_symmap3_herb_herb_cosine_jiaoji limit %s,%s" % (head, 16)
        cursor.execute(sql)
        res=cursor.fetchall()
    return render(request,"HHall.html",{'pagestring':page_string,'res':res})


def finalall(request):
    db = MySQLdb.connect("localhost", "root", "", "mysite", charset='utf8')
    cursor = db.cursor()
    sqls = "SELECT count(*) FROM mysite.app01_gene_dis;"
    cursor.execute(sqls)
    itemnum = int(cursor.fetchall()[0][0])
    finalpage = itemnum / 16
    startpage = int(1)
    if request.method=='GET':
        page=int(request.GET.get('page'))
        # 页码部分
        if page>=finalpage:
            page=finalpage
        ranges = 5
        if page>=finalpage-ranges:
            endpage=finalpage-ranges
        elif page<=6:
            startpage=1
            endpage=11
        else:
            startpage=page-ranges
            endpage=page+ranges
        page_str_list=[]
        if page>1:
            prev='<li class="page-item"><a class="page-link" href="/finalall/?page={}" target="_self">上一页</a></li>'.format(page-1)
        else:
            prev='<li class="page-item"><a class="page-link" href="/finalall/?page={}" target="_self">上一页</a></li>'.format(1)
        page_str_list.append(prev)
        for i in range(startpage,endpage):
            if i==page:
                ele='<li class="page-item active"><a class="page-link" href="/finalall/?page={}" target="_self">{' \
                    '}</a></li>'.format(i,i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="/finalall/?page={}" target="_self">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        if page<endpage:
            invv='<li class="page-item"><a class="page-link" href="/finalall/?page={}" target="_self">下一页</a></li>'.format(page+1)
        else:
            invv='<li class="page-item"><a class="page-link" href="/finalall/?page={}" target="_self">下一页</a></li>'.format(63)
        page_str_list.append(invv)
        page_string=mark_safe("".join(page_str_list))
        #数据库
        head = 16 * (page - 1)
        cursor=db.cursor()
        sql = "SELECT * from mysite.app01_gene_dis limit %s,%s" % (head, 16)
        cursor.execute(sql)
        newres1=cursor.fetchall()
    return render(request,"FinalAll.html",{'pagestring':page_string,'newres1':newres1})

def finalall2(request):
    db = MySQLdb.connect("localhost", "root", "", "mysite", charset='utf8')
    cursor = db.cursor()
    sqls = "SELECT count(*) FROM mysite.app01_gene_gene;"
    cursor.execute(sqls)
    itemnum = int(cursor.fetchall()[0][0])
    finalpage = itemnum / 16
    startpage = int(1)
    if request.method=='GET':
        page=int(request.GET.get('page'))
        # 页码部分
        if page>=finalpage:
            page=finalpage
        ranges = 5
        if page>=finalpage-ranges:
            endpage=finalpage-ranges
        elif page<=6:
            startpage=1
            endpage=11
        else:
            startpage=page-ranges
            endpage=page+ranges
        page_str_list=[]
        if page>1:
            prev='<li class="page-item"><a class="page-link" href="/finalall2/?page={}" target="_self">上一页</a></li>'.format(page-1)
        else:
            prev='<li class="page-item"><a class="page-link" href="/finalall2/?page={}" target="_self">上一页</a></li>'.format(1)
        page_str_list.append(prev)
        for i in range(startpage,endpage):
            if i==page:
                ele='<li class="page-item active"><a class="page-link" href="/finalall2/?page={}" target="_self">{' \
                    '}</a></li>'.format(i,i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="/finalall2/?page={}" target="_self">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        if page<endpage:
            invv='<li class="page-item"><a class="page-link" href="/finalall2/?page={}" target="_self">下一页</a></li>'.format(page+1)
        else:
            invv='<li class="page-item"><a class="page-link" href="/finalall2/?page={}" target="_self">下一页</a></li>'.format(63)
        page_str_list.append(invv)
        page_string=mark_safe("".join(page_str_list))
        #数据库
        head = 16 * (page - 1)
        cursor=db.cursor()
        sql = "SELECT * from mysite.app01_gene_gene limit %s,%s;" % (head, 16)
        cursor.execute(sql)
        newres1=cursor.fetchall()
    return render(request,"finalall2.html",{'pagestring':page_string,'newres1':newres1})




