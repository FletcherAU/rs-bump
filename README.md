## Clan thread notifications

This code checks a RS3 forum page specified by `url` for a thread title specified by `clan_str`. It can then be configured to do something based on the ranking (or lack thereof) of the thread in question.

### Parameters

* `url` - url to check
* `clan_str` - thread title to check for
* `trigger` - trigger behaviour
  * `not_on_front` - Send a notification if we're not on the first page
  * `threshold` - Send a notification if we're ranked higher than X
  * `always` - Send a notification no matter what
* `threshold` - The minimum notification position for the threshold trigger

### Notifications

Change the `notify` function.