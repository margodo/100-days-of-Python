def format_name(f_name, l_name):
#     output = f_name.title() + ' ' + l_name.title()
#     return output
    form_name = f_name.title()
    form_lname = l_name.title()
    return f'{form_name} {form_lname}'

print(format_name('dvv','JIDWN'))