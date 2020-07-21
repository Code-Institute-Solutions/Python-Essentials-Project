"""
Simple Python script to demonstrate our
JobScrape class
"""

from scraper import JobScrape

mj = JobScrape("monster")

print("Working...")
results = mj.get_jobs("dublin", "ie", "react")

if results:
    print(f"Found {len(results)} job(s)")

    for result in results:
        print(f"Job Title: {result['title']}")
        print(f"Company:   {result['company']}")
        print(f"URL:       {result['url']}")
        if "description" in result:
            print(f"Description:\n{result['description']}\n")
else:
    print("No jobs found")
