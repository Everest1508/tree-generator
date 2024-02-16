from django.shortcuts import render

# Create your views here.

import json

def dynamic_tree_view(request):
    
    dynamic_data = []
    if request.method == 'POST':
        input_data = request.POST.get('dictionaryInput')
        print(input_data)
        if input_data:
            try:
                dynamic_data = json.loads(input_data)
            except json.JSONDecodeError:
                # Handle invalid JSON data
                pass
    
    
    # dynamic_data = [
    #     {
    #         'name': 'Home',
    #         'children': [
    #             {
    #                 'name': 'About us',
    #                 'children': [
    #                     {
    #                         'name': 'Our history',
    #                         'children': [{'name': 'Founder'}]
    #                     },
    #                     {
    #                         'name': 'Our board',
    #                         'children': [
    #                             {'name': 'Brad Whiteman'},
    #                             {'name': 'Cynthia Tolken'},
    #                             {'name': 'Bobby Founderson'}
    #                         ]
    #                     }
    #                 ]
    #             },
    #             {
    #                 'name': 'Our products',
    #                 'children': [
    #                     {'name': 'The Widget 2000™', 'children': [{'name': 'Order form'}]},
    #                     {'name': 'The McGuffin V2', 'children': [{'name': 'Order form'}]}
    #                 ]
    #             },
    #             {
    #                 'name': 'Contact us',
    #                 'children': [{'name': 'Social media', 'children': [{'name': 'Facebook'}]}]
    #             }
    #         ]
    #     }
    # ]
    return render(request, 'index.html', {'dynamic_data': dynamic_data})
