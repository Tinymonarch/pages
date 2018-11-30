#__author__ : Administrator
#__date__: 2018/11/30 0030

class Pagination(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=30, maxPageNum=7):
        #数据总个数
        self.total_count = totalCount
        #当前页
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        #每页显示行数
        self.per_page_item_num = perPageItemNum
        #最多显示页面
        self.max_page_num = maxPageNum

    def start(self):
        return (self.current_page-1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):
        #总页数
        a,b =divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a+1

    def pager_num_range(self):
        # 当前页： self.current_page
        # 最多显示的页码数量 self.per_page_num
        # 总页数 num_pages
        if self.num_pages <= self.max_page_num:
            return range(1, self.num_pages+1)
        #总页数特别多
        part = int(self.max_page_num/2)
        if self.current_page <= part:
            return range(1, self.max_page_num+1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages - self.max_page_num, self.num_pages+1)
        return range(self.current_page-part, self.current_page+part+1)

    def page_str(self):
        page_list = []

        first = "<a href='/index2.html?p=1'>首页</a>"
        page_list.append(first)

        if self.current_page == 1:
            prev = "<a href='#'>上一页</a>"
        else:
            prev = "<a href='/index2.html?p=%s'>上一页</a>" %(self.current_page - 1)
        page_list.append(prev)

        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<a style='font-size:30px' href='/index2.html?p=%s'>%s<a/>" % (i, i)
            else:
                temp = "<a href='/index2.html?p=%s'>%s<a/>" %(i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            nex = "<a href='#'>下一页</a>"
        else:
            nex = "<a href='/index2.html?p=%s'>下一页</a>" %(self.current_page + 1)
        page_list.append(nex)

        return ''.join(page_list)
