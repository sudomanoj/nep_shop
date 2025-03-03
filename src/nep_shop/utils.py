
def unique_slugify(instance, slug):
    """
    This function takes an instance and a slug and returns a unique slug by adding a 
    random string at the end of the slug if the slug already exists in the database.
    """
    model = instance.__class__
    unique_slug = slug
    counter = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{slug}-{counter}'
        counter += 1
    return unique_slug