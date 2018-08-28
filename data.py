#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item, Category

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
categories = [Category(name="Crime"), Category(name="Drama"),
              Category(name="Action"), Category(name="Thriller"),
              Category(name="Comedy"), Category(name="Adventure"),
              Category(name="Animation"), Category(name="Horror"),
              Category(name="Mystery"), Category(name="Biography")]
users = [User(email="ms10596@gmail.com", name="Mohamed Sayed",
              password="password")]

items = [Item(name="Twin Peaks", categoryId=1, userId=1,
              description="An idiosyncratic FBI agent investigates "
                          "the murder of a young woman in the even "
                          "more idiosyncratic town of Twin Peaks."),
         Item(name="The Sopranos", categoryId=1, userId=1,
              description="New Jersey mob boss Tony Soprano deals "
                          "with personal and professional issues "
                          "in his home and business life that affect"
                          " his mental state, leading him to seek "
                          "professional psychiatric counseling."),
         Item(name="Game of Thrones", categoryId=3, userId=1,
              description="Nine noble families fight for control "
                          "over the mythical lands of Westeros, "
                          "while an ancient enemy returns after "
                          "being dormant for thousands of years."),
         Item(name="Breaking Bad", categoryId=4, userId=1,
              description="A high school chemistry teacher diagnosed "
                          "with inoperable lung cancer turns to "
                          "manufacturing and selling methamphetamine "
                          "in order to secure his family's future."),
         Item(name="The Larry Sanders Show", categoryId=5, userId=1,
              description="A comedic behind the scenes look at a "
                          "late night talk show."),
         Item(name="Curb Your Enthusiasm ", categoryId=5, userId=1,
              description="The life and times of Larry David and "
                          "the predicaments he gets himself into "
                          "with his friends and complete strangers."),
         Item(name="Lost", categoryId=6, userId=1,
              description="The survivors of a plane crash are "
                          "forced to work together in order to "
                          "survive on a seemingly deserted tropical island."),
         Item(name="Louie", categoryId=2, userId=1,
              description="The life of Louie C.K., a divorced "
                          "comedian living in New York with two kids."),
         Item(name="Cheers", categoryId=5, userId=1,
              description="The regulars of the Boston bar Cheers "
                          "share their experiences and lives with "
                          "each other while drinking or working at "
                          "the bar where everybody knows your name."),
         Item(name="Scener ur ett aktenskap", categoryId=2, userId=1,
              description="Ten years within the marriage of Marianne "
                          "and Johan."),
         Item(name="Buffy the Vampire Slayer", categoryId=3, userId=1,
              description="A young woman is forced to fulfill her "
                          "destiny of fighting vampires and demons with "
                          "the help of her friends all the while struggling "
                          "to live a normal teenage life of heart"
                          " break and drama."),
         Item(name="The Shield", categoryId=1, userId=1,
              description="Follows the lives and cases of a dirty Los Angeles"
                          " Police Department cop and the "
                          "unit under his command."),
         Item(name="Deadwood", categoryId=1, userId=1,
              description="A show set in the late 1800s, revolving around "
                          "the characters of Deadwood, South Dakota;"
                          " a town of deep corruption and crime."),
         Item(name="The Marvelous Mrs. Maisel ", categoryId=5, userId=1,
              description="A housewife in the 1950s decides to become a "
                          "stand-up comic."),
         Item(name="Horace and Pete", categoryId=2, userId=1,
              description="Louis C.K.'s Eugene O'Neill-esque dramedic web "
                          "series about two brothers, introverted Horace"
                          " and mentally ill Pete, the current owners of"
                          " their family's Irish bar Horace and Pete's, and"
                          " their dysfunctional family and friends."),
         Item(name="Top of the Lake", categoryId=9, userId=2,
              description="Obsessed with the disappearance of a"
                          " 12-year-old pregnant girl near a "
                          "freezing lake in New Zealand, a brave "
                          "detective will find herself up against small-town"
                          " secrets and a side of herself that was "
                          "meticulously kept at bay."),
         Item(name="The Simpsons", categoryId=7, userId=2,
              description="The satiric adventures of a working-class"
                          " family in the misfit city of Springfield."),
         Item(name="The Walking Dead", categoryId=8, userId=2,
              description="Sheriff Deputy Rick Grimes wakes up from "
                          "a coma to learn the world is in ruins, and "
                          "must lead a group of survivors to stay alive."),
         Item(name="The Wire", categoryId=4, userId=2,
              description="Baltimore drug scene, seen through the eyes of "
                          "drug dealers and law enforcement."),
         Item(name="Welt am Draht", categoryId=9, userId=2,
              description="Somewhere in the future there is a computer "
                          "project called Simulacron one of which is able "
                          "to simulate a full featured reality, when suddenly "
                          "project leader Henry Vollmer dies."),
         Item(name="House of Cards", categoryId=2, userId=2,
              description="A Congressman works with his equally"
                          " conniving wife "
                          "to exact revenge on the people who betrayed him."),
         Item(name="Fargo", categoryId=4, userId=2,
              description="Various chronicles of deception,"
                          " intrigue and murder "
                          "in and around frozen Minnesota. Yet all of these "
                          "tales mysteriously lead back one way or another to "
                          "Fargo, North Dakota."),
         Item(name="Angel", categoryId=3, userId=2,
              description="The vampire Angel, cursed with a soul, moves to "
                          "Los Angeles and aids people with "
                          "supernatural-related"
                          " problems while questing for his own redemption."),
         Item(name="V", categoryId=6, userId=2,
              description="A year after Liberation Day, courtesy "
                          "of the red-dust bacteria, the humanoid, "
                          "lizard-like aliens develop a resistance "
                          "to the micro-organism and try to regain "
                          "control of the Earth--only now some humans "
                          "are knowingly working with them."),
         Item(name="Jessica Jones", categoryId=3, userId=2,
              description="Following the tragic end of her brief "
                          "superhero career, Jessica Jones tries to "
                          "rebuild her life as a private investigator, "
                          "dealing with cases involving people with "
                          "remarkable abilities in New York City."),
         Item(name="Daredevil", categoryId=1, userId=2,
              description="Matt Murdock, with his other "
                          "senses superhumanly enhanced, "
                          "fights crime as a blind lawyer by day,"
                          " and vigilante by night."),
         Item(name="Seinfield", categoryId=5, userId=2,
              description="The continuing misadventures of neurotic"
                          " New York City stand-up comedian Jerry "
                          "Seinfeld and his equally neurotic "
                          "New York City friends."),
         Item(name="Slings and Arrows", categoryId=5, userId=2,
              description="In the fictional town of New Burbage,"
                          " legendary theatrical madman Geoffrey Tennant "
                          "returns to the New Burbage Theatre Festival, "
                          "the site of his greatest triumph and most "
                          "humiliating failure.."),
         Item(name="I, Claudius ", categoryId=10, userId=2,
              description="The history of the Roman Empire as "
                          "experienced by one of its rulers."),
         Item(name="Rome", categoryId=10, userId=2,
              description="A down-to-earth account of the lives of both "
                          "illustrious and ordinary Romans set in the "
                          "last days of the Roman Republic.")]
for category in categories:
    session.add(category)
session.commit()

for item in items:
    session.add(item)
session.commit()

for user in users:
    session.add(user)
session.commit()
