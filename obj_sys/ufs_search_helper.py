from obj_sys.models import UfsObj
# import itertools


def search_helper(count, query):
    model_list = UfsObj.objects.filter(description_json__icontains=query, valid=True)
    # for L in range(1, count+1):
    #     for subset in itertools.permutations(words, L):
    #         count1=1
    #         query1=subset[0]
    #         while count1!=len(subset):
    #                 query1=query1+" "+subset[count1]
    #                 count1+=1
    #         model_list = entry_list | Article.objects.filter(title__icontains=query1, status=1)
    return model_list.distinct()