from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session, select
from dotenv import load_dotenv, find_dotenv
from os import getenv

_: bool = load_dotenv(find_dotenv())


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


postgres_url = getenv("POSTGRES_URL")

engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).join(Team, isouter=True)
        results = session.exec(statement)
        # for hero, team in results:
        #     print("Hero:", hero, "Team:", team)

        heroes = results.all()
        print(heroes)



# choose single hero from team by join

def select_heroes_by_join():
    with Session(engine) as session:
        statmt = select(Hero).join(Team).where(Team.name == "Avengers")
        results = session.exec(statmt)
        for hero in results:
            print("Hero:", hero)

        heroes = results.first()
        print(heroes)
        

# def create_heroes():
#     with Session(engine) as session:
#         team_Avengers = Team(name="Avengers", headquarters="California")
#         team_Justice_league = Team(name="Justice league", headquarters="New York")
#         session.add(team_Avengers)
#         session.add(team_Justice_league)
#         session.commit()

#         hero_1 = Hero(name="BB", secret_name="Hulk",team_id=team_Avengers.id)
#         hero_2 = Hero(name="CC", secret_name="SpiderMan", team_id=team_Justice_league.id)
        #  hero_3= Hero(name="DD", secret_name="Black Panther")
        # hero_3.team_id = team_Avengers.id

#         session.add(hero_1)
#         session.add(hero_2)
#         session.add(hero_3)
#         session.commit()
        
# hero with no team_id will update with team_id




















def main():
    pass
    # create_db_and_tables()
    # create_heroes()
    # select_heroes()
    # select_heroes_by_join()
    update_heroes()
   


if __name__ == "__main__":
    main()    