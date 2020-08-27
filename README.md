# Python Walkthrough

This is the source code to for the Python Essentials Walkthrough project.

We will walk the students through creating a class, which can be extended. Initially, it will scrape Monster, but other sites can be added.

## Usage

The project is based on `requests_html`, so we will need to type: `pip3 install requests_html` unless we're running it on repl.it.

After that, the following code shows how it works:

```python
from scraper import JobScrape

jobs = JobScrape("monster")
```

This initialises an instance and sets the site to "monster". A search can be performed using the only public method in the class:

```python
results = jobs.get_jobs("dublin", "ie", "python", True)
```

Arguments:

"dublin" - the city

"ie" - the ISO code of the country

"python" - a comma-separated list of keywords

True - a Boolean value determining whether to scrape the job description or not

