import asyncio
from Wg_web_client.client import WireGuardWebClient


async def main():
    client = WireGuardWebClient("45.8.98.193:51821", "./downloads")
    await client.create_key("2323")



if __name__ == "__main__":
    asyncio.run(main())