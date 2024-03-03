from django.shortcuts import render
import json

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def parse_input(input_str):
    lines = input_str.split('\n')
    root = None
    nodes = {}

    for line in lines:
        parts = line.strip().split(' = ')
        parent_name = parts[0].split('.')[0]
        child_name = parts[1]

        if parent_name == 'root':
            root = Node(child_name)
            nodes[child_name] = root
        else:
            parent_node = nodes[parent_name]
            child_node = Node(child_name)
            parent_node.children.append(child_node)
            nodes[child_name] = child_node

    return root

def tree_to_json(node):
    json_tree = {
        "name": node.name,
        "children": [tree_to_json(child) for child in node.children]
    }
    return json_tree



def dynamic_tree_view(request):
    
    dynamic_data = []
    if request.method == "GET":
        input_data = ""
    if request.method == 'POST':
        input_data = ""
        input_data = request.POST.get('dictionaryInput')
        # print(input_data)
        input_data = input_data = input_data.strip()
        root = parse_input(input_data)
        print(root)

        json_tree = tree_to_json(root)
        print(json_tree)
        compiled_data ="["+json.dumps(json_tree)+"]"
        # mymain = []
        # mymain.append(json_tree)
        print(compiled_data)
        if compiled_data:
            try:
                dynamic_data = json.loads(compiled_data)
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
    return render(request, 'index.html', {'dynamic_data': dynamic_data,'old_txt':input_data})
