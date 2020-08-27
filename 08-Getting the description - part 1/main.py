from scraper import JobScrape

mon = JobScrape("monster")

mon_results = mon.get_jobs("dublin", "ie", "python,developer")

print(mon_results)
