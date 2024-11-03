import asyncio
from pyppeteer import launch
import os


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({"width": 1920, "height": 1080})
    await page.setContent("<h1>Hello, World!</h1>")
    await page.screenshot({'path': 'other/example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())