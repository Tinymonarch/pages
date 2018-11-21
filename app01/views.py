from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

USER_LIST = []
for i in range(1,999):
    temp = {'name': 'root'+str(i), 'age': i}
    USER_LIST.append(temp)

def index(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)
    # p=1
    # 0,10 0-9
    # p=2
    # 10,20 10-19
    start = (current_page-1) * per_page_count
    end = current_page * per_page_count
    data = USER_LIST[start:end]

    prev_page = current_page - 1
    next_page = current_page + 1
    return render(request, 'index.html', {'user_list':data,
                                          'perv_page': prev_page,
                                          'next_page': next_page,})


def index1(request):

    paginator = Paginator(USER_LIST, 10)
    # 全部数据：    USER_LIST,=> 得出的共有多少条数据
    # per_page:    每页显示条目数量
    # count：      数据总个数
    # num_pages：  总页数
    # page_range:  总页数的索引范围，如：（1，10） （1，200）
    # page：       page对象
    current_page = request.GET.get('p')
    try:
        posts = paginator.page(current_page)
        #has_next               是否有下一页
        #next_page_number       下一页页码
        #has_previous           是否有上一页
        #pervious_page_number   上一页页码
        #object_list            分页之后的数据列表
        #number                 当前页
        #paginator              paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except Exception:
        posts = paginator.page(paginator.num_pages)

    return render(request,'index1.html', {'posts': posts})

