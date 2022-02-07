database = {"shakespeare":
            "William Shakespeare (26 April 1564 - 23 April 1616) was an\n"
            "English poet, and actor, widely regarded as the\n"
            "greatest writer in the English language and the world's\n"
            "pre-eminent dramatist.",
            "asimov":
            "Isaac Asimov (2 January 1920 - 6 April 1992) was an\n"
            "American writer and professor of Biochemistry, famous for\n"
            "his works of hard science fiction and popular science.",
            "homer":
            "Homer was an ancient Greek author and epic poet. He is the\n"
            "reputed author of the Iliad and the Odyssey, the two epic\n"
            "poems that are the foundational works of ancient Greek literature."
            }


def process(query):
    return [val for key, val in database.items() if key in query.lower()]
