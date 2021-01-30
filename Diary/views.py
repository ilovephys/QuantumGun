from django.shortcuts import render
from django.views import generic

from .models import BlogModel6, aboutModel, aboutQGModel

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class EntranceView(generic.TemplateView):
    template_name = "entrance.html"

class BlogList(generic.ListView):
    template_name = "BlogList.html"
    model = BlogModel6
    ordering = ['-postdate']

def arXiv(request):
    objectArXiv = BlogModel6.objects.all().order_by("-postdate")
    """
    ブログの月刊アーカイブを作成
    """
    # 日付順に記事をソート
    DTLsorted = [data.postdate for data in objectArXiv]
    #for data in objectArXiv:
        #DTLsorted.append(data.postdate)

    # 同じ月に投稿された記事とその個数を抽出
    baseYear = DTLsorted[0].year
    baseMonth = DTLsorted[0].month
    count = 0
    sort2 = []

    for i in range(len(DTLsorted)):
        if i == len(DTLsorted) - 1:
            count += 1
            sort2.append([baseYear, baseMonth, count])
        else:
            if DTLsorted[i].year == baseYear:
                if DTLsorted[i].month == baseMonth:
                    count += 1
                else:
                    sort2.append([baseYear, baseMonth, count])
                    count = 1
                    baseMonth = DTLsorted[i].month
            else:
                sort2.append([baseYear, baseMonth, count])
                count = 1
                baseYear = DTLsorted[i].year
                baseMonth = DTLsorted[i].month
    return sort2

def allBlogList(request):
    objectList = BlogModel6.objects.all()
    objectFamousArticle = BlogModel6.objects.filter().values().order_by("-pageView")
    objectArXiv = arXiv(request)

    return render(
        request,
        "BlogList.html",
        {
            "objectList": objectList,
            "objectFamousArticle": objectFamousArticle,
            "objectArXiv": objectArXiv
        }
    )

def blogList(request, SUBNAME):
    objectList = BlogModel6.objects.filter(category=SUBNAME)
    objectFamousArticle = BlogModel6.objects.filter().values().order_by("-pageView")
    objectArXiv = arXiv(request)

    return render(
        request,
        "BlogList.html",
        {
            "objectList": objectList,
            "objectFamousArticle": objectFamousArticle,
            "objectArXiv": objectArXiv
        }
    )

def BlogDetail(request, pk):
    object1 = BlogModel6.objects.get(pk=pk)
    objectFamousArticle = BlogModel6.objects.filter().values().order_by("-pageView")
    objectArXiv = arXiv(request)
    objectRelationArticle = BlogModel6.objects.filter(category=object1.category)

    object1.pageView += 1
    object1.save()

    objectLinkList = [
        object1.link,
        object1.link2,
        object1.link3,
        object1.link4,
        object1.link5
    ]

    contents = {
        "object1": object1,
        "objectFamousArticle": objectFamousArticle,
        "objectArXiv": objectArXiv,
        "objectRelationArticle": objectRelationArticle
    }

    INT = 0
    for LinkCard in objectLinkList:
        if LinkCard is not None:
            contents["objectLink"+str(INT)] = BlogModel6.objects.get(pk=LinkCard)
        INT+=1

    return render(
        request,
        "BlogDetail.html",
        contents
    )

def about(request):
    object1 = aboutModel.objects.get()
    objectFamousArticle = BlogModel6.objects.filter().values().order_by("-pageView")
    objectArXiv = arXiv(request)

    object1.pageView += 1
    object1.save()

    objectLinkList = [
        object1.link,
        object1.link2,
        object1.link3,
        object1.link4,
        object1.link5
    ]
    contents = {
        "object1": object1,
        "objectFamousArticle": objectFamousArticle,
        "objectArXiv": objectArXiv
    }

    INT = 0
    for LinkCard in objectLinkList:
        if LinkCard is not None:
            contents["objectLink"+str(INT)] = BlogModel6.objects.get(pk=LinkCard)
        INT+=1

    return render(
        request,
        "Entrance/about.html",
        contents
    )
def aboutQG(request):
    object1 = aboutQGModel.objects.get()
    objectFamousArticle = BlogModel6.objects.filter().values().order_by("-pageView")
    objectArXiv = arXiv(request)

    object1.pageView += 1
    object1.save()

    objectLinkList = [
        object1.link,
        object1.link2,
        object1.link3,
        object1.link4,
        object1.link5
    ]
    print(objectLinkList, "¥n@@@@@@@@")
    contents = {
        "object1": object1,
        "objectFamousArticle": objectFamousArticle,
        "objectArXiv": objectArXiv
    }

    INT = 0
    for LinkCard in objectLinkList:
        if LinkCard is not None:
            contents["objectLink"+str(INT)] = BlogModel6.objects.get(pk=LinkCard)
        INT+=1

    return render(
        request,
        "Entrance/about.html",
        contents
    )