from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    try:
        return user.groups.filter(name=group_name).exists()
    except Exception as e:
        print("Error al validar el grupo del usuario.")
        print(e)