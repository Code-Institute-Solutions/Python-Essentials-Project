# from scraper import JobScrape

# mon = JobScrape("monster")

# mon_results = mon.get_jobs("dublin", "ie", "python,developer")

# print(mon_results)

from requests_html import HTMLSession

s = HTMLSession()

r = s.get("https://job-openings.monster.ie/senior-python-developer-back-end-saas-analytics-platform-dublin-dublin-ie-stelfox/219182048")

print(r.html.html)
