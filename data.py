from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item, Category

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
categories = [Category(category="Crime"), Category(category="Drama"), Category(category="Action"), Category(category="Thriller"), Category(category="Comedy"),
              Category(category="Adventure"), Category(category="Fantasy"), Category(category="History"), Category(category="Animation"),
              Category(category="Horror"), Category(category="Mystery"), Category(category="Biography")]
for category in categories:
    session.add(category)
session.commit()

items = []
items.append(Item(name="Twin Peaks", categoryId=1,
                  description="An idiosyncratic FBI agent investigates the murder of a young woman in the even more idiosyncratic town of Twin Peaks.",
                  userId=1))
items.append(Item(name="The Sopranos", categoryId=1,
                  description="New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect his mental state, leading him to seek professional psychiatric counseling.",
                  userId=1))
items.append(Item(name="Game of Thrones", categoryId=1,
                  description="Nine noble families fight for control over the mythical lands of Westeros, while an ancient enemy returns after being dormant for thousands of years.",
                  userId=1))
items.append(Item(name="Breaking Bad", categoryId=2,
                  description="A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.",
                  userId=1))
items.append(Item(name="The Larry Sanders Show", categoryId=2,
                  description="A comedic behind the scenes look at a late night talk show.", userId=1))
items.append(Item(name="Curb Your Enthusiasm ", categoryId=2,
                  description="The life and times of Larry David and the predicaments he gets himself into with his friends and complete strangers.",
                  userId=1))
items.append(Item(name="Lost", categoryId=3,
                  description="The survivors of a plane crash are forced to work together in order to survive on a seemingly deserted tropical island.",
                  userId=1))
items.append(Item(name="Louie", categoryId=3,
                  description="The life of Louie C.K., a divorced comedian living in New York with two kids.",
                  userId=1))
items.append(Item(name="Cheers", categoryId=3,
                  description="The regulars of the Boston bar Cheers share their experiences and lives with each other while drinking or working at the bar where everybody knows your name.",
                  userId=1))
items.append(Item(name="Scener ur ett aktenskap", categoryId=4,
                  description="Ten years within the marriage of Marianne and Johan.", userId=1))
items.append(Item(name="Buffy the Vampire Slayer", categoryId=4,
                  description="A young woman is forced to fulfill her destiny of fighting vampires and demons with the help of her friends all the while struggling to live a normal teenage life of heart break and drama.",
                  userId=1))
items.append(Item(name="The Shield", categoryId=4,
                  description="Follows the lives and cases of a dirty Los Angeles Police Department cop and the unit under his command.",
                  userId=1))
items.append(Item(name="Deadwood", categoryId=5,
                  description="A show set in the late 1800s, revolving around the characters of Deadwood, South Dakota; a town of deep corruption and crime.",
                  userId=1))
items.append(Item(name="The Marvelous Mrs. Maisel ", categoryId=5,
                  description="A housewife in the 1950s decides to become a stand-up comic.", userId=1))
items.append(Item(name="Horace and Pete", categoryId=5,
                  description="Louis C.K.'s Eugene O'Neill-esque dramedic web series about two brothers, introverted Horace and mentally ill Pete, the current owners of their family's Irish bar Horace and Pete's, and their dysfunctional family and friends.",
                  userId=1))
items.append(Item(name="Top of the Lake", categoryId=6,
                  description="Obsessed with the disappearance of a 12-year-old pregnant girl near a freezing lake in New Zealand, a brave detective will find herself up against small-town secrets and a side of herself that was meticulously kept at bay.",
                  userId=1))
items.append(Item(name="The Simpsons", categoryId=6,
                  description="The satiric adventures of a working-class family in the misfit city of Springfield.",
                  userId=1))
items.append(Item(name="The Walking Dead", categoryId=6,
                  description="Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins, and must lead a group of survivors to stay alive.",
                  userId=1))
items.append(Item(name="The Wire", categoryId=7,
                  description="Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.",
                  userId=1))
items.append(Item(name="Welt am Draht", categoryId=7,
                  description="Somewhere in the future there is a computer project called Simulacron one of which is able to simulate a full featured reality, when suddenly project leader Henry Vollmer dies.",
                  userId=1))
items.append(Item(name="House of Cards", categoryId=7,
                  description="A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.",
                  userId=1))
items.append(Item(name="Fargo", categoryId=8,
                  description="Various chronicles of deception, intrigue and murder in and around frozen Minnesota. Yet all of these tales mysteriously lead back one way or another to Fargo, North Dakota.",
                  userId=1))
items.append(Item(name="Angel", categoryId=9,
                  description="The vampire Angel, cursed with a soul, moves to Los Angeles and aids people with supernatural-related problems while questing for his own redemption.",
                  userId=1))
items.append(Item(name="V", categoryId=9,
                  description="A year after Liberation Day, courtesy of the red-dust bacteria, the humanoid, lizard-like aliens develop a resistance to the micro-organism and try to regain control of the Earth--only now some humans are knowingly working with them.",
                  userId=1))
items.append(Item(name="Jessica Jones", categoryId=8,
                  description="Following the tragic end of her brief superhero career, Jessica Jones tries to rebuild her life as a private investigator, dealing with cases involving people with remarkable abilities in New York City.",
                  userId=1))
items.append(Item(name="Daredevil", categoryId=10,
                  description="Matt Murdock, with his other senses superhumanly enhanced, fights crime as a blind lawyer by day, and vigilante by night.",
                  userId=1))
items.append(Item(name="Seinfield", categoryId=11,
                  description="The continuing misadventures of neurotic New York City stand-up comedian Jerry Seinfeld and his equally neurotic New York City friends.",
                  userId=1))
items.append(Item(name="Slings and Arrows", categoryId=11,
                  description="In the fictional town of New Burbage, legendary theatrical madman Geoffrey Tennant returns to the New Burbage Theatre Festival, the site of his greatest triumph and most humiliating failure..",
                  userId=1))
items.append(Item(name="I, Claudius ", categoryId=12,
                  description="The history of the Roman Empire as experienced by one of its rulers.", userId=1))
items.append(Item(name="Rome", categoryId=12,
                  description="A down-to-earth account of the lives of both illustrious and ordinary Romans set in the last days of the Roman Republic.",
                  userId=1))

for i in items:
    session.add(i)
session.commit()
