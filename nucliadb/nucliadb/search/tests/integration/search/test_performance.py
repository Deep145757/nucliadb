import asyncio
import time

from faker import Faker

from nucliadb_models.resource import NucliaDBRoles


async def test_node_performance_bottleneck(search_api, multiple_search_resource):
    async with search_api(roles=[NucliaDBRoles.READER]) as client:
        kbid = multiple_search_resource

        fake = Faker()
        times = []

        async def find_request():
            start = time.perf_counter()
            resp = await client.get(
                f"/kb/{kbid}/find", params={"query": fake.sentence()}
            )
            assert resp.status_code == 200
            duration = time.perf_counter() - start
            times.append(duration)

        async def suggest_request():
            resp = await client.get(
                f"/kb/{kbid}/suggest", params={"query": fake.sentence()}
            )
            assert resp.status_code == 200

        async def find_session():
            # Simulate a find session by calling suggest
            # a few times (while the user inputs the query)
            await suggest_request()
            await suggest_request()
            await suggest_request()
            await find_request()

        for n_sessions in [500, 750, 1000]:
            aws = [asyncio.create_task(find_session()) for _ in range(n_sessions)]
            done, _ = await asyncio.wait(aws)
            for task in done:
                if task.exception() is not None:
                    print(
                        f"Error reproduced with {n_sessions} concurrent find sessions"
                    )
                    raise task.exception()
            avg_time = sum(times) / len(times)
            print(
                f"{n_sessions} simulatneous sessions. Average find response time: {avg_time}"
            )
            times.clear()
