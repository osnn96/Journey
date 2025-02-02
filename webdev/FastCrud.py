from fastapi import FastAPI, Body, Query, Path, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status


app = FastAPI()

drivers_db = [
    {'id' : 1, 'driver': 'Osman', "title" : "num1_driver", "team": "IUC-Racing", "rating": 9},
    {'id' : 2, 'driver': 'Mert', "title" : "num2_driver", "team": "IUC-Racing", "rating": 9},
    {'id' : 3, 'driver': 'Frog', "title" : "num2_driver", "team": "DogGo-Racing", "rating": 2},
    {'id' : 4, 'driver': 'Dog', "title" : "num1_driver", "team": "DogGo-Racing", "rating": 1},
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/drivers")
async def drivers():
    return drivers_db

@app.get("/drivers/rating")
async def drivers_by_rating(rating: int = Query(gt=0, lt=10)):
    selected_drivers = []
    for selected in drivers_db:
        if selected.get('rating') == rating:
            selected_drivers.append(selected)
    return selected_drivers 
 


@app.get("/drivers/{id}")
async def drivers(id: int = Path(gt=0, lt=3)):
    for driver in drivers_db:
        if driver.get('id') == id:
            return driver
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver not found")


@app.get("/drivers/byteam/{team}")
async def drivers(team: str):
    counter = 0
    for ofteam in drivers_db:
        if ofteam.get('team').casefold() == team.casefold():
            counter += 1
    return {"for selected team": f"ther are {counter} driver for the selected {team}"}


@app.get("/drivers/")
async def drivers(team_selected : str):
    selected = []
    for team in drivers_db:
        if team['team'].casefold() == team_selected.casefold():
            selected.append(team)
    return selected

# path & query combined
@app.get("/drivers_by/{team}")
async def drivers_by_team(team_selected : str, title: str):
    selected = []
    for team in drivers_db:
        if (team['team'].casefold() == team_selected.casefold()
                and team['title'] == title.casefold()):
            selected.append(team)
    return selected

@app.post("/drivers/add_driver")
async def add_driver(new_driver = Body()):
    drivers_db.append(new_driver)
    return {"successfully added new driver": new_driver}

@app.put("/drivers/update_driver")
async def update_driver(updated_driver = Body()):
    for index in range(len(drivers_db)):
        if drivers_db[index].get('id') == updated_driver.get('id'):
            drivers_db[index] = updated_driver
    return {"successfully updated driver"  : updated_driver}

@app.delete("/drivers/delete_driver/{id}")
async def delete_driver(id: int):
    for index in range(len(drivers_db)):
        if drivers_db[index].get('id') == id:
            drivers_db.pop(index)
            break
    return {"successfully deleted driver": f"with id {id}"}
