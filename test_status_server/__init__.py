from pathlib import Path
import typing as t

from aiohttp import web

from .protobuf import status_pb2

class Server:
    def __init__(self, statuses: status_pb2.Tests) -> None:
        self.statuses = statuses

    def routes(self) -> t.Iterable[web.RouteDef]:
        return [
            web.get('/', self.get_index),
            web.get('/{testid}/status-icon.png', self.get_status_icon),
            # placeholder: add more route-defs here
        ]

    async def get_index(self, request: web.BaseRequest) -> web.StreamResponse:
        return web.Response(
            status=200,
            content_type='text/html',
            body='<ul>' + '\n'.join(
                f'<li><a href="/{testid}/details"> {testid} <img src="/{testid}/status-icon.png" /></a></li>'
                for testid in sorted(self.statuses.test_cases.keys())
            ) + '</ul>',
        )

    async def get_status_icon(self, request: web.BaseRequest) -> web.StreamResponse:
        test_id = request.match_info["testid"]
        test_case = self.statuses.test_cases.get(test_id)
        if test_case is None:
            return web.HTTPNotFound(reason="no such test")

        if test_case.WhichOneof("status") == "passed":
            return web.FileResponse(Path(__file__).parent / "resources" / f"green.png")
        else:
            return web.FileResponse(Path(__file__).parent / "resources" / f"red.png")
