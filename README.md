Django Admin Inline Paginator Plus ⏩
=====================================

**🍴 This is a forked and updated version based on original library [django-admin-inline-paginator](https://github.com/shinneider/django-admin-inline-paginator).**

> *As for 10.07.2024 nobody took responsibility, so I decided to take it since we need additional functionlity like AJAX for pagination.*

The **"Django Admin Inline Paginator Plus"** is simple way to paginate your inline in django admin

To keep Django ecosystem fresh and updated, please share your love and support, click `Star` 🫶

## Features
- **Easy Inline Pagination:** Quickly paginate inlines in the Django admin.
- **AJAX Support:** Smooth and dynamic pagination without page reloads with `htmx`.
- **Multiple Inline Pagination:** Manage multiple paginated inlines seamlessly.


Here's a screenshot of the paginated inlines in action:

![Django Admin Inline Paginator Plus screenshot](https://github.com/DmytroLitvinov/django-admin-inline-paginator-plus/blob/bd4d0eb435ae86b37473044a6d192405c3f0c86f/example/django-admin-inline-paginator-plus.png "Screenshot of Django Admin Inline Paginator Plus")


# Install:

Install the package via pip:

```bash
pip install django-admin-inline-paginator-plus
```

# Usage:

1. Add to your INSTALLED_APPS, in settings.py:

   ```
   INSTALLED_APPS = [
       ...
       'django_admin_inline_paginator_plus',
       ...
   ]
   ```
2. Create your model inline:

    You can use `TabularInlinePaginated` ot `StackedInlinePaginated`. In our example we use `TabularInlinePaginated`.

   ```
   from django_admin_inline_paginator_plus.admin import TabularInlinePaginated

   class ModelWithFKAdminInline(TabularInlinePaginated):
       model = ModelWithFK
       fields = (...)
       per_page = 5
   ```

3. Create main model admin and use inline:

    ```
    @register(YourModel)
    class YourModelAdmin(ModelAdmin):
        model = YourModel
        fields = (...)
        inlines = (ModelWithFKAdminInline, )
    ```

# Advanced Usage:

1. Paginate multiples inlines:

    ```
    from django_admin_inline_paginator_plus.admin import TabularInlinePaginated, StackedInlinePaginated

    class ModelWithFKInline(TabularInlinePaginated):
       model = ModelWithFK
       fields = ('name', 'active')
       per_page = 2
       pagination_key = 'page-model'  # make sure it's unique for page inline

    class AnotherModelWithFKInline(StackedInlinePaginated):
       model = AnotherModelWithFK
       fields = ('name', 'active')
       per_page = 2
       pagination_key = 'page-another-model'  # make sure it's unique for page inline
    ```

2. Use inlines from step 1. and add to your main model admin:

    ```
    @register(YourModel)
    class YourModelAdmin(ModelAdmin):
        model = YourModel
        fields = (...)
        inlines = (ModelWithFKAdminInline, AnotherModelWithFKInline)
    ```
