from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {"my_list":[

    {"restaurant_name":"kudo",
    "food_type":"fast food",
    },
    {"restaurant_name":"pizza hut",
    "food_type":"pizza",
    },
    {"restaurant_name":"chaina",
    "food_type":"chania food",
    },

],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {
            "restaurant_name":"pizza hut",
            "food_type":"pizza",
        },
    }

    return render(request, 'detail.html', context)
