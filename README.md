## Clan thread notifications

This code checks a RS3 forum page specified by `url` for a thread title specified by `clan_str`. It can then be configured to do something based on the ranking (or lack thereof) of the thread in question.

## Example console output

```
$ ./main.py
We're #1, we're #1!
-----
#1: Clan banana
#2: Clan apples
#3: Juice clan
...
#19: Carrot Company
```

```
./main.py
We're currently 3 on the recruitment forum. Time for a bump?
-----
#1: Clan apples
#2: Juice clan
#3: Clan banana
...
#20: Carrot Company```
