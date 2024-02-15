def start_spring(**kwargs):
    spring_objects = {}

    for object_, type_ in kwargs.items():

        if type_ not in spring_objects:
            spring_objects[type_] = []
        spring_objects[type_].append(object_)

    result = ''
    for t, objects in sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{t}:\n"

        for obj in sorted(objects):
            result += f'-{obj}\n'

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
