import main
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
  Body: str

class TagsResponse(BaseModel):
  tags: List[str]

print(main.tagger.get_tags(main.tagger.get_cluster("data sql ne marche pas data sql help sql")))
app = FastAPI()

@app.get("/", response_model=TagsResponse)
def json_body_response(body: Item):
  """Renvoie les tags associés à un body
  entrée au format json"""
  print(body)
  resp = main.tagger.get_tags(main.tagger.get_cluster(body))
  print(resp)
  x = TagsResponse(tags=resp)
  return x

@app.post("/test/", response_model=TagsResponse)
def json_body_response(body: str):
  """Renvoie les tags associés à un body
  entrée au format str"""
  print(body)
  resp = main.tagger.get_tags(main.tagger.get_cluster(body))
  print(resp)
  x = TagsResponse(tags = resp)
  return x