from fastapi import FastAPI, Body, Query, Path, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Teams:
    id: int
    team_name : str
    team_boss : str
    ranking : int
    founded_date : int

    def __init__(self,id : int, team_name : str, team_boss : str, ranking: int, founded_date: int):
        self.id = id
        self.team_name = team_name
        self.team_boss = team_boss
        self.ranking = ranking
        self.founded_date = founded_date


class TeamRequest(BaseModel):
    id : Optional[int] = Field(description="The id of the team, optional", default=None)
    team_name : str = Field(min_length=3, max_length=50)
    team_boss : str = Field(min_length=3)
    ranking : Optional[int] = Field(gt=0, lt=11)
    founded_date : int = Field(ge=1940, le=2025)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "team_name": "Redbull",
                "team_boss": "Horner",
                "ranking": 5,
                "founded_date": 2005
            }
        }
    }


teams_db = [
    Teams(id=1, team_name="Redbull", team_boss="Horner", ranking=5, founded_date=2005),
    Teams(id=2, team_name="Ferrari", team_boss="Vaseur", ranking=5, founded_date=1950),
    Teams(id=3, team_name="Mercedes", team_boss="Toto", ranking=4, founded_date=1960),
    Teams(id=4, team_name="Aston Martin", team_boss="Andy", ranking=3.5, founded_date=1970),
    Teams(id=5, team_name="Alpine", team_boss="Dolandırıcı Briatore", ranking=3, founded_date=2005),    
]

@app.get("/teams/")
async def get_teams():
    return teams_db


@app.post("/create_team/", status_code=status.HTTP_201_CREATED)
async def create_team(team: TeamRequest):   
    new_team = Teams(**team.model_dump())
    teams_db.append(find_team_id(new_team))

def find_team_id(team : Teams):
    team.id = 1 if len(teams_db) == 0 else teams_db[-1].id + 1
    return team

@app.post("/teams/update_team", status_code=status.HTTP_204_NO_CONTENT)
async def update_team(team: TeamRequest):
    team_updated = False
    for i in range(len(teams_db)):
        if teams_db[i].id == team.id:
            teams_db[i] = team
            team_updated = True
    if not team_updated:
        raise HTTPException(status_code=404, detail="Team not found")

@app.delete("/teams/delete_team/{team_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_team(team_id: int = Path(gt=0)):
    team_deleted = False
    for i in range(len(teams_db)):
        if teams_db[i].id == team_id:
            teams_db.pop(i)
            team_deleted = True
            break
    if not team_deleted:
        raise HTTPException(status_code=404, detail="Team not found") 
