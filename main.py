import asyncio
from Wg_web_client.client import WireGuardWebClient


async def main():
    client = WireGuardWebClient("45.8.98.193:51821", "./downloads", "/path/to/chromedriver")

    status = await client.get_key_status("15494993167303")
    print(status)  # True или False

    await client.disable_key("15494993167303")


if __name__ == "__main__":
    asyncio.run(main())