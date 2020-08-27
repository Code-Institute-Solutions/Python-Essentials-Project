class JobScrape():

    def __init__(self, site_name):
        """
        Having the job sites in a list means we can
        check on initialisation and throw an error
        if the site is not available.
        """

        sites = [{"monster":
                  {"url": "https://www.monster.ie/jobs/search/",
                   "query_format": "?q={keywords}&where={city}&cy={country}",
                   "results": "#SearchResults",
                   }}]

    def _format_monster():
        pass

    def _get_description():
        pass

    def _scrape_site():
        pass

    def get_jobs():
        pass
