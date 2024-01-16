from site_setup.models import MenuLink, SiteSetup


def context_processor_example(request):
    return {
        'example': 'Veio do context processor (example)'
    }


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    menu_link = MenuLink.objects.all()

    return {
        'site_setup': setup,
        'menu_link': menu_link
    }