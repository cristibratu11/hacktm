import smmrpy
import aiohttp
import asyncio
import re
import analyzer

my_list = []
async def fetch():
    s = smmrpy.SMMRPY('8B1BD1A777') # Instantiate the SMMRPY instance.
    article = await s.get_smmry('https://edition.cnn.com/2018/05/11/middleeast/iran-israel-syria-intl/index.html')
    print(article.title) # Print the title of the found article.
    a = article.content
    my_list = a.split(".")
    for sent in my_list:
        analyzer.analyze(sent)

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch())
loop.close()
