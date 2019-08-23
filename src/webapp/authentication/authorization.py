def process_roles(details, user, **kwargs):
    user.is_staff = True
    user.is_superuser = True
    user.save()
