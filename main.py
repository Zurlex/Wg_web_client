import asyncio
from Wg_web_client.client import WireGuardWebClient


async def main():
    client = WireGuardWebClient("45.8.98.193:51821", "/path/to/chromedriver")
    link = await client.create_key("567567")
    print(link)


if __name__ == "__main__":
    asyncio.run(main())