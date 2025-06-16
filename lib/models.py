from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


Base = declarative_base()

class Players(Base):
    __tablename__ = "players"
    id = Column(Integer(), primary_key=True)
    username = Column(String())
    level = Column(Integer())
    experience = Column(String())
    money = Column(Float())

    playermonsters = relationship("Player_Monsters", back_populates="player")


class Monster_Species(Base):
    __tablename__ = "monsters"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type_monster = Column(String())
    base_stats = Column(Integer())
    rarity = Column(String())
    abilities = Column(String())

    players = relationship("Player_Monsters", back_populates="monster")


class Player_Monsters(Base):
    __tablename__ = "playermonster"
    id = Column(Integer(), primary_key=True)
    player_id = Column(Integer(), ForeignKey("players.id"))
    monster_id = Column(Integer(), ForeignKey("monsters.id"))
    level = Column(Integer())
    experience = Column(String())

    player = relationship("Players", back_populates="playermonsters")
    monster = relationship("Monster_Species", back_populates="players")
    
class Battles(Base):
    __tablename__ = ""
    
    
    