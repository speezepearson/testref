import argparse
import json
from pathlib import Path

from aiohttp import web
from google.protobuf import json_format as jsonpb

from . import Server
from .protobuf import status_pb2


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=8080)
parser.add_argument('-H', '--host', default='localhost')
parser.add_argument('testcase_results', type=Path)
args = parser.parse_args()

statuses = jsonpb.ParseDict(json.load(args.testcase_results.open()), status_pb2.Tests())

print(statuses)

app = web.Application()
app.add_routes(Server(statuses).routes())

web.run_app(app, host=args.host, port=args.port)
