#!/usr/bin/python3

from rich import print
from rich.style import Style
from rich.text import Text
from rich.console import Console
from rich.align import Align 
from rich.rule import Rule
import os, json, random
import datetime



def get_rand_quote():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(
        os.path.join(__location__, 'quotes.json'), 'r', encoding='utf-8'
    ) as quotes_file:
        list_of_quotes = json.load(quotes_file)
    return random.choice(list_of_quotes)

quote = get_rand_quote()

c = Console()
content = Text(quote["content"], style="italic cyan ")
author = Text("• " + quote["author"] + " •" , style="italic gray74 ")

greeting = Text(f" Hello, Hubert 💫 It's {datetime.date.today().strftime('%y%m%d')} {datetime.datetime.now().strftime('%H%M')} ", style="bold blue")
rule = Rule(title=greeting, style=Style(dim=True))
c.print(rule)
c.print()
c.print(Align.center(content))
c.print(Align.center(author))
