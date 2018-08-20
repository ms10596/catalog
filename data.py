from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item

engine = create_engine('sqlite:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()
items = []
items.append(Item(name = "Twin Peaks", category="Crime", description="An idiosyncratic FBI agent investigates the murder of a young woman in the even more idiosyncratic town of Twin Peaks."))
items.append(Item(name="The Sopranos", category="Drama", description="New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect his mental state, leading him to seek professional psychiatric counseling."))
items.append(Item(name="Game of Thrones", category="Action", description="Nine noble families fight for control over the mythical lands of Westeros, while an ancient enemy returns after being dormant for thousands of years."))
items.append(Item(name="Breaking Bad", category="Thriller", description="A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future."))
items.append(Item(name="The Larry Sanders Show", category="Comedy", description="A comedic behind the scenes look at a late night talk show."))
items.append(Item(name="Curb Your Enthusiasm ", category="Comedy", description="The life and times of Larry David and the predicaments he gets himself into with his friends and complete strangers."))
items.append(Item(name="Lost", category="Adventure", description="The survivors of a plane crash are forced to work together in order to survive on a seemingly deserted tropical island."))
items.append(Item(name="Louie", category="Drama", description="The life of Louie C.K., a divorced comedian living in New York with two kids."))
items.append(Item(name="Cheers", category="Comedy", description="The regulars of the Boston bar Cheers share their experiences and lives with each other while drinking or working at the bar where everybody knows your name."))
items.append(Item(name="Scener ur ett aktenskap", category="Drama", description="Ten years within the marriage of Marianne and Johan."))
items.append(Item(name="Buffy the Vampire Slayer", category="Fantasy", description="A young woman is forced to fulfill her destiny of fighting vampires and demons with the help of her friends all the while struggling to live a normal teenage life of heart break and drama."))
items.append(Item(name="The Shield", category="Crime", description="Follows the lives and cases of a dirty Los Angeles Police Department cop and the unit under his command."))
items.append(Item(name="Deadwood", category="History", description="A show set in the late 1800s, revolving around the characters of Deadwood, South Dakota; a town of deep corruption and crime."))
items.append(Item(name="The Marvelous Mrs. Maisel ", category="Comedy", description="A housewife in the 1950s decides to become a stand-up comic."))
items.append(Item(name="Horace and Pete", category="Drama", description="Louis C.K.'s Eugene O'Neill-esque dramedic web series about two brothers, introverted Horace and mentally ill Pete, the current owners of their family's Irish bar Horace and Pete's, and their dysfunctional family and friends."))
items.append(Item(name="Top of the Lake", category="Mystery", description="Obsessed with the disappearance of a 12-year-old pregnant girl near a freezing lake in New Zealand, a brave detective will find herself up against small-town secrets and a side of herself that was meticulously kept at bay."))
items.append(Item(name="The Simpsons", category="Animation", description="The satiric adventures of a working-class family in the misfit city of Springfield."))
items.append(Item(name="The Walking Dead", category="Horror", description="Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins, and must lead a group of survivors to stay alive."))
items.append(Item(name="The Wire", category="Thriller", description="Baltimore drug scene, seen through the eyes of drug dealers and law enforcement."))
items.append(Item(name="Welt am Draht", category="Mystery", description="Somewhere in the future there is a computer project called Simulacron one of which is able to simulate a full featured reality, when suddenly project leader Henry Vollmer dies."))
items.append(Item(name="House of Cards", category="Drama", description="A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him."))
items.append(Item(name="Fargo", category="Thriller", description="Various chronicles of deception, intrigue and murder in and around frozen Minnesota. Yet all of these tales mysteriously lead back one way or another to Fargo, North Dakota."))
items.append(Item(name="Angel", category="Fantasy", description="The vampire Angel, cursed with a soul, moves to Los Angeles and aids people with supernatural-related problems while questing for his own redemption."))
items.append(Item(name="V", category="Adventure", description="A year after Liberation Day, courtesy of the red-dust bacteria, the humanoid, lizard-like aliens develop a resistance to the micro-organism and try to regain control of the Earth--only now some humans are knowingly working with them."))
items.append(Item(name="Jessica Jones", category="Action", description="Following the tragic end of her brief superhero career, Jessica Jones tries to rebuild her life as a private investigator, dealing with cases involving people with remarkable abilities in New York City."))
items.append(Item(name="Daredevil", category="Crime", description="Matt Murdock, with his other senses superhumanly enhanced, fights crime as a blind lawyer by day, and vigilante by night."))
items.append(Item(name="Seinfield", category="Comedy", description="The continuing misadventures of neurotic New York City stand-up comedian Jerry Seinfeld and his equally neurotic New York City friends."))
items.append(Item(name="Slings and Arrows", category="Comedy", description="In the fictional town of New Burbage, legendary theatrical madman Geoffrey Tennant returns to the New Burbage Theatre Festival, the site of his greatest triumph and most humiliating failure.."))
items.append(Item(name="I, Claudius ", category="Biography", description="The history of the Roman Empire as experienced by one of its rulers."))
items.append(Item(name="Rome", category="History", description="A down-to-earth account of the lives of both illustrious and ordinary Romans set in the last days of the Roman Republic."))


