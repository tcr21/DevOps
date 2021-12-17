database = {"shakespeare":
            "William Shakespeare (26 April 1564 - 23 April 1616) was an\n"
            "English poet, playwright, and actor, widely regarded as the\n"
            "greatest writer in the English language and the world's\n"
            "pre-eminent dramatist.",
            "asimov":
            "Isaac Asimov (2 January 1920 - 6 April 1992) was an\n"
            "American writer and professor of Biochemistry, famous for\n"
            "his works of hard science fiction and popular science."
            }


def process(query):
    return '\n'.join(val for key, val in database.items() if key in query)
