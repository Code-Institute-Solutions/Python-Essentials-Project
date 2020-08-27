from scraper import JobScrape

mon = JobScrape("monster")

print("Working...")

mon_results = mon.get_jobs("dublin", "ie", "python,developer")

for result in mon_results:
    print(f"Job Title: {result['title']}")
    print(f"Company: {result['company']}")
    print(f"URL: {result['url']}")
    if "description" in result:
        print(f"Description: {result['description']}")

print(f"{len(mon_results)} jobs found")
