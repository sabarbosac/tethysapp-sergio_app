from tethys_sdk.base import TethysAppBase, url_map_maker


class SergioApp(TethysAppBase):
    """
    Tethys app class for Sergio App.
    """

    name = 'Sergio App'
    index = 'sergio_app:home'
    icon = 'sergio_app/images/icon.gif'
    package = 'sergio_app'
    root_url = 'sergio-app'
    color = '#16a085'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='sergio-app',
                controller='sergio_app.controllers.home'
            ),
        )

        return url_maps