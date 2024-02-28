from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from dotenv import load_dotenv, find_dotenv
from os import getenv

_: bool = load_dotenv(find_dotenv())

postgres_url = getenv("POSTGRES_URL")
engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")

def create_heroes():
    with Session(engine) as session:
        # Create team instances
       # stmt = select(Hero).join(Team).where(Team.name == "team_Paak")
        team_Paak = Team(name="Pak_fighter", headquarters="minar_e_pak")
        # team_India = Team(name="Ind_fighter", headquarters="taj_mahal")

        # Create hero instances
        # hero_Rj = Hero(name="if", secret_name="afaq", team=team_Paak)
        # hero_Jsh = Hero(name="Raj", secret_name="Rajesh_khana",  team=team_India)
        hero_cptn_america = Hero(name="Captain America", secret_name="Steve Rogers")
        # Add objects to the session
        # session.add_all([team_Paak, team_India, hero_Rj, hero_Jsh])
        hero_cptn_america.team = team_Paak
        session.add(hero_cptn_america)
        # Commit the transaction
        session.commit() 



def main():
    
    # create_db_and_tables()
    create_heroes()
    # select_heroes()
    # select_heroes_by_join()
    # update_heroes()
   


if __name__ == "__main__":
    main()  