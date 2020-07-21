"""
scraper.py
Python scraping walkthrough project using
Requests-HTML
"""

import re
from requests_html import HTMLSession


class JobScrape():
    """
    Main JobScrape class
    initialise with the name of the site you want to
    search. E.g: mj = JobScrape("monster")
    Put the names of enabled sites in the list.
    """

    def __init__(self, site):
        """
        Having the job sites in a list means we can
        check on initialisation and throw an error
        if the site is not available.
        """

        enabled_sites = ["monster"]

        if site in enabled_sites:
            self.site = site
        else:
            raise ValueError(f"{site} not found.")

    def _clean_HTML(self, string):
        """
        Private method to use regular expressions and
        remove HTML tags from the job description
        """

        return re.sub("<[^>]*>", " ", string)

    def _scrape_monster(self, city, country, keywords):
        """
        Private method to scrape the Monster website.
        Other sites would have similar structure
        """
        s = HTMLSession()

        base_url = "https://www.monster.ie/jobs/search/?q="
        keywords = keywords.split(",")
        keywords = "-".join(keywords)

        r = s.get(f"{base_url}{keywords}&where={city}&cy={country}")
        if r.html.find(".pivot.block"):
            return None
        else:
            return r.html.find("#SearchResults", first=True)

    def _get_monster_desc(self, url):
        """
        Private function to retrieve the job description
        from a URL
        """
        s = HTMLSession()

        r = s.get(url)
        result = r.html.find('div[name="sanitizedHtml"]', first=True)

        return self._clean_HTML(result.html) if result else "No description available"

    def _format_monster(self, results, desc=True):
        """
        Private method to return job details in this format:
        [{ "title": "",
           "company": "",
           "url": "",
           "description": ""}]
        Description is optional and can be controlled with
        the desc parameter
        """

        job_summaries = []
        cards = results.find(".card-content .summary")
        for card in cards:
            job = {}
            job["title"] = card.find(".title a", first=True).text
            try:
                job["company"] = card.find(".company a", first=True).text
            except:
                job["company"] = card.find(".company > span", first=True).text
            url = card.find(".title a", first=True)
            job["url"] = url.attrs["href"]
            if desc:
                job["description"] = self._get_monster_desc(url.attrs["href"])

            job_summaries.append(job)

        return job_summaries

    def get_jobs(self, city, country, keywords, desc=True):
        """
        Main method of the class. Initialises the search based
        on which site was selected.
        """
        if self.site.lower() == "monster":
            jobs = self._scrape_monster(city, country, keywords)
            results = self._format_monster(jobs, desc) if jobs else None

        return results
